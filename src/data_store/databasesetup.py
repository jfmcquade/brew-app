import pymysql

def add_drink_to_mysql():
    connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "BrewApp")
    cursor = connection.cursor()
    args = ("tea")
    cursor.execute("INSERT INTO Drinks (drink_name) VALUES (%s)", args)
    connection.commit()

    cursor.close()
    connection.close()

add_drink_to_mysql()