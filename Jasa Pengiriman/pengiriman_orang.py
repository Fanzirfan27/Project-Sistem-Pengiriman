import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_sistempengiriman"
)

mycursor = mydb.cursor()

class PengirimanOrang:
    def __init__(self):
        pass

    @staticmethod
    def load_all_data():
        sql = "SELECT * FROM orang_pengiriman"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(myresult)
        return myresult

    @staticmethod
    def select_data_by_id(id):
        sql = "SELECT * FROM orang_pengiriman WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        print(myresult)
        return myresult

    @staticmethod
    def insert_data(nama_pemesanan, alamat_pemesanan, alamat_tujuan, kategori):
        sql = """INSERT INTO orang_pengiriman
                 (nama_pemesanan, alamat_pemesanan, alamat_tujuan, kategori) 
                 VALUES (%s, %s, %s, %s)"""
        val = (nama_pemesanan, alamat_pemesanan, alamat_tujuan, kategori)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil ditambahkan.")
        return mycursor.rowcount

    @staticmethod
    def update_data(id, nama_pemesanan, alamat_pemesanan, alamat_tujuan, kategori):
        sql = """UPDATE orang_pengiriman
                 SET nama_pemesanan = %s, alamat_pemesanan = %s, alamat_tujuan = %s, kategori = %s
                 WHERE id = %s"""
        val = (nama_pemesanan, alamat_pemesanan, alamat_tujuan, kategori, id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil diupdate.")
        return mycursor.rowcount

    @staticmethod
    def delete_data(id):
        sql = "DELETE FROM orang_pengiriman WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil dihapus.")
        return mycursor.rowcount
    @staticmethod
    def select_data_by_id_pembayaran(id):
        sql = "SELECT id, nama_pemesanan, alamat_pemesanan, alamat_tujuan, kategori, harga, voucher,status_pembayaran FROM orang_pengiriman WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        print(myresult)
        return myresult
    @staticmethod
    def bayar_pengiriman_orang(id, harga, voucher):
        sql ="UPDATE orang_pengiriman SET harga = %s, voucher = %s, status_pembayaran = 'Sudah Dibayar' WHERE id = %s"
        val = (harga, voucher,id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil dibayar.")
        return mycursor.rowcount
    @staticmethod
    def detail_pengiriman_orang(id):
        sql = "SELECT * FROM orang_pengiriman WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        print(myresult)
        return myresult
    @staticmethod
    def update_detail_pengiriman_orang(id, nama_pemesan, alamat_pemesan, alamat_tujuan, kategori, status, harga, voucher, status_pembayaran):
        sql = """UPDATE orang_pengiriman 
                 SET nama_pemesanan = %s, alamat_pemesanan = %s, alamat_tujuan = %s, kategori = %s, 
                     status = %s, harga = %s, voucher = %s, status_pembayaran = %s
                 WHERE id = %s"""
        val = ( nama_pemesan, alamat_pemesan, alamat_tujuan, kategori,status, harga, voucher, status_pembayaran, id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil diupdate.")
        return mycursor.rowcount
        