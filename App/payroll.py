# Form implementation generated from reading ui file 'Payroll2.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
import pymysql

class Ui_MainWin(object):
    def setupUi(self, MainWin):
        MainWin.setObjectName("MainWin")
        MainWin.resize(1326, 1527)
        self.centralwidget = QtWidgets.QWidget(parent=MainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(310, 10, 751, 791))
        self.widget.setStyleSheet("border : 1px solid blue;")
        self.widget.setObjectName("widget")
        self.Welcome_lbl = QtWidgets.QLabel(parent=self.widget)
        self.Welcome_lbl.setGeometry(QtCore.QRect(30, 10, 221, 41))
        self.Welcome_lbl.setObjectName("Welcome_lbl")
        self.Greeting_lbl = QtWidgets.QLabel(parent=self.widget)
        self.Greeting_lbl.setGeometry(QtCore.QRect(100, 60, 211, 31))
        self.Greeting_lbl.setObjectName("Greeting_lbl")
        self.Time_lbl = QtWidgets.QLabel(parent=self.widget)
        self.Time_lbl.setGeometry(QtCore.QRect(420, 60, 161, 31))
        self.Time_lbl.setObjectName("Time_lbl")
        self.Payroll_lbl = QtWidgets.QLabel(parent=self.widget)
        self.Payroll_lbl.setGeometry(QtCore.QRect(90, 130, 581, 31))
        self.Payroll_lbl.setObjectName("Payroll_lbl")
        self.BasicSal_lbl = QtWidgets.QLabel(parent=self.widget)
        self.BasicSal_lbl.setGeometry(QtCore.QRect(30, 300, 171, 31))
        self.BasicSal_lbl.setStyleSheet("border : opx solid black;")
        self.BasicSal_lbl.setObjectName("BasicSal_lbl")
        self.Transport_lbl = QtWidgets.QLabel(parent=self.widget)
        self.Transport_lbl.setGeometry(QtCore.QRect(30, 350, 171, 31))
        self.Transport_lbl.setStyleSheet("border : 0px solid black ;")
        self.Transport_lbl.setObjectName("Transport_lbl")
        self.Feeding_lbl = QtWidgets.QLabel(parent=self.widget)
        self.Feeding_lbl.setGeometry(QtCore.QRect(30, 400, 171, 31))
        self.Feeding_lbl.setStyleSheet("border :0px solid black;")
        self.Feeding_lbl.setObjectName("Feeding_lbl")
        self.Clothing_lbl = QtWidgets.QLabel(parent=self.widget)
        self.Clothing_lbl.setGeometry(QtCore.QRect(30, 450, 171, 31))
        self.Clothing_lbl.setStyleSheet("border : 0px solid black")
        self.Clothing_lbl.setObjectName("Clothing_lbl")
        self.Utility_lbl = QtWidgets.QLabel(parent=self.widget)
        self.Utility_lbl.setGeometry(QtCore.QRect(30, 490, 171, 31))
        self.Utility_lbl.setStyleSheet("border : 0px solid black;")
        self.Utility_lbl.setObjectName("Utility_lbl")
        self.Pfa_lbl = QtWidgets.QLabel(parent=self.widget)
        self.Pfa_lbl.setGeometry(QtCore.QRect(30, 540, 171, 31))
        self.Pfa_lbl.setStyleSheet("border : 0px sold black")
        self.Pfa_lbl.setObjectName("Pfa_lbl")
        self.Tax_lbl = QtWidgets.QLabel(parent=self.widget)
        self.Tax_lbl.setGeometry(QtCore.QRect(30, 590, 171, 31))
        self.Tax_lbl.setStyleSheet("border : 0px solid black ;")
        self.Tax_lbl.setObjectName("Tax_lbl")
        self.ErrorBox_lbl = QtWidgets.QLabel(parent=self.widget)
        self.ErrorBox_lbl.setGeometry(QtCore.QRect(30, 730, 671, 41))
        self.ErrorBox_lbl.setText("")
        self.ErrorBox_lbl.setObjectName("ErrorBox_lbl")
        self.BasicSal_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        self.BasicSal_lnedit.setGeometry(QtCore.QRect(270, 310, 161, 21))
        self.BasicSal_lnedit.setObjectName("BasicSal_lnedit")
        self.Transport_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        self.Transport_lnedit.setGeometry(QtCore.QRect(270, 360, 161, 21))
        self.Transport_lnedit.setObjectName("Transport_lnedit")
        self.Feeding_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        self.Feeding_lnedit.setGeometry(QtCore.QRect(270, 400, 161, 22))
        self.Feeding_lnedit.setObjectName("Feeding_lnedit")
        self.Clothing_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        self.Clothing_lnedit.setGeometry(QtCore.QRect(270, 450, 161, 22))
        self.Clothing_lnedit.setObjectName("Clothing_lnedit")
        self.Utility_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        self.Utility_lnedit.setGeometry(QtCore.QRect(270, 500, 161, 22))
        self.Utility_lnedit.setObjectName("Utility_lnedit")
        self.Pfa_linedi = QtWidgets.QLineEdit(parent=self.widget)
        self.Pfa_linedi.setGeometry(QtCore.QRect(270, 550, 161, 22))
        self.Pfa_linedi.setObjectName("Pfa_linedi")
        self.Tax_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        self.Tax_lnedit.setGeometry(QtCore.QRect(270, 600, 161, 22))
        self.Tax_lnedit.setObjectName("Tax_lnedit")
        self.Submit_PushBtn = QtWidgets.QPushButton(parent=self.widget)
        self.Submit_PushBtn.setGeometry(QtCore.QRect(110, 670, 171, 28))
        self.Submit_PushBtn.setObjectName("Submit_PushBtn")
        self.Submit_PushBtn.clicked.connect(self.calculate_sal)
        self.Clear_PushBtn = QtWidgets.QPushButton(parent=self.widget)
        self.Clear_PushBtn.setGeometry(QtCore.QRect(500, 670, 171, 28))
        self.Clear_PushBtn.setObjectName("Clear_PushBtn")
        self.Clear_PushBtn.clicked.connect(self.clear)
        self.Back_PushBtn = QtWidgets.QPushButton(parent=self.widget)
        self.Back_PushBtn.setGeometry(QtCore.QRect(310, 670, 171, 28))  # Adjusted position
        self.Back_PushBtn.setObjectName("Back_PushBtn")
        self.Back_PushBtn.setVisible(True)
        self.Back_PushBtn.clicked.connect(MainWin.close)
        self.Enter_PushBtn = QtWidgets.QPushButton(parent=self.widget)
        self.Enter_PushBtn.setGeometry(QtCore.QRect(560, 420, 111, 51))
        self.Enter_PushBtn.setObjectName("Enter_PushBtn")
        self.Enter_PushBtn.clicked.connect(self.calculate_sal)
        self.Salary_lbl = QtWidgets.QLabel(parent=self.widget)
        self.Salary_lbl.setGeometry(QtCore.QRect(20, 260, 221, 31))
        self.Salary_lbl.setStyleSheet("border :0px solid black;")
        self.Salary_lbl.setObjectName("Salary_lbl")
        self.Salary_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        self.Salary_lnedit.setGeometry(QtCore.QRect(270, 260, 161, 22))
        self.Salary_lnedit.setObjectName("Salary_lnedit")
        self.Salary_lnedit.editingFinished.connect(self.calculate_sal)
        MainWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1326, 26))
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
        new_time = current_time.strftime('%I:%M:%p')  # 12hr format with am/pm
        self.Time_lbl.setText(new_time)
        if current_time.hour < 12:
            greeting = 'Good Morning'
        else:
            greeting = 'Good Afternoon'

        self.Greeting_lbl.setText(greeting)

    def calculate_sal(self):
        try:
            salary = float(self.Salary_lnedit.text())
        except ValueError:
            self.ErrorBox_lbl.setText('Please Enter A Valid Number')
            return
        basic_salary = salary * 0.48
        transport = salary * 0.10
        feeding = salary * 0.15
        clothing = salary * 0.10
        utility = salary * 0.05
        pfa = salary * 0.05
        tax = salary *0.02
        salary = basic_salary + transport + feeding + clothing + utility + pfa - tax

        self.BasicSal_lnedit.setText(f'{basic_salary : 2f}')
        self.Transport_lnedit.setText(f'{transport : 2f}')
        self.Feeding_lnedit.setText(f'{feeding : 2f}')
        self.Clothing_lnedit.setText(f'{clothing : 2f}')
        self.Utility_lnedit.setText(f'{utility : 2f}')
        self.Pfa_linedi.setText(f'{pfa : 2f}')
        self.Tax_lnedit.setText(f'{tax : 2f}')

        db_conn = pymysql.connect(
            user='root',
            password='',
            host='localhost',
            database='app_db'
        )
        cur = db_conn.cursor()
        insert_query = ("INSERT INTO Payroll_tbl (Basic_Salary, Transport, Feeding, Clothing, Utility, Pfa, Tax)"
                        " VALUES (%s, %s, %s, %s, %s, %s, %s)")
        values = (basic_salary, transport, feeding, clothing, utility, pfa, tax)
        db_conn.commit()

    def clear(self):
        self.BasicSal_lnedit.clear()
        self.Transport_lnedit.clear()
        self.Feeding_lnedit.clear()
        self.Clothing_lnedit.clear()
        self.Utility_lnedit.clear()
        self.Pfa_linedi.clear()
        self.Tax_lnedit.clear()

        # self.BasicSal_lbl.clear()
        # self.Transport_lbl.clear()
        # self.Feeding_lbl.clear()
        # self.Clothing_lbl.clear()
        # self.Utility_lbl.clear()
        # self.Pfa_lbl.clear()
        # self.Tax_lbl.clear()

    def back(self):
        self.Salary_lnedit.clear()
        self.BasicSal_lnedit.clear()
        self.Transport_lnedit.clear()
        self.Feeding_lnedit.clear()
        self.Clothing_lnedit.clear()
        self.Utility_lnedit.clear()
        self.Pfa_linedi.clear()
        self.Tax_lnedit.clear()
        self.ErrorBox_lbl.clear()
        self.Back_PushBtn.setVisible(True)


    def retranslateUi(self, MainWin):
        _translate = QtCore.QCoreApplication.translate
        MainWin.setWindowTitle(_translate("MainWin", "Payroll"))
        self.Welcome_lbl.setText(_translate("MainWin",'Welcome BigBaby' "<html><head/><body><p><br/></p></body></html>"))
        self.Greeting_lbl.setText(_translate("MainWin", "<html><head/><body><p><br/></p></body></html>"))
        self.Time_lbl.setText(_translate("MainWin", "<html><head/><body><p><br/></p></body></html>"))
        self.Payroll_lbl.setText(_translate("MainWin", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">PAYROLL</span></p></body></html>"))
        self.BasicSal_lbl.setText(_translate("MainWin", "<html><head/><body><p><span style=\" font-size:12pt;\">BASIC SALARY</span></p></body></html>"))
        self.Transport_lbl.setText(_translate("MainWin", "<html><head/><body><p><span style=\" font-size:12pt;\">TRANSPORT</span></p></body></html>"))
        self.Feeding_lbl.setText(_translate("MainWin", "<html><head/><body><p><span style=\" font-size:12pt;\">FEEDING</span></p></body></html>"))
        self.Clothing_lbl.setText(_translate("MainWin", "<html><head/><body><p><span style=\" font-size:12pt;\">CLOTHING</span></p></body></html>"))
        self.Utility_lbl.setText(_translate("MainWin", "<html><head/><body><p><span style=\" font-size:12pt;\">UTILITY</span></p></body></html>"))
        self.Pfa_lbl.setText(_translate("MainWin", "<html><head/><body><p><span style=\" font-size:12pt;\">PFA </span></p></body></html>"))
        self.Tax_lbl.setText(_translate("MainWin", "<html><head/><body><p><span style=\" font-size:12pt;\">TAX</span></p></body></html>"))
        self.Submit_PushBtn.setText(_translate("MainWin", "SUBMIT"))
        self.Clear_PushBtn.setText(_translate("MainWin", "CLEAR"))
        self.Back_PushBtn.setText(_translate("MainWin", "BACK"))
        self.Enter_PushBtn.setText(_translate("MainWin", "Show"))
        self.Salary_lbl.setText(_translate("MainWin", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">SALARY (MONTHLY)</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWin = QtWidgets.QMainWindow()
    ui = Ui_MainWin()
    ui.setupUi(MainWin)
    MainWin.show()
    sys.exit(app.exec())