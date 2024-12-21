# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setStyleSheet(u"background-color: rgb(100, 53, 95)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setPlaceholderText("Введите числа здесь...") #!!
        self.lineEdit.setEnabled(False) #!!!
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        self.lineEdit.setFont(font1)

        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.startButton.setFont(font2)

        self.gridLayout.addWidget(self.startButton, 4, 0, 1, 1)

        self.centretext = QLabel(self.centralwidget)
        self.centretext.setObjectName(u"centretext")
        font3 = QFont()
        font3.setPointSize(17)
        font3.setBold(True)
        self.centretext.setFont(font3)
        self.centretext.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.centretext, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.checkButton = QPushButton(self.centralwidget)
        self.checkButton.setObjectName(u"checkButton")
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        self.checkButton.setFont(font4)
        self.checkButton.setEnabled(False)

        self.gridLayout.addWidget(self.checkButton, 5, 0, 1, 1)

        self.textWinLose = QLabel(self.centralwidget)
        self.textWinLose.setObjectName(u"textWinLose")
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(False)
        font5.setItalic(True)
        font5.setUnderline(False)
        self.textWinLose.setFont(font5)

        self.gridLayout.addWidget(self.textWinLose, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Game-test memory", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.centretext.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \"\u0421\u0442\u0430\u0440\u0442\", \u0447\u0442\u043e\u0431\u044b \u043d\u0430\u0447\u0430\u0442\u044c \u0438\u0433\u0440\u0443!", None))
        self.checkButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.textWinLose.setText(QCoreApplication.translate("MainWindow", u"", None))
    # retranslateUi

