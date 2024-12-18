import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
import random
from PyQt6.QtCore import QTimer, Qt

# короче изменить переход между проверкой и следующим раундом,а также во время некст раундов менять кнопку "старт" на "продллжить"
# либо просто как то упростить себе жизнь ... можно добавить всплывающее окно(?) после "победы" или "проигрыша", дабы не менять главный текст?...


class MainWindow(QMainWindow):
    def __init__(
        self,
        parent=None,
    ):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.startButton.clicked.connect(self.startTest)
        self.ui.checkButton.clicked.connect(self.checkAnswer)

        self.level = 1  # текущий уровень сложности
        self.sequence = []  # Последовательность чисел вывод на экран
        self.show_time = 2000  # Время показа чисел в миллисекундах

    # здесь, при нажатии кнопки старт, мы получим рандом числа на экран на 2 сек
    def startTest(self):
        # text = self.ui.lineEdit.text() это проверка кода с ютуба хдхд
        # if text == "":
        #     text = "Oo"
        # self.ui.centretext.setText(f"Проверка, {text}!!!")
        self.sequence = [random.randint(0, 9) for _ in range(self.level + 2)]
        self.ui.centretext.setText(" ".join(map(str, self.sequence)))
        self.ui.lineEdit.setText("")
        self.ui.lineEdit.setEnabled(False)
        self.ui.checkButton.setEnabled(False)  # блок кнопки и ввода
        QTimer.singleShot(self.show_time, self.hideNumbers)

    def hideNumbers(self):
        self.ui.centretext.setText("Введите числа в правильном порядке:")
        self.ui.lineEdit.setEnabled(True)
        self.ui.checkButton.setEnabled(True)
        self.ui.lineEdit.setFocus()

    def checkAnswer(self):
        user_in = self.ui.lineEdit.text().strip()
        user_sequence = list(map(str, user_in.split()))

        if user_sequence == list(map(str, self.sequence)):
            self.ui.centretext.setText(
                "Excellent!! Вы ввели правильную последовательность."
            )
            self.level += 1
            self.show_time = max(1000, self.show_time - 200)
        else:
            self.ui.centretext.setText(
                f"Неверно:(\nПравильная последовательность была: {' '.join(map(str, self.sequence))})"
            )
            self.level = 1
            self.show_time = 2000
        self.ui.lineEdit.setEnabled(False)
        self.ui.checkButton.setEnabled(False)
        self.ui.centretext.setText("Нажмите 'старт', чтобы продолжить")


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
