import mysql.connector

# Koneksi ke database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_sistempengiriman"
)
mycursor = mydb.cursor()
class Pelanggan:
    def __init__(self):
        pass
    def register_pelanggan(username, password, level):
        sql = "INSERT INTO users (username, password, level) VALUES (%s, %s, %s)"
        val = (username, password, level)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data Berhasil ditambahkannn.....")
    
    def login_pelanggan(username, password):
        """Verifikasi login berdasarkan username dan password."""
        sql = "SELECT level FROM users WHERE username = %s AND password = %s"
        val = (username, password)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if result:
            return result[0]  # Mengembalikan level (Admin/Kasir)
        else:
            return None