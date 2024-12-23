# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insert_data_makanan.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pengiriman_makanan import PengirimanMakanan as PM
from alamat import Alamat



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 497)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 90, 85, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 90, 120, 21))
        self.lineEdit.setStyleSheet("QLineEdit#lineEdit {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 130, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 170, 120, 21))
        self.lineEdit_3.setStyleSheet("QLineEdit#lineEdit_3 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(220, 130, 120, 21))
        self.comboBox_3.setStyleSheet("QComboBox#comboBox_3 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 170, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 210, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 210, 120, 21))
        self.comboBox_2.setStyleSheet("QComboBox#comboBox_2 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(90, 250, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(220, 250, 120, 21))
        self.lineEdit_7.setStyleSheet("QLineEdit#lineEdit_7 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(125, 20, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 380, 100, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 380, 100, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-280, -30, 871, 691))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix/533-5338308_food-delivery-png-download-food-delivery-transparent-png.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(90, 290, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(220, 290, 120, 21))
        self.lineEdit_8.setStyleSheet("QLineEdit#lineEdit_8 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_3.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.lineEdit_3.raise_()
        self.comboBox_3.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.comboBox_2.raise_()
        self.label_9.raise_()
        self.lineEdit_7.raise_()
        self.label_10.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.label_11.raise_()
        self.lineEdit_8.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.getDataAlamat()
        #aksi button
        self.pushButton_3.clicked.connect(self.openhomepelanggan)
        self.pushButton.clicked.connect(self.simpan_data)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nama Pengirim"))
        self.label_2.setText(_translate("MainWindow", "Alamat Pengirim"))
        self.label_7.setText(_translate("MainWindow", "Nama Penerima"))
        self.label_8.setText(_translate("MainWindow", "Alamat Penerima"))
        self.label_9.setText(_translate("MainWindow", "Nama Makanan"))
        self.label_10.setText(_translate("MainWindow", "Insert Data Makanan"))
        self.pushButton.setText(_translate("MainWindow", "Simpan"))
        self.pushButton_3.setText(_translate("MainWindow", "Kembali"))
        self.label_11.setText(_translate("MainWindow", "Jumlah Makanan"))

        
    def openhomepelanggan(self):        
        import home_pelanggan as hp
        self.window = QtWidgets.QMainWindow()
        self.ui = hp.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        QtWidgets.QWidget.close(QtWidgets.QApplication.activeWindow())
    def getDataAlamat(self):
        data = Alamat.select_data()
        self.comboBox_3.addItems(data)
        self.comboBox_2.addItems(data)    
    def simpan_data(self):
        nama_pengirim = self.lineEdit.text()
        alamat_pengirim = self.comboBox_3.currentText()  
        nama_penerima = self.lineEdit_3.text()
        alamat_penerima = self.comboBox_2.currentText()  
        nama_makanan = self.lineEdit_7.text()
        jumlah_makanan = self.lineEdit_8.text()
        rows_inserted = PM.insert_data(nama_pengirim, alamat_pengirim, nama_penerima, alamat_penerima, nama_makanan, jumlah_makanan)
        if rows_inserted is not None and rows_inserted > 0:
                QtWidgets.QMessageBox.information(None, "Berhasil", "Data berhasil disimpan.")
                self.lineEdit.clear()
                self.lineEdit_3.clear()
                self.lineEdit_7.clear()
                self.comboBox_3.setCurrentIndex(0)
                self.comboBox_2.setCurrentIndex(0)
                self.lineEdit_8.clear()
        else:
                QtWidgets.QMessageBox.warning(None, "Gagal", "Data gagal disimpan.")


import image


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
