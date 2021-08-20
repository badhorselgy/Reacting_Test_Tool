from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, pyqtSignal
import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStatusBar
from Ui_Reacting_mainWindow import Ui_MainWindow
import time


class Reacting_Games(QMainWindow, Ui_MainWindow):

    react_signal = pyqtSignal()
    t1 = 0
    t2 = 0

    def __init__(self, parent=None):
        #初始化并显示窗口
        super(Reacting_Games, self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.timer = QTimer(self)

        #私有变量初始化
        self.t1 = 0
        self.t2 = 0
        self.highscore = 0

        

        #高分记录文件读写，未实现
        # scores_file = open('thefile.txt')
        # scores_file.readline(1)
        
        #将信号连接到槽
        self.Start_button.clicked.connect(self.click_start_btn)
        self.Scoreboard_button.clicked.connect(self.click_Scoreboard_button_btn)
        self.Reacting_button.clicked.connect(self.click_reacting_btn)
        self.timer.timeout.connect(self.change_background_color)
        self.react_signal.connect(self.click_reacting_btn)

        self.label.grabKeyboard()   #控件开始捕获键盘
        self.statusbar.showMessage("Made by Mark Lau(AKA: superbadhorse), Central South University.")
        
    def click_start_btn(self):
        if not self.timer.isActive():
            print("Game start!")
            self.setStyleSheet("background-color:rgb(140, 210, 95);")
            delay_time = random.randint(15, 40)
            self.timer.setSingleShot(True)
            self.timer.start(delay_time*100)
            print(delay_time)
            
    def click_Scoreboard_button_btn(self):
        QMessageBox.information(self, 'Scoreboard', "Your highest score is %f, %s" % (self.highscore, (time.asctime(time.localtime(time.time())))))

    def click_reacting_btn(self):
        if self.t1 != 0:
            self.t2 = time.time()
            print("Your reacting time is %f" % (self.t2-self.t1))
            QMessageBox.setStyleSheet(self, "background-color: rgb(255, 255, 255);")
            QMessageBox.information(self, 'Result', "Your reacting time is %f" % (self.t2-self.t1))
            

            if self.highscore == 0:
                self.highscore = (self.t2-self.t1)
            elif (self.t2-self.t1) < self.highscore:
                self.highscore = (self.t2-self.t1)

            self.t1 = 0
            self.t2 = 0
        else:
            self.timer.stop()
            print("Please click the button after the surface turn red!!!\nClick start button to restart the game")
            QMessageBox.warning(self, 'Warning', "Please click the button after the surface turn red!!!")
            self.t1 = 0
            self.t2 = 0   

        self.setStyleSheet("background-color: rgb(170, 255, 255);")    

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key()== QtCore.Qt.Key.Key_Space:  #判断是否按下了空格键
            print('按下了空格键')
            self.react_signal.emit()
        if QKeyEvent.key()== QtCore.Qt.Key.Key_S:
            print('按下了S键')
            self.Start_button.clicked.emit()

            

    def change_background_color(self):
        print("background color change!")
        self.setStyleSheet("background-color:red;")
        self.t1 = time.time()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Win = Reacting_Games()
    sys.exit(app.exec_())