import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from ui_mainwindow import Ui_MainWindow
from ui_dialoguewindow import Ui_Dialog
import random
from PySide6.QtCore import QTimer


class DifficultyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.difficulty = "Легкий"  #По умолч легкий

        # Привязываем событие изменения выбора к сохранению сложности
        self.ui.buttonBox.accepted.connect(self.acceptDifficulty)
        self.ui.buttonBox.rejected.connect(self.reject)

    def acceptDifficulty(self):
        self.difficulty = self.ui.comboBox.currentText()
        self.accept()  # Закрываем диалог с успешным результатом


class MainWindow(QMainWindow):
    def __init__(self, difficulty="Легкий", parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.startButton.clicked.connect(self.startTest)
        self.ui.checkButton.clicked.connect(self.checkAnswer)

        # Настройки сложности
        self.difficulty = difficulty
        self.setDifficultyParams()

        self.level = 1  # текущий уровень сложности
        self.sequence = []  # Последовательность чисел вывод на экран

    def setDifficultyParams(self):
        #Устанавливает параметры на основе сложности
        difficulties = {
            "Легкий": {"show_time": 3000, "sequence": 3},
            "Средний": {"show_time": 2000, "sequence": 5},
            "Сложный": {"show_time": 1500, "sequence": 7},
        }

        params = difficulties.get(self.difficulty, difficulties["Легкий"])
        self.show_time = params["show_time"]
        self.base_sequence = params["sequence"]

    def startTest(self):
        self.ui.startButton.setText("Начать заново")
        self.ui.textWinLose.setText("ヽ(*・ω・)ﾉ")
        self.sequence = [random.randint(0, 9) for _ in range(self.base_sequence + self.level - 1)]
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
            self.ui.textWinLose.setText(
                "Excellent! Всё правильноヽ(>∀<☆)ノ"
            )
            self.level += 1
            self.show_time = max(1000, self.show_time - 200)
        else:
            self.ui.textWinLose.setText(
                f"Неверно (μ_μ)... Правильно было: {' '.join(map(str, self.sequence))}"
            )
            self.level = 1
            self.setDifficultyParams()
        self.ui.lineEdit.setEnabled(False)
        self.ui.checkButton.setEnabled(False)
        self.ui.startButton.setText("Вперед")
        self.ui.centretext.setText("Нажмите 'Вперед', чтобы продолжить")


if __name__ == "__main__":
    app = QApplication()

    # Показываем диалог выбора сложности
    dialog = DifficultyDialog()
    if dialog.exec():
        difficulty = dialog.difficulty
    else:
        sys.exit(0)  # Если диалог был отменен, завершаем программу

    # Запускаем главное окно с выбранной сложностью
    window = MainWindow(difficulty)
    window.show()
    sys.exit(app.exec())
