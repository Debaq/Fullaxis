class helpers():
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

        