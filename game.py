import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
import random
from PyQt6.QtCore import QTimer, Qt



class MainWindow(QMainWindow):
    def __init__(
        self,
        parent=None,
    ):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.startButton.clicked.connect(self.startTest)
        self.level = 1  # текущий уровень сложности
        self.sequence = []  # Последовательность чисел вывод на экран
        self.show_time = 2000  # Время показа чисел в миллисекундах

    # здесь, при нажатии кнопки старт, мы получим рандом числа на экран на 2 сек
    def startTest(self):
        # text = self.ui.lineEdit.text() это проверка кода с ютуба хдхд
        # if text == "":
        #     text = "Oo"
        # self.ui.centretext.setText(f"Проверка, {text}!!!")
        self.sequence = [random.randint(0,9) for _ in range(self.level + 2)]
        self.ui.centretext.setText(" ".join(map(str, self.sequence)))
        self.ui.lineEdit.setText("")
        self.ui.lineEdit.setEnabled(False)
        self.ui.checkButton.setEnabled(False) #блок кнопки и ввода
        QTimer.singleShot(...) #дописать после хайднамберс



if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
