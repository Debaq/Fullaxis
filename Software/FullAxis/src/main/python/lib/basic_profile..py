# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basic_profile.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFontComboBox, QFormLayout,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(749, 603)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_profile = QWidget()
        self.tab_profile.setObjectName(u"tab_profile")
        self.formLayout = QFormLayout(self.tab_profile)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_number = QLabel(self.tab_profile)
        self.lbl_number.setObjectName(u"lbl_number")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_number)

        self.input_number = QLabel(self.tab_profile)
        self.input_number.setObjectName(u"input_number")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.input_number)

        self.lbl_first_name = QLabel(self.tab_profile)
        self.lbl_first_name.setObjectName(u"lbl_first_name")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_first_name)

        self.input_first_name = QLineEdit(self.tab_profile)
        self.input_first_name.setObjectName(u"input_first_name")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.input_first_name)

        self.lbl_last_name = QLabel(self.tab_profile)
        self.lbl_last_name.setObjectName(u"lbl_last_name")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_last_name)

        self.input_last_name = QLineEdit(self.tab_profile)
        self.input_last_name.setObjectName(u"input_last_name")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.input_last_name)

        self.lbl_id = QLabel(self.tab_profile)
        self.lbl_id.setObjectName(u"lbl_id")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_id)

        self.input_id = QLineEdit(self.tab_profile)
        self.input_id.setObjectName(u"input_id")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.input_id)

        self.lbl_date_birth = QLabel(self.tab_profile)
        self.lbl_date_birth.setObjectName(u"lbl_date_birth")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_date_birth)

        self.input_date_birth = QDateEdit(self.tab_profile)
        self.input_date_birth.setObjectName(u"input_date_birth")
        self.input_date_birth.setCalendarPopup(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.input_date_birth)

        self.lbl_info = QLabel(self.tab_profile)
        self.lbl_info.setObjectName(u"lbl_info")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lbl_info)

        self.input_info = QTextEdit(self.tab_profile)
        self.input_info.setObjectName(u"input_info")
        font = QFont()
        font.setPointSize(8)
        self.input_info.setFont(font)
        self.input_info.setAutoFormatting(QTextEdit.AutoAll)
        self.input_info.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.input_info)

        self.btn_save = QPushButton(self.tab_profile)
        self.btn_save.setObjectName(u"btn_save")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.btn_save)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.tab_profile)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(30, 16777215))
        font1 = QFont()
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.tab_profile)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(30, 16777215))
        font2 = QFont()
        font2.setItalic(False)
        font2.setUnderline(True)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.tab_profile)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(30, 16777215))
        font3 = QFont()
        font3.setItalic(True)
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.spinBox = QSpinBox(self.tab_profile)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(40, 16777215))
        self.spinBox.setMinimum(6)
        self.spinBox.setMaximum(18)
        self.spinBox.setValue(8)

        self.horizontalLayout_2.addWidget(self.spinBox)

        self.fontComboBox = QFontComboBox(self.tab_profile)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.horizontalLayout_2.addWidget(self.fontComboBox)

        self.line = QFrame(self.tab_profile)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.btn_pred = QPushButton(self.tab_profile)
        self.btn_pred.setObjectName(u"btn_pred")

        self.horizontalLayout_2.addWidget(self.btn_pred)


        self.formLayout.setLayout(6, QFormLayout.SpanningRole, self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_profile, "")
        self.tab_record = QWidget()
        self.tab_record.setObjectName(u"tab_record")
        self.verticalLayout_4 = QVBoxLayout(self.tab_record)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btn_create_session = QPushButton(self.tab_record)
        self.btn_create_session.setObjectName(u"btn_create_session")

        self.horizontalLayout_3.addWidget(self.btn_create_session)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.list_records = QTreeWidget(self.tab_record)
        self.list_records.setObjectName(u"list_records")

        self.verticalLayout_4.addWidget(self.list_records)

        self.tabWidget.addTab(self.tab_record, "")
        self.tab_session = QWidget()
        self.tab_session.setObjectName(u"tab_session")
        self.verticalLayout_3 = QVBoxLayout(self.tab_session)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalFrame = QFrame(self.tab_session)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.horizontalFrame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_new_sot = QPushButton(self.horizontalFrame)
        self.btn_new_sot.setObjectName(u"btn_new_sot")

        self.horizontalLayout.addWidget(self.btn_new_sot)

        self.btn_new_tug = QPushButton(self.horizontalFrame)
        self.btn_new_tug.setObjectName(u"btn_new_tug")

        self.horizontalLayout.addWidget(self.btn_new_tug)


        self.verticalLayout_2.addWidget(self.horizontalFrame)

        self.widget_session = QWidget(self.tab_session)
        self.widget_session.setObjectName(u"widget_session")
        self.layout_session = QVBoxLayout(self.widget_session)
        self.layout_session.setSpacing(0)
        self.layout_session.setObjectName(u"layout_session")
        self.layout_session.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.widget_session)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab_session, "")

        self.verticalLayout.addWidget(self.tabWidget)

        QWidget.setTabOrder(self.tabWidget, self.input_first_name)
        QWidget.setTabOrder(self.input_first_name, self.input_last_name)
        QWidget.setTabOrder(self.input_last_name, self.input_id)
        QWidget.setTabOrder(self.input_id, self.input_date_birth)
        QWidget.setTabOrder(self.input_date_birth, self.input_info)
        QWidget.setTabOrder(self.input_info, self.btn_pred)
        QWidget.setTabOrder(self.btn_pred, self.fontComboBox)
        QWidget.setTabOrder(self.fontComboBox, self.spinBox)
        QWidget.setTabOrder(self.spinBox, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.btn_save)
        QWidget.setTabOrder(self.btn_save, self.btn_new_tug)
        QWidget.setTabOrder(self.btn_new_tug, self.btn_new_sot)

        self.retranslateUi(Form)
        self.fontComboBox.currentFontChanged.connect(self.input_info.setCurrentFont)
        self.pushButton_2.clicked["bool"].connect(self.input_info.setFontUnderline)
        self.pushButton_3.clicked["bool"].connect(self.input_info.setFontItalic)
        self.spinBox.valueChanged.connect(self.input_info.setFontWeight)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_number.setText(QCoreApplication.translate("Form", u"Number", None))
        self.input_number.setText(QCoreApplication.translate("Form", u"nn", None))
        self.lbl_first_name.setText(QCoreApplication.translate("Form", u"First name", None))
        self.lbl_last_name.setText(QCoreApplication.translate("Form", u"Last name", None))
        self.lbl_id.setText(QCoreApplication.translate("Form", u"Id", None))
        self.lbl_date_birth.setText(QCoreApplication.translate("Form", u"Date of birth", None))
        self.lbl_info.setText(QCoreApplication.translate("Form", u"Info", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"B", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"U", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"I", None))
        self.btn_pred.setText(QCoreApplication.translate("Form", u"pred.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_profile), QCoreApplication.translate("Form", u"Profile", None))
        self.btn_create_session.setText(QCoreApplication.translate("Form", u"Create Session", None))
        ___qtreewidgetitem = self.list_records.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"Date", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"Activity", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"Session", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_record), QCoreApplication.translate("Form", u"Records", None))
        self.label.setText(QCoreApplication.translate("Form", u"Last:", None))
        self.btn_new_sot.setText(QCoreApplication.translate("Form", u"New SOT", None))
        self.btn_new_tug.setText(QCoreApplication.translate("Form", u"New TUG", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_session), QCoreApplication.translate("Form", u"Session", None))
    # retranslateUi

