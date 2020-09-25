import csv
def wait():
    input("\nPress ENTER to return to the menu.")

# Make lists and dictionaries from files
def list_from_file(filepath, list_name):
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


def dict_from_csv(filepath, dict_name):
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


# Save data to files
def save_dict_to_csv(filepath, dict_name):
    try:
        with open(filepath, "w") as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for key, value in dict_name.items():
                csv_writer.writerow([key, value])
    except:
        print(f"An error occurred when trying to save to {filepath}.")
        wait()

def save_list_to_file(filepath, list_name):
    file_var = open(filepath, "w")
    # with open(filepath, "w") as file_var:
    try:
        for item in list_name:
            file_var.write(item + "\n") # writelines?
    except:
        print(f"Unable to write to {filepath}.")
    finally:
        file_var.close()