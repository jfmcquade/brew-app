import pymysql

def load_people_list_to_db(people_formatted):
        connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "BrewApp")
        cursor = connection.cursor()
        for person in people_formatted:
            cursor.execute("INSERT INTO people_task (fname, lname) VALUES (%s, %s)", person)
        connection.commit()
        cursor.close()
        connection.close()