# -*- coding: utf-8 -*-
#################################################################
#                                                               #
#               NOMBRE PLUGIN : WIZARDCONVERTFORMAT             #
#                          VER. 0.1                             #
#               CREADOR : NICOLÁS QUEZADA QUEZADA               #
#                                                               #
#################################################################
"""
WizardConvertFormat

Función: wizard para importar versiones anteriores de Fullaxis, 
CSV y Json sin formato al formato Json-faxy (*.faxy)


Flujo de funcionamiento: - aparece un nuevo botón en la ventana
                           del creador de registros bajo la lista 
                           de pruebas:
                           (importar desde versiones anteriores) 
                         - Seleccione un archivo de las versiones 
                           anteriores para realizar la transformación
                           si el formato es CSV se le mostrarán unos
                           gráficos para que seleccione los ejes 
                           correctos.


Dependencias: *faxyCreateRegister

"""