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
    
def istest(text: str, test: str) -> bool:
    """
    Esta función verifica si el string 'test' coincide con los primeros caracteres del string 'text'.

    Parámetros:
    text (str): El string en el que se buscará la coincidencia.
    test (str): El string que se buscará al inicio de 'text'.

    Retorna:
    bool: True si 'test' coincide con los primeros caracteres de 'text', False en caso contrario.
    """
    return text.startswith(test)





        