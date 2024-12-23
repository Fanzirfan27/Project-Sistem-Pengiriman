# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registrasi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pelanggan import Pelanggan
import home_pelanggan as hp
import home_admin as ha

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 550)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 20, 390, 500))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 20, 310, 460))
        self.label.setStyleSheet("border-image: url(:/images/drops-5451924_1280.jpg);\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 310, 460))
        self.label_2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50),stop:0.835227 rgba(0,0,0,75));\n"
"border-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(55, 40, 280, 420))
        self.label_3.setStyleSheet("background-color:rgba(0,0,0,100);\n"
"border-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(128, 80, 135, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgba(255,255,255,210);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(95, 135, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
"border: none;\n"
"border-bottom: 2px solid rgba(255, 255, 255, 0.7);\n"
"color: rgba(255, 255, 255, 0.9); \n"
"padding-bottom: 7px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(95, 190, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
"border: none;\n"
"border-bottom: 2px solid rgba(255, 255, 255, 0.7);\n"
"color: rgba(255, 255, 255, 0.9); \n"
"padding-bottom: 7px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(95, 370, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, \n"
"        stop:0 rgba(78, 47, 20, 219), stop:1 rgba(100, 60, 30, 226)); /* Cokelat gelap */\n"
"    color: rgba(255, 255, 255, 210); /* Warna teks putih */\n"
"    border-radius: 5px; /* Sudut melengkung */\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, \n"
"        stop:0 rgba(100, 60, 30, 219), stop:1 rgba(120, 70, 40, 226)); /* Cokelat sedikit lebih terang */\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(60, 40, 20, 200); /* Cokelat sangat gelap (hampir hitam) */\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(95, 250, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
"border: none;\n"
"border-bottom: 2px solid rgba(255, 255, 255, 0.7);\n"
"color: rgba(255, 255, 255, 0.9); \n"
"padding-bottom: 7px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(95, 305, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
"border: none;\n"
"border-bottom: 2px solid rgba(255, 255, 255, 0.7);\n"
"color: rgba(255, 255, 255, 0.9); \n"
"padding-bottom: 7px;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 45, 35, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, \n"
"        stop:0 rgba(78, 47, 20, 219), stop:1 rgba(100, 60, 30, 226)); /* Cokelat gelap */\n"
"    color: rgba(255, 255, 255, 210); /* Warna teks putih */\n"
"    border-radius: 5px; /* Sudut melengkung */\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, \n"
"        stop:0 rgba(100, 60, 30, 219), stop:1 rgba(120, 70, 40, 226)); /* Cokelat sedikit lebih terang */\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(60, 40, 20, 200); /* Cokelat sangat gelap (hampir hitam) */\n"
"}\n"
"\n"
"QPushButton#pushButton_2 {\n"
"    background-color: transparent; /* Transparan sepenuhnya */\n"
"    color: rgba(255, 255, 255, 0.7); /* Teks putih keabu-abuan */\n"
"    border: none; /* Tidak ada garis tepi */\n"
"    transition: color 0.3s ease, text-shadow 0.3s ease; /* Animasi halus */\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover {\n"
"    color: rgba(255, 255, 255, 1); /* Teks menjadi putih solid saat hover */\n"
"    text-shadow: 0 0 5px rgba(255, 255, 255, 0.8); /* Efek bayangan cahaya pada teks */\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.register_user)
        self.pushButton_2.clicked.connect(self.openWelcomePage)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Registrasi"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "R e g i s t e r"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Konfirmasi Password"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Level"))
        self.pushButton_2.setText(_translate("Form", "X"))
        
    def register_user(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        confirm_password = self.lineEdit_3.text()
        level = self.lineEdit_4.text().lower()
        # Validasi input
        if not username or not password or not confirm_password or not level:
            QMessageBox.warning(None, "Warning", "Semua field harus diisi!")
            return
        if password != confirm_password:
            QMessageBox.warning(None, "Warning", "Password tidak cocok!")
            return
        if level not in ["admin", "pelanggan"]:
            QMessageBox.warning(None, "Warning", "Level harus 'admin' atau 'pelanggan'!")
            return
        if level == "admin":
            QMessageBox.information(None, "Login Sukses", "Selamat datang, Admin!")
            self.openDashboardAdmin()
        elif level == "pelanggan":
            QMessageBox.information(None, "Login Sukses", "Selamat datang, Pelanggan!")
            self.openDashboardPelanggan()
        Pelanggan.register_pelanggan(username,password,level)
        
    def openDashboardAdmin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ha.Ui_MainWindow()
        self.ui.setupUi(self.window) 
        self.window.show()
        QtWidgets.QWidget.close(QtWidgets.QApplication.activeWindow())

    def openDashboardPelanggan(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = hp.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        QtWidgets.QWidget.close(QtWidgets.QApplication.activeWindow())
        
    def openWelcomePage(self):
        import welcome as hw
        self.window = QtWidgets.QMainWindow()
        self.ui = hw.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        QtWidgets.QWidget.close(QtWidgets.QApplication.activeWindow())
        
import res


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
