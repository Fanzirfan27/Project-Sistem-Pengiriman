# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detail_barang.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(185, 20, 130, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 590, 100, 23))
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 110, 100, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_bag = QtWidgets.QLabel(self.centralwidget)
        self.label_bag.setGeometry(QtCore.QRect(-590, -10, 1091, 700))
        self.label_bag.setStyleSheet("background-image: url(:/newPrefix/pengiriman-barang-satu-hari-sampai.jpg);")
        self.label_bag.setText("")
        self.label_bag.setObjectName("label_bag")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 70, 100, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(290, 150, 100, 20))
        self.label_17.setStyleSheet("QLabel#label_17 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(290, 190, 100, 20))
        self.label_18.setStyleSheet("QLabel#label_18 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 150, 100, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 190, 100, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 230, 100, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 270, 100, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(120, 310, 100, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(120, 350, 100, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(120, 390, 100, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 430, 100, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(120, 470, 100, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(120, 510, 100, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(120, 550, 115, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(290, 70, 100, 20))
        self.label_15.setStyleSheet("QLabel#label_15 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(290, 110, 100, 20))
        self.label_16.setStyleSheet("QLabel#label_16 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(290, 230, 100, 20))
        self.label_19.setStyleSheet("QLabel#label_19 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(290, 270, 100, 20))
        self.label_20.setStyleSheet("QLabel#label_20 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(290, 310, 100, 20))
        self.label_21.setStyleSheet("QLabel#label_21 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(290, 350, 100, 20))
        self.label_22.setStyleSheet("QLabel#label_22 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(290, 390, 100, 20))
        self.label_23.setStyleSheet("QLabel#label_23 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(290, 430, 100, 20))
        self.label_24.setStyleSheet("QLabel#label_24 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(290, 470, 100, 20))
        self.label_25.setStyleSheet("QLabel#label_25 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(290, 510, 100, 20))
        self.label_26.setStyleSheet("QLabel#label_26 {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(290, 550, 100, 20))
        self.label_27.setStyleSheet("QLabel#label_27\n"
" {\n"
"    border: 1px solid black; /* Border hitam dengan ketebalan 2px */\n"
"}")
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.label_bag.raise_()
        self.label_7.raise_()
        self.pushButton_4.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton_4.clicked.connect(self.openhomepelanggan)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Detail Barang"))
        self.pushButton_4.setText(_translate("MainWindow", "Kembali"))
        self.label_2.setText(_translate("MainWindow", "Alamat Pengirim"))
        self.label.setText(_translate("MainWindow", "Nama Pengirim"))
        self.label_3.setText(_translate("MainWindow", "Nama Penerima"))
        self.label_4.setText(_translate("MainWindow", "Alamat Penerima"))
        self.label_5.setText(_translate("MainWindow", "Nama Barang"))
        self.label_6.setText(_translate("MainWindow", "Berat Barang"))
        self.label_8.setText(_translate("MainWindow", "Jumlah Barang"))
        self.label_9.setText(_translate("MainWindow", "Tgl Pengiriman"))
        self.label_10.setText(_translate("MainWindow", "Tgl Penerimaan"))
        self.label_11.setText(_translate("MainWindow", "Status"))
        self.label_12.setText(_translate("MainWindow", "Total Harga"))
        self.label_13.setText(_translate("MainWindow", "Voucher"))
        self.label_14.setText(_translate("MainWindow", "Status Pembayaran"))
    def openhomepelanggan(self):
        import home_pelanggan as hp
        self.window = QtWidgets.QMainWindow()
        self.ui = hp.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        QtWidgets.QWidget.close(QtWidgets.QApplication.activeWindow())
import image


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
