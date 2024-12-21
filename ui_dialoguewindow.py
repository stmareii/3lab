# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialoguewindow.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(338, 143)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.515778, y1:0.049, x2:0.513, y2:1, stop:0 rgba(100, 53, 95, 255), stop:1 rgba(0, 0, 0, 255))")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        font1 = QFont()
        font1.setBold(False)
        self.comboBox.setFont(font1)

        self.verticalLayout.addWidget(self.comboBox)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u041b\u0435\u0433\u043a\u0438\u0439", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u0421\u043b\u043e\u0436\u043d\u044b\u0439", None))

    # retranslateUi

