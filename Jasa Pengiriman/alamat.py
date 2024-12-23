import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_sistempengiriman"
)

mycursor = mydb.cursor()

class Alamat:
    
    def __init__(self):
        self

    def select_data():
        sql = "SELECT nama_alamat FROM alamat"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        data = []
        for x in myresult:
            data.append(
                str(x).replace("(", "")
                       .replace("'", "")
                       .replace(",", "")
                       .replace(")", "")
            )
            print(x)
        return data
    def get_koordinat_dari_db(nama_alamat):
          # Query untuk mendapatkan koordinat
        query = "SELECT latitude, longitude FROM alamat WHERE nama_alamat = %s"
        mycursor.execute(query, (nama_alamat,))
        result = mycursor.fetchone()

        if result:
            return result[0], result[1] 
        else:
            raise ValueError(f"Alamat '{nama_alamat}' tidak ditemukan dalam database.")

    def load_all_data():
        sql = "SELECT * FROM alamat"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(myresult)
        return myresult
    def select_data_by_id(id):
        sql = "SELECT * FROM alamat WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        print(myresult)
        return myresult

    def insert_data(nama_alamat, latitude, longitude):
        sql = "INSERT INTO alamat (nama_alamat, latitude, longitude) VALUES (%s,%s, %s)" 
        val = (nama_alamat, latitude, longitude)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil ditambahkan.")
        return mycursor.rowcount

    def update_data(id,nama_alamat, latitude, longitude):
        sql = "UPDATE alamat  SET nama_alamat = %s, latitude = %s, longitude = %s WHERE id = %s"
        val = (nama_alamat, latitude, longitude, id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil diupdate.")
        return mycursor.rowcount

    def delete_data(id):
        sql = "DELETE FROM alamat WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        return mycursor.rowcount
# Contoh pemanggilan
alamat = Alamat()
alamat_data = Alamat.select_data()

