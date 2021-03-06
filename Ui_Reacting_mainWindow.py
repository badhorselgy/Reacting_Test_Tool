# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\课外项目资料（图像处理）\图形界面制作(PyQt5)\Reacting_Games\Reacting_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 600)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/IMG_2775(20200519-194904).JPG"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("border-color: rgb(170, 255, 0);\n"
"background-color: rgb(170, 255, 255);")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Reacting_button = QtWidgets.QPushButton(self.centralwidget)
        self.Reacting_button.setGeometry(QtCore.QRect(170, 280, 371, 101))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(48)
        font.setItalic(True)
        self.Reacting_button.setFont(font)
        self.Reacting_button.setAutoFillBackground(False)
        self.Reacting_button.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.Reacting_button.setObjectName("Reacting_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 30, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.Start_button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_button.setGeometry(QtCore.QRect(170, 190, 101, 41))
        self.Start_button.setAutoFillBackground(False)
        self.Start_button.setStyleSheet("border-color: rgb(255, 255, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.Start_button.setObjectName("Start_button")
        self.Scoreboard_button = QtWidgets.QPushButton(self.centralwidget)
        self.Scoreboard_button.setGeometry(QtCore.QRect(310, 190, 91, 41))
        self.Scoreboard_button.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Scoreboard_button.setObjectName("Scoreboard_button")
        self.Quit_button = QtWidgets.QPushButton(self.centralwidget)
        self.Quit_button.setGeometry(QtCore.QRect(440, 190, 101, 41))
        self.Quit_button.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Quit_button.setObjectName("Quit_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 90, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 16pt \"Bradley Hand ITC\";\n"
"\n"
"")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Quit_button.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reacting!!!"))
        self.Reacting_button.setText(_translate("MainWindow", "Reacting!"))
        self.label.setText(_translate("MainWindow", "Reacting test"))
        self.Start_button.setText(_translate("MainWindow", "START"))
        self.Scoreboard_button.setText(_translate("MainWindow", "Scoreboard"))
        self.Quit_button.setText(_translate("MainWindow", "QUIT"))
        self.label_2.setText(_translate("MainWindow", "Press START button (or press key S) to start the test\n"
"When the surface turn green, it means that the test has started.\n"
"When the surface turn red, press the \'Reacting\' button (or press key SPACE) as soon as possible!\n"
""))
import Window_icon_rc
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")