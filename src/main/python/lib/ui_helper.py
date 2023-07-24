
from PySide6.QtGui import QImage, QPixmap,QAction
from PySide6.QtWidgets import QMenu
from lib.CustomWidgets import TabButton

class Helpers():
    def __init__(self) -> None:
        pass
    
    def reset_layout(self, layout) -> None:
        """permite eliminar todos los items que se encuentren en el layout 
            para poder ingresar nuevos items

        Args:
            layout (QLayout): Layout que se desea resetear
        """
        for i in reversed(range(layout.count())): 
            widgetToRemove = layout.itemAt(i).widget()
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)
    
    
    def handle_selection(self, selected, deselected):
        """crea un diccionario con los items seleccionados y deseleccionados

        Args:
            selected (QItemSelection): Items seleccionados
            deselected (QItemSelection): Items deseleccionados

        Returns:
            dict: Diccionario con los items seleccionados y deseleccionados
        """
        for index in selected.indexes():
            item = self.list_records.itemFromIndex(index)
            sel = [index.row(), index.column(), item.text()]
        for index in deselected.indexes():
            item = self.list_records.itemFromIndex(index)
            desel = [index.row(), index.column(), item.text()]
        
        return {'selected': sel, 'deselected': desel}
    
    def menu(self, button, action_func, list_):
        menu = QMenu()
        test = list_
        for i in test:
            action = QAction(i, button)
            action.triggered.connect(action_func)
            menu.addAction(action)
        return menu


class TabsHelper():
    def __init__(self, tab_layout , tab_widget) -> None:
        self.tabs_layout = tab_layout
        self.tabs_widget = tab_widget
        self.last_tab = 0
    
    def create_tab(self, test, func_select, func_close):
        self.last_tab += 1
        tab = TabButton(test, f"new {test} {self.last_tab}")
        tab.setObjectName(f"tab_{self.last_tab}")
        tab.click_close.connect(self.close_tab)
        tab.click_tab.connect(self.select_tab)
        tab.click_tab.connect(func_select)
        tab.click_close.connect(func_close)

        tab.setName(f"tab_{self.last_tab}")
        self.tabs_layout.addWidget(tab)
        self.select_tab(f"tab_{self.last_tab}")
        return f"tab_{self.last_tab}"

    def close_tab(self, tab_name=None):
        if tab_name is None:
            tab_name = self.sender().objectName()
        tab = self.tabs_widget.findChild(TabButton, tab_name)
        if tab is not None:
            self.tabs_layout.removeWidget(tab)
            tab.deleteLater()

    def select_tab(self, tab_name=None):
        if tab_name is None:
            tab_name = self.sender().objectName()
        tabs = self.tabs_widget.findChildren(TabButton)
        for tab in tabs:
            if tab.objectName() == tab_name:
                tab.setActive(True)
            else:
                tab.setActive(False)
        return tab_name
    
    def type_tab(self, tab_name=None):
        tab = self.tabs_widget.findChild(TabButton, tab_name)
        return tab.get_test()
        



        