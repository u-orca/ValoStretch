# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(211, 173)
        MainWindow.setMinimumSize(QSize(211, 173))
        MainWindow.setMaximumSize(QSize(211, 173))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning))
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.main = QWidget(MainWindow)
        self.main.setObjectName(u"main")
        self.label = QLabel(self.main)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(10, 40, 151, 16))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.label.setFont(font1)
        self.credits = QLabel(self.main)
        self.credits.setObjectName(u"credits")
        self.credits.setEnabled(True)
        self.credits.setGeometry(QRect(10, 150, 191, 18))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        self.credits.setFont(font2)
        self.lineEdit = QLineEdit(self.main)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 60, 81, 31))
        self.lineEdit.setFont(font1)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2 = QLineEdit(self.main)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 60, 81, 31))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QRect(90, 70, 31, 21))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.main)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 110, 191, 41))
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(9)
        font4.setBold(False)
        self.pushButton.setFont(font4)
        self.label_3 = QLabel(self.main)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QRect(10, 10, 191, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_3.setFont(font5)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.main)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ValoStretch", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select preferred resolution", None))
        self.credits.setText(QCoreApplication.translate("MainWindow", u"made by u-orca \U0001f408\U0000200d\U00002b1b", None))
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Set Resolution", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Valorant True Stretcher", None))
    # retranslateUi

