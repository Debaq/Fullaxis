from PySide6 import QtCore, QtGui, QtWidgets


class TaskDelegate(QtWidgets.QItemDelegate):
    # based on https://stackoverflow.com/a/8036666/1504082
    # https://doc.qt.io/archives/qt-4.7/qitemdelegate.html#drawDisplay
    # https://doc.qt.io/archives/qt-4.7/qwidget.html#render
    margin_x = 5
    margin_y = 3

    def drawDisplay(self, painter, option, rect, text):
        label = self.make_label(option, text)
        # calculate render anchor point
        point = rect.topLeft()
        point.setX(point.x() + self.margin_x)
        point.setY(point.y() + self.margin_y)

        label.render(painter, point, renderFlags=QtWidgets.QWidget.DrawChildren)

    def sizeHint(self, option, index):
        # get text using model and index
        text = index.model().data(index)
        label = self.make_label(option, text)
        return QtCore.QSize(label.width(), label.height() + self.margin_y)

    def make_label(self, option, text):
        label = QtWidgets.QLabel(text)

        if option.state & QtWidgets.QStyle.State_Selected:
            p = option.palette
            p.setColor(QtGui.QPalette.WindowText,
                       p.color(QtGui.QPalette.Active,
                               QtGui.QPalette.HighlightedText)
                       )

            label.setPalette(p)

        label.setStyleSheet("border: 1px dotted black")

        # adjust width according to widget's target width
        label.setMinimumWidth(self.target_width - (2 * self.margin_x))
        label.setMaximumWidth(self.target_width - self.margin_x)
        label.setWordWrap(True)
        label.adjustSize()
        
        return label


class CustomQCompleter(QtWidgets.QCompleter):
    """ Implement "contains" filter mode as the filter mode "contains" is not
    available in Qt < 5.2
    From: https://stackoverflow.com/a/7767999/1504082 """

    def __init__(self, parent=None):
        super(CustomQCompleter, self).__init__(parent)
        self.local_completion_prefix = ""
        self.source_model = None
        self.delegate = TaskDelegate()
        # widget not set yet
        # self.delegate.target_width = self.widget().width()

    def setModel(self, model):
        self.source_model = model
        super(CustomQCompleter, self).setModel(self.source_model)

    def updateModel(self):
        local_completion_prefix = self.local_completion_prefix

        # see: http://doc.qt.io/qt-4.8/model-view-programming.html#proxy-models
        class InnerProxyModel(QtCore.QSortFilterProxyModel):
            def filterAcceptsRow(self, sourceRow, sourceParent):
                # model index mapping by row, 1d model => column is always 0
                index = self.sourceModel().index(sourceRow, 0, sourceParent)
                source_data = self.sourceModel().data(index, QtCore.Qt.DisplayRole)
                # performs case insensitive matching
                # return True if item shall stay in th returned filtered data
                # return False to reject an item
                return local_completion_prefix.lower() in source_data.lower()

        proxy_model = InnerProxyModel()
        proxy_model.setSourceModel(self.source_model)
        super(CustomQCompleter, self).setModel(proxy_model)
        # @todo: Why to be set here again?
        # -> rescale popup list items to widget width
        self.delegate.target_width = self.widget().width()
        self.popup().setItemDelegate(self.delegate)

    def splitPath(self, path):
        self.local_completion_prefix = path
        self.updateModel()
        return ""


class AutoCompleteEdit(QtWidgets.QLineEdit):
    data_signal = QtCore.Signal(str)
    """ Basically from:
    http://doc.qt.io/qt-5/qtwidgets-tools-customcompleter-example.html
    """

    def __init__(self, list_data, placehold='', separator=' ', addSpaceAfterCompleting=True):
        super(AutoCompleteEdit, self).__init__()
        # settings
        self.setPlaceholderText(placehold)
        self._separator = separator
        self._addSpaceAfterCompleting = addSpaceAfterCompleting
        # completer
        self._completer = CustomQCompleter(self)
        self._completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self._completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

        self.model = QtCore.QStringListModel(list_data)
        self._completer.setModel(self.model)

        # connect the completer to the line edit
        self._completer.setWidget(self)
        # trigger insertion of the selected completion when its activated
        self.connect(self._completer,
                     QtCore.SIGNAL('activated(QString)'),
                     self._insertCompletion)

        self._ignored_keys = [QtCore.Qt.Key_Enter,
                              QtCore.Qt.Key_Return,
                              QtCore.Qt.Key_Escape,
                              QtCore.Qt.Key_Tab]

    def _insertCompletion(self, completion):
        """
        This is the event handler for the QCompleter.activated(QString) signal,
        it is called when the user selects an item in the completer popup.
        It will remove the already typed string with the one of the completion.
        """
        stripped_text = self.text()[:-len(self._completer.completionPrefix())]
        extra_text = completion  # [-extra:]
        if self._addSpaceAfterCompleting:
            extra_text += ' '
        self.setText(stripped_text + extra_text)
        self.data_signal.emit(self.text())

    def textUnderCursor(self):
        text = self.text()
        textUnderCursor = ''
        i = self.cursorPosition() - 1
        while i >= 0 and text[i] != self._separator:
            textUnderCursor = text[i] + textUnderCursor
            i -= 1
        return textUnderCursor

    def keyPressEvent(self, event):
        if self._completer.popup().isVisible() and event.key() in self._ignored_keys:
            event.ignore()
            return
        super(AutoCompleteEdit, self).keyPressEvent(event)
        completionPrefix = self.textUnderCursor()
        if completionPrefix != self._completer.completionPrefix():
            self._updateCompleterPopupItems(completionPrefix)
        if len(event.text()) > 0 and len(completionPrefix) > 0:
            self._completer.complete()
        if len(completionPrefix) == 0:
            self._completer.popup().hide()

    def _updateCompleterPopupItems(self, completionPrefix):
        """
        Filters the completer's popup items to only show items
        with the given prefix.
        """
        self._completer.setCompletionPrefix(completionPrefix)
        # self._completer.popup().setCurrentIndex(
        #     self._completer.completionModel().index(0, 0))


if __name__ == '__main__':
    def demo():
        import sys
        app = QtWidgets.QApplication(sys.argv)
        values = ['Germany',
                  'Austria',
                  'Switzerland',
                  'Hungary',
                  'The United Kingdom of Great Britain and Northern Ireland',
                  'USA']
        editor = AutoCompleteEdit(values)
        window = QtWidgets.QWidget()
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(editor)
        window.setLayout(hbox)
        window.show()

        sys.exit(app.exec_())

    demo()