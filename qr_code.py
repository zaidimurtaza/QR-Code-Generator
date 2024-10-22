import mysql.connector as msql
import qrcode as qr
import os

connection = msql.connect(
    host='localhost',
    user='release_user',
    password='release_password',
    database='data'
)

my_cursor = connection.cursor()

my_cursor.execute("CREATE table IF NOT exists IMAGES(id int NOT Null AUTO_INCREMENT PRIMARY KEY,Photo BLOB NOT NULL)")
print("Enter 1 for uploading\nEnter 2 for saving back")
def upload(input):
    code = qr.make(input)
    path = os.path.join(r"F:\Murtaza\Python-Projects\QR-code\qr-codes",f"{input}.png" )
    code.save(path)
    with open(path , "rb") as f:
        img_binary_data = f.read()
        sql_statement = "INSERT INTO IMAGES( Photo) values(%s)"
        my_cursor.execute(sql_statement, (img_binary_data, ))
    connection.commit()
def retreve(ID):
    my_cursor.execute(f"SELECT * from IMAGES Where id = {ID} ")
    data = my_cursor.fetchone()[1]
    store_file_path = r"F:\Murtaza\Python-Projects\QR-code\image_folder\{0}.png".format(str(ID))
    with open(store_file_path, "wb") as file:
            file.write(data)
            file.close()
respond = input()
if int(respond) == 1:
    
    upload(input("Enter file : "))
elif int(respond) == 2:
    
    retreve(input("Enter ID : "))

