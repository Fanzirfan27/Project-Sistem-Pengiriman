import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_sistempengiriman"
)

mycursor = mydb.cursor()

class PengirimanMakanan:
    def __init__(self):
        pass

    @staticmethod
    def load_all_data():
        sql = "SELECT * FROM makanan_pengiriman"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(myresult)
        return myresult

    @staticmethod
    def select_data_by_id(id):
        sql = "SELECT * FROM makanan_pengiriman WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        print(myresult)
        return myresult

    @staticmethod
    def insert_data(nama_pengirim, alamat_pengirim, nama_penerima, alamat_penerima, nama_makanan, jumlah_makanan):
        sql = """INSERT INTO makanan_pengiriman
                 (nama_pengirim, alamat_pengirim, nama_penerima, alamat_penerima, nama_makanan, jumlah_makanan) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        val = (nama_pengirim, alamat_pengirim, nama_penerima, alamat_penerima, nama_makanan, jumlah_makanan)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil ditambahkan.")
        return mycursor.rowcount

    @staticmethod
    def update_data(id, nama_pengirim, alamat_pengirim, nama_penerima, alamat_penerima, nama_makanan, jumlah_makanan):
        sql = """UPDATE makanan_pengiriman
                 SET nama_pengirim = %s, alamat_pengirim = %s, nama_penerima = %s, alamat_penerima = %s, 
                     nama_makanan = %s, jumlah_makanan = %s
                 WHERE id = %s"""
        val = (nama_pengirim, alamat_pengirim, nama_penerima, alamat_penerima, nama_makanan, jumlah_makanan, id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil diupdate.")
        return mycursor.rowcount

    @staticmethod
    def delete_data(id):
        sql = "DELETE FROM makanan_pengiriman WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        return mycursor.rowcount
    
    @staticmethod
    def select_data_by_id_pembayaran(id):
        sql = "SELECT id, nama_pengirim, alamat_pengirim, nama_penerima,alamat_penerima, nama_makanan, voucher, harga, jumlah_makanan, status_pembayaran FROM makanan_pengiriman WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        print(myresult)
        return myresult
    @staticmethod
    def bayar_pengiriman_makanan(id, harga, voucher):
        sql ="UPDATE makanan_pengiriman SET harga = %s, voucher = %s, status_pembayaran = 'Sudah Dibayar' WHERE id = %s"
        val = (harga, voucher,id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil dibayar")
        return mycursor.rowcount
    @staticmethod
    def detail_pengiriman_makanan(id):
        sql = "SELECT * FROM makanan_pengiriman WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        print(myresult)
        return myresult
    @staticmethod
    def update_detail_pengiriman_makanan(id, nama_pengirim, alamat_pengirim, nama_penerima, alamat_penerima, nama_makanan, jumlah_makanan,tgl_pengiriman, tgl_penerimaan, status, harga, voucher, status_pembayaran):
        sql = """UPDATE makanan_pengiriman 
                 SET nama_pengirim = %s, alamat_pengirim = %s, nama_penerima = %s, alamat_penerima = %s, 
                     nama_makanan = %s, jumlah_makanan = %s,tanggal_pengiriman = %s, tanggal_penerimaan = %s, status = %s, harga = %s, voucher = %s, status_pembayaran = %s
                 WHERE id = %s"""
        val = (nama_pengirim, alamat_pengirim, nama_penerima, alamat_penerima, nama_makanan,  jumlah_makanan, tgl_pengiriman, tgl_penerimaan, status, harga, voucher, status_pembayaran, id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil diupdate.")
        return mycursor.rowcount