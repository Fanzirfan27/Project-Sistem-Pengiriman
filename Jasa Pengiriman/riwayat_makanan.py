from PyQt5 import QtCore, QtGui, QtWidgets
from pengiriman_makanan import PengirimanMakanan as PM

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Label Judul
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(465, 30, 350, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        # Tombol Kembali
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 20, 100, 23))
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4 {\n"
                                       "    background-color: #1E90FF;\n"
                                       "    color: white;\n"
                                       "    font-size: 14px;\n"
                                       "    border-radius: 5px;\n"
                                       "}\n"
                                       "QPushButton#pushButton_4:hover {\n"
                                       "    background-color: #4682B4;\n"
                                       "}")
        self.pushButton_4.setObjectName("pushButton_4")

        # Tabel Log
        self.table_widget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_widget.setGeometry(QtCore.QRect(20, 70, 1240, 580))
        self.table_widget.setColumnCount(13)
        self.table_widget.setHorizontalHeaderLabels([
            "ID", "Nama Pengirim", "Alamat Pengirim", "Nama Penerima",
            "Alamat Penerima", "Nama Makanan", "Jumlah Makanan",
            "Tanggal Pengiriman", "Tanggal Penerimaan", "Status", "Harga",
            "Voucher", "Status Pembayaran"
        ])
        self.table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.setStyleSheet("""
            QTableWidget {
                background-color: #F0F8FF;
                alternate-background-color: #E6F7FF;
                gridline-color: #B0C4DE;
                font-size: 14px;
            }
            QHeaderView::section {
                background-color: #1E90FF;
                color: white;
                font-weight: bold;
                font-size: 15px;
            }
        """)
        self.table_widget.setObjectName("table_widget")


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Tambahkan aksi tombol
        self.pushButton_4.clicked.connect(self.openhomeadmin)
        self.load_data_to_table_view_makanan()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Log Riwayat Pengiriman Makanan"))
        self.label_7.setText(_translate("MainWindow", "Log Riwayat Pengiriman Makanan"))
        self.pushButton_4.setText(_translate("MainWindow", "Kembali"))
        

    def openhomeadmin(self):
        import home_admin as ha
        self.window = QtWidgets.QMainWindow()
        self.ui = ha.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        QtWidgets.QWidget.close(QtWidgets.QApplication.activeWindow())
    
    def load_data_to_table_view_makanan(self):
        self.table_widget.setRowCount(0)
        data = PM.load_all_data()
        for row_number, row_data in enumerate(data):
            self.table_widget.insertRow(row_number)
            for column_number, data_item in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data_item))
                self.table_widget.setItem(row_number, column_number, item)
                 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
