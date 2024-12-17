import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(
        self,
        parent=None,
    ):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.startButton.clicked.connect(self.hello)

    def hello(self):
        text = self.ui.lineEdit.text()
        if text == "":
            text = "Oo"
        self.ui.centretext.setText(f"Проверка, {text}!!!")


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
