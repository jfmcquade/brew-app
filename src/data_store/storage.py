import csv
import pymysql
from src.models.person_class import Person

def wait():
    input("\nPress ENTER to return to the menu.")

def get_connection():
  return pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "BrewApp")

class File_Handling:
    def __init__(self, name):
        self.name = name

    def load_people_from_db(self, people):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM People")
        connection.commit()
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        for row in rows:
            person = Person(row[0], row[1], row[2])
            people.append(person)
        return people

    def list_from_file(self, filepath, list_name):
        file_var = open(filepath, "r")
        file_list = file_var.readlines()
        try:
            file_list = [item.strip() for item in file_list]
            for item in file_list:
                list_name.append(item)
            file_var.close()
            return list_name
        except FileNotFoundError as fnfe:
            print("Unable to open file:" + str(fnfe))
            return list_name
        except:
            print("An error occurred")
            wait()
        finally:
            file_var.close()

    def dict_from_csv(self, filepath, dict_name):
        try:
            with open(filepath, "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    dict_name[row[0]] = row[1]
                return dict_name
        except FileNotFoundError as fnfe:
            print("Unable to open file:" + str(fnfe))
            return dict_name
        except:
            print("An error occurred")
            wait()

    def load_people_from_csv(self, filepath, people):
        try:
            with open(filepath, "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    person = Person(row[0], row[1])
                    people.append(person)
                return people
        except FileNotFoundError as fnfe:
            print("Unable to open file:" + str(fnfe))
            return people
        except:
            print("An error occurred")
            wait()

    def save_dict_to_csv(self, filepath, dict_name):
        try:
            with open(filepath, "w") as csv_file:
                csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                for key, value in dict_name.items():
                    csv_writer.writerow([key, value])
        except:
            print(f"An error occurred when trying to save to {filepath}.")
            wait()
        
    def save_list_to_file(self, filepath, list_name):
        file_var = open(filepath, "w")
        try:
            for item in list_name:
                file_var.write(item + "\n")
        except:
            print(f"Unable to write to {filepath}.")
        finally:
            file_var.close()

    def save_list_of_person_instances_to_csv(self, filepath, list_of_instances): # , instance_variable1, instance_variable2?
        try:
            with open(filepath, "w") as csv_file:
                csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                for i in range(len(list_of_instances)):
                    instance = list_of_instances[i]
                    csv_writer.writerow([instance.name, instance.preference])
        except: 
            print(f"An error occurred when trying to save to {filepath}.")
            wait()

    def save_drinks_list_to_db(self, drinks):
        connection = get_connection()
        cursor = connection.cursor()
        for drink in drinks:
            cursor.execute(f'''INSERT INTO Drinks (drink_name) VALUES ("{drink}") ON DUPLICATE KEY UPDATE drink_name="{drink}"''')
        connection.commit()
        cursor.close()
        connection.close()

    def save_people_list_to_db(self, people, deleted_people):
        connection = get_connection()
        cursor = connection.cursor()
        for person in people:
            person_list_of_attributes = [person.person_id, person.name, person.preference]
            cursor.execute(f'''INSERT INTO People (person_id, name, preference) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE name="{person.name}"''', person_list_of_attributes)
        for person in deleted_people:
            person_list_of_attributes = [person.person_id, person.name, person.preference]
            cursor.execute(f'''DELETE FROM People WHERE person_id={person.person_id} AND name="{person.name}"''')
        connection.commit()
        cursor.close()
        connection.close()




    # def load_drinks_from_db(self, people):
    #     connection = get_connection()
    #     cursor = connection.cursor()
    #     cursor.execute("SELECT drinkID FROM Drinks")
    #     connection.commit()
    #     rows = cursor.fetchall()
    #     cursor.close()
    #     connection.close()
        
    #     for row in rows:
    #         print(row)

    #     return



# test_list = [Person("Johnny", "tea"), Person("Ross", "squash")]

# class_list_saver = File_Handling("class_list_saver")
# class_list_saver.save_list_of_person_instances_to_csv("./data/test.csv", test_list)