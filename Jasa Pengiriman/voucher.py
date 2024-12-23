import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_sistempengiriman"
)

mycursor = mydb.cursor()

class Voucher:
    def __init__(self):
        pass
    
    def select_data():
        sql = "SELECT kode_voucher FROM voucher"
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

    def get_diskon_voucher(kode_voucher):
        query = "SELECT diskon_persen FROM voucher WHERE kode_voucher = %s"
        mycursor.execute(query, (kode_voucher,))
        result = mycursor.fetchone()

        if result:
            return result[0]  # Mengembalikan nilai diskon_persen
        else:
            return 0 
    
   
    def load_all_data():
        sql = "SELECT * FROM voucher"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(myresult)
        return myresult
    
   
    def select_data_by_id(id):
        sql = "SELECT * FROM voucher WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        print(myresult)
        return myresult

    def insert_data(kode_voucher, diskon_persen):
        sql = "INSERT INTO voucher (kode_voucher, diskon_persen) VALUES (%s, %s)" 
        val = (kode_voucher, diskon_persen)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil ditambahkan.")
        return mycursor.rowcount

    def update_data(id,kode_voucher, diskon_persen):
        sql = "UPDATE voucher  SET kode_voucher = %s, diskon_persen = %s WHERE id = %s"
        val = (kode_voucher, diskon_persen, id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil diupdate.")
        return mycursor.rowcount

    def delete_data(id):
        sql = "DELETE FROM voucher WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        return mycursor.rowcount