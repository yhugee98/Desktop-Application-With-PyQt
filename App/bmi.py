# Form implementation generated from reading ui file 'Bmi.ui'
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
        MainWin.resize(1134, 760)
        self.centralwidget = QtWidgets.QWidget(parent=MainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.Qwidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.Qwidget.setGeometry(QtCore.QRect(290, 10, 781, 641))
        self.Qwidget.setStyleSheet("border : 1px solid blue;")
        self.Qwidget.setObjectName("Qwidget")
        self.Bmi_lbl = QtWidgets.QLabel(parent=self.Qwidget)
        self.Bmi_lbl.setGeometry(QtCore.QRect(120, 120, 561, 31))
        self.Bmi_lbl.setStyleSheet("border : 0px solid black;")
        self.Bmi_lbl.setObjectName("Bmi_lbl")
        self.Welcome_lbl = QtWidgets.QLabel(parent=self.Qwidget)
        self.Welcome_lbl.setGeometry(QtCore.QRect(50, 10, 301, 31))
        self.Welcome_lbl.setStyleSheet("border : 1px solid black;")
        self.Welcome_lbl.setObjectName("Welcome_lbl")
        self.Greeting_lbl = QtWidgets.QLabel(parent=self.Qwidget)
        self.Greeting_lbl.setGeometry(QtCore.QRect(440, 10, 301, 31))
        self.Greeting_lbl.setStyleSheet("border : 1px solid black;")
        self.Greeting_lbl.setObjectName("Greeting_lbl")
        self.Time_lbl = QtWidgets.QLabel(parent=self.Qwidget)
        self.Time_lbl.setGeometry(QtCore.QRect(310, 60, 161, 31))
        self.Time_lbl.setStyleSheet("border : 1px solid black;")
        self.Time_lbl.setObjectName("Time_lbl")
        self.Height_lbl = QtWidgets.QLabel(parent=self.Qwidget)
        self.Height_lbl.setGeometry(QtCore.QRect(34, 209, 181, 41))
        self.Height_lbl.setStyleSheet("border : 0px solid black;")
        self.Height_lbl.setObjectName("Height_lbl")
        self.Weight_lbl = QtWidgets.QLabel(parent=self.Qwidget)
        self.Weight_lbl.setGeometry(QtCore.QRect(30, 270, 181, 41))
        self.Weight_lbl.setStyleSheet("border : 0px solid black;")
        self.Weight_lbl.setObjectName("Weight_lbl")
        self.BmiResult_lbl = QtWidgets.QLabel(parent=self.Qwidget)
        self.BmiResult_lbl.setGeometry(QtCore.QRect(30, 430, 191, 51))
        self.BmiResult_lbl.setStyleSheet("border : 0px solix black;")
        self.BmiResult_lbl.setObjectName("BmiResult_lbl")
        self.ErrorBox_lbl = QtWidgets.QLabel(parent=self.Qwidget)
        self.ErrorBox_lbl.setGeometry(QtCore.QRect(60, 570, 671, 61))
        self.ErrorBox_lbl.setText("")
        self.ErrorBox_lbl.setObjectName("ErrorBox_lbl")
        self.Height_lnedit = QtWidgets.QLineEdit(parent=self.Qwidget)
        self.Height_lnedit.setGeometry(QtCore.QRect(190, 220, 221, 22))
        self.Height_lnedit.setObjectName("Height_lnedit")
        self.Weight_lnedit = QtWidgets.QLineEdit(parent=self.Qwidget)
        self.Weight_lnedit.setGeometry(QtCore.QRect(190, 280, 221, 22))
        self.Weight_lnedit.setObjectName("Weight_lnedit")
        self.BmiResult_lnedit = QtWidgets.QLineEdit(parent=self.Qwidget)
        self.BmiResult_lnedit.setGeometry(QtCore.QRect(410, 440, 221, 22))
        self.BmiResult_lnedit.setObjectName("BmiResult_lnedit")
        self.Kg_lbl = QtWidgets.QLabel(parent=self.Qwidget)
        self.Kg_lbl.setGeometry(QtCore.QRect(450, 270, 81, 31))
        self.Kg_lbl.setStyleSheet("border : 0px solid black;")
        self.Kg_lbl.setObjectName("Kg_lbl")
        self.Cm_lbl = QtWidgets.QLabel(parent=self.Qwidget)
        self.Cm_lbl.setGeometry(QtCore.QRect(450, 220, 81, 31))
        self.Cm_lbl.setStyleSheet("border : 0px solid black;")
        self.Cm_lbl.setObjectName("Cm_lbl")
        self.Calculate_PushBtn = QtWidgets.QPushButton(parent=self.Qwidget)
        self.Calculate_PushBtn.setGeometry(QtCore.QRect(480, 340, 231, 41))
        self.Calculate_PushBtn.setObjectName("Calculate_PushBtn")
        self.Calculate_PushBtn.clicked.connect(self.calculateBMI)
        self.Submit_PushBtn = QtWidgets.QPushButton(parent=self.Qwidget)
        self.Submit_PushBtn.setGeometry(QtCore.QRect(50, 480, 171, 41))
        self.Submit_PushBtn.setObjectName("Submit_PushBtn")
        self.Submit_PushBtn.clicked.connect(self.submitResults)
        self.Clear_Pushbutton = QtWidgets.QPushButton(parent=self.Qwidget)
        self.Clear_Pushbutton.setGeometry(QtCore.QRect(290, 480, 181, 41))
        self.Clear_Pushbutton.setObjectName("Clear_Pushbutton")
        self.Clear_Pushbutton.clicked.connect(self.clearFields)
        self.Back_Pushbutton = QtWidgets.QPushButton(parent=self.Qwidget)
        self.Back_Pushbutton.setGeometry(QtCore.QRect(530, 480, 181, 41))
        self.Back_Pushbutton.setObjectName("Back_Pushbutton")
        self.Back_Pushbutton.setVisible(True)
        self.Back_Pushbutton.clicked.connect(MainWin.close)
        MainWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1134, 26))
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

    def calculateBMI(self):
        height_text = self.Height_lnedit.text()
        weight_text = self.Weight_lnedit.text()

        if height_text and weight_text:
            try:
                height = float(height_text)
                weight = float(weight_text)
                if height > 0 and weight > 0:
                    bmi = weight / ((height / 100) ** 2)
                    self.BmiResult_lnedit.setText(f"{bmi:.2f}")

                    db_conn = pymysql.connect(
                        user='root',
                        password='',  # Replace with your MySQL password
                        host='localhost',
                        database='app_db'  # Replace with your database name
                    )
                    cur = db_conn.cursor()

                    insert_query = ("INSERT INTO Bmi_tbl (Height, Weight, Result) "
                                    "VALUES (%s, %s, %s)")
                    cur.execute(insert_query, (height, weight, bmi))
                    db_conn.commit()

                    if bmi < 18.5:
                       self.ErrorBox_lbl.setText("Underweight")
                    elif bmi >= 18.5 and bmi < 24.9:
                       self.ErrorBox_lbl.setText("Normal weight")
                    elif bmi >= 24.9 and bmi < 29.9:
                       self.ErrorBox_lbl.setText("Overweight")
                    else:
                       self.ErrorBox_lbl.setText("Obese")

                    cur.close()
                    db_conn.close()

                else:
                    self.ErrorBox_lbl.setText("Height and weight must be positive numbers.")
            except ValueError:
                self.ErrorBox_lbl.setText("Please enter valid numeric values for height and weight.")
        else:
            self.ErrorBox_lbl.setText("Please enter both height and weight.")

    def submitResults(self):
        bmi_result = self.BmiResult_lnedit.text()
        if bmi_result:
            self.ErrorBox_lbl.setText(f"Submitted BMI Result: {bmi_result}")
        else:
            self.ErrorBox_lbl.setText("No BMI result to submit.")

    def clearFields(self):
        self.Height_lnedit.clear()
        self.Weight_lnedit.clear()
        self.BmiResult_lnedit.clear()
        self.ErrorBox_lbl.clear()

    def back(self):
        self.Height_lnedit.clear()
        self.Weight_lnedit.clear()
        self.BmiResult_lnedit.clear()
        self.ErrorBox_lbl.clear()
        self.Back_Pushbutton.setVisible(True)

    def retranslateUi(self, MainWin):
        _translate = QtCore.QCoreApplication.translate
        MainWin.setWindowTitle(_translate("MainWin", "MainWindow"))
        self.Bmi_lbl.setText(_translate("MainWin", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">UNIT CONVERTER</span></p></body></html>"))
        self.Welcome_lbl.setText(_translate("MainWin", 'Welcome BigBaby'"<html><head/><body><p><br/></p><p><span style=\" font-weight:600;\"><br/></span></p></body></html>"))
        self.Greeting_lbl.setText(_translate("MainWin", "<html><head/><body><p><br/></p></body></html>"))
        self.Time_lbl.setText(_translate("MainWin", "<html><head/><body><p><br/></p></body></html>"))
        self.Height_lbl.setText(_translate("MainWin", "<html><head/><body><p><span style=\" font-size:12pt;\">HEIGHT</span></p></body></html>"))
        self.Weight_lbl.setText(_translate("MainWin", "<html><head/><body><p><span style=\" font-size:12pt;\">WEIGHT</span></p></body></html>"))
        self.BmiResult_lbl.setText(_translate("MainWin", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">BMI RESULT</span></p></body></html>"))
        self.Kg_lbl.setText(_translate("MainWin", "<html><head/><body><p><span style=\" font-size:10pt;\">Kg</span></p></body></html>"))
        self.Cm_lbl.setText(_translate("MainWin", "<html><head/><body><p><span style=\" font-size:10pt;\">Cm</span></p></body></html>"))
        self.Calculate_PushBtn.setText(_translate("MainWin", "CALCULATE BMI"))
        self.Submit_PushBtn.setText(_translate("MainWin", "SUBMIT"))
        self.Clear_Pushbutton.setText(_translate("MainWin", "CLEAR"))
        self.Back_Pushbutton.setText(_translate("MainWin", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWin = QtWidgets.QMainWindow()
    ui = Ui_MainWin()
    ui.setupUi(MainWin)
    MainWin.show()
    sys.exit(app.exec())
