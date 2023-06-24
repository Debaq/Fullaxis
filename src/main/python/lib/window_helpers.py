from PySide6.QtWidgets import  QMessageBox


def check_screen_resolution(app):
    screen_resolution = app.primaryScreen().size()
    if screen_resolution.width() < 1280 or screen_resolution.height() < 720:
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Resolución de pantalla insuficiente")
        msgBox.setInformativeText("Se necesita una resolución mínima de 720p para ejecutar este programa.")
        msgBox.exec()
        return False
    else:
        return True