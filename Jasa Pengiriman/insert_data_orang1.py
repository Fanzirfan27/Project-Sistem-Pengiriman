# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insert_data_orang.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from alamat import Alamat
from pengiriman_orang import PengirimanOrang as PO
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(135, 30, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(240, 140, 120, 20))
        self.comboBox.setStyleSheet("QComboBox#comboBox {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 220, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 180, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 100, 120, 20))
        self.lineEdit.setStyleSheet("QLineEdit#lineEdit {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(240, 180, 120, 22))
        self.comboBox_2.setStyleSheet("QComboBox#comboBox_2 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 140, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 100, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(240, 220, 120, 22))
        self.comboBox_3.setStyleSheet("QComboBox#comboBox_3 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 260, 100, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 260, 100, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 651, 651))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix/2920421574.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label_7.raise_()
        self.comboBox.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.comboBox_2.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.comboBox_3.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.getDataAlamat()
        self.pushButton.clicked.connect(self.simpan_data)
        self.pushButton_3.clicked.connect(self.openhomepelanggan)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Insert Data Orang"))
        self.label_5.setText(_translate("MainWindow", "Kategori"))
        self.label_4.setText(_translate("MainWindow", "Alamat Tujuan"))
        self.label_2.setText(_translate("MainWindow", "Alamat Pemesanan"))
        self.label.setText(_translate("MainWindow", "Nama Pemesanan"))
        self.pushButton.setText(_translate("MainWindow", "Simpan"))
        self.pushButton_3.setText(_translate("MainWindow", "Kembali"))

    def openhomepelanggan(self):        
        import home_pelanggan as hp
        self.window = QtWidgets.QMainWindow()
        self.ui = hp.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        QtWidgets.QWidget.close(QtWidgets.QApplication.activeWindow())
    def getDataAlamat(self):
        data = Alamat.select_data()
        self.comboBox.addItems(data)
        self.comboBox_2.addItems(data)
        kategori_items = ["Bike", "Car"]
        self.comboBox_3.addItems(kategori_items)
    def simpan_data(self):
        nama_pemesanan = self.lineEdit.text()
        alamat_pemesanan = self.comboBox.currentText()  
        alamat_tujuan = self.comboBox_2.currentText()  
        kategori = self.comboBox_3.currentText()
        rows_inserted = PO.insert_data(nama_pemesanan, alamat_pemesanan, alamat_tujuan, kategori)
        if rows_inserted is not None and rows_inserted > 0:
                QtWidgets.QMessageBox.information(None, "Berhasil", "Data berhasil disimpan.")
                self.lineEdit.clear()
                self.comboBox_3.setCurrentIndex(0)
                self.comboBox_2.setCurrentIndex(0)
                self.comboBox.setCurrentIndex(0)
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
