# Form implementation generated from reading ui file 'page11.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QLabel
from datetime import datetime



class Ui_MainWin(object):
    def setupUi(self, MainWin):
        MainWin.setObjectName("MainWin")
        MainWin.resize(1250, 748)
        self.centralwidget = QtWidgets.QWidget(parent=MainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(320, 30, 771, 601))
        self.widget.setStyleSheet("border : 1px solid black;\n"
"background-color : light gray;\n"
"color : ligh blue")
        self.widget.setObjectName("widget")
        self.welcome_lbl = QtWidgets.QLabel(parent=self.widget)
        self.welcome_lbl.setGeometry(QtCore.QRect(210, 20, 321, 51))
        self.welcome_lbl.setObjectName("welcome_lbl")
        self.welcome_lbl.setText('WELCOME BIG BABY')
        self.greeting_lbl = QtWidgets.QLabel(parent=self.widget)
        self.greeting_lbl.setGeometry(QtCore.QRect(40, 80, 221, 41))
        self.greeting_lbl.setObjectName("greeting_lbl")

        self.time_lbl = QtWidgets.QLabel(parent=self.widget)
        self.time_lbl.setGeometry(QtCore.QRect(360, 80, 251, 41))
        self.time_lbl.setObjectName("time_lbl")
        self.PAYROLL_PushBtn = QtWidgets.QPushButton(parent=self.widget)
        self.PAYROLL_PushBtn.setGeometry(QtCore.QRect(80, 190, 191, 41))
        self.PAYROLL_PushBtn.setObjectName("PAYROLL_PushBtn")
        self.PAYROLL_PushBtn.clicked.connect(self.showPayroll)
        self.ErrorBox_lbl = QtWidgets.QLabel(parent=self.widget)
        self.ErrorBox_lbl.setGeometry(QtCore.QRect(60, 540, 651, 51))
        self.ErrorBox_lbl.setText("")
        self.ErrorBox_lbl.setObjectName("ErrorBox_lbl")
        self.BMI_PushBtn = QtWidgets.QPushButton(parent=self.widget)
        self.BMI_PushBtn.setGeometry(QtCore.QRect(200, 250, 191, 41))
        self.BMI_PushBtn.setObjectName("BMI_PushBtn")
        self.BMI_PushBtn.clicked.connect(self.showBmi)
        self.TODO_PushBtn = QtWidgets.QPushButton(parent=self.widget)
        self.TODO_PushBtn.setGeometry(QtCore.QRect(350, 310, 191, 41))
        self.TODO_PushBtn.setObjectName("TODO_PushBtn")
        self.TODO_PushBtn.clicked.connect(self.showToDo)
        self.SI_PushBtn = QtWidgets.QPushButton(parent=self.widget)
        self.SI_PushBtn.setGeometry(QtCore.QRect(510, 370, 201, 41))
        self.SI_PushBtn.setObjectName("SI_PushBtn")
        self.SI_PushBtn.clicked.connect(self.showSimpleInterest)
        self.LogOut_PushBtn = QtWidgets.QPushButton(parent=self.widget)
        self.LogOut_PushBtn.setGeometry(QtCore.QRect(320, 470, 141, 41))
        self.LogOut_PushBtn.setObjectName("LogOut_PushBtn")
        self.LogOut_PushBtn.clicked.connect(MainWin.close)
        MainWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 26))
        self.menubar.setObjectName("menubar")
        MainWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWin)
        self.statusbar.setObjectName("statusbar")
        MainWin.setStatusBar(self.statusbar)

        self.retranslateUi(MainWin)
        QtCore.QMetaObject.connectSlotsByName(MainWin)

        self.updateTimeAndGreeting()

    def updateTimeAndGreeting(self):
        current_time = datetime.now()
        new_time = current_time.strftime('%I:%M:%p')  ###12hr format with am/pm
        self.time_lbl.setText(new_time)
        if current_time.hour < 12:
            greeting = 'Good Morning'
        else:
            greeting = 'Good Afternoon'

        self.greeting_lbl.setText(greeting)

    def showPayroll(self):
        from PyQt6.QtWidgets import QMainWindow
        from payroll import Ui_MainWin
        self.win = Ui_MainWin()
        self.main = QMainWindow()
        self.win.setupUi(self.main)
        self.main.show()

    def showBmi(self):
        from PyQt6.QtWidgets import QMainWindow
        from bmi import Ui_MainWin
        self.win = Ui_MainWin()
        self.main = QMainWindow()
        self.win.setupUi(self.main)
        self.main.show()


    def showToDo(self):
        from PyQt6.QtWidgets import QMainWindow
        from todo import Ui_MainWin
        self.win = Ui_MainWin()
        self.main = QMainWindow()
        self.win.setupUi(self.main)
        self.main.show()


    def showSimpleInterest(self):
        from PyQt6.QtWidgets import QMainWindow
        from simpleinterest import Ui_MainWin
        self.win = Ui_MainWin()
        self.main = QMainWindow()
        self.win.setupUi(self.main)
        self.main.show()



    def retranslateUi(self, MainWin):
        _translate = QtCore.QCoreApplication.translate
        MainWin.setWindowTitle(_translate("MainWin", "App"))
        self.welcome_lbl.setText(_translate("MainWin", 'Welcome BigBaby'"<html><head/><body><p><br/></p></body></html>"))
        self.greeting_lbl.setText(_translate("MainWin", "<html><head/><body><p><br/></p></body></html>"))
        self.time_lbl.setText(_translate("MainWin", "<html><head/><body><p><br/></p></body></html>"))
        self.PAYROLL_PushBtn.setText(_translate("MainWin", "PAYROLL"))
        self.BMI_PushBtn.setText(_translate("MainWin", "BMI"))
        self.TODO_PushBtn.setText(_translate("MainWin", "TO-DO APP"))
        self.SI_PushBtn.setText(_translate("MainWin", "SIMPLE INTEREST"))
        self.LogOut_PushBtn.setText(_translate("MainWin", "LOG OUT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWin = QtWidgets.QMainWindow()
    ui = Ui_MainWin()
    ui.setupUi(MainWin)
    MainWin.show()
    sys.exit(app.exec())