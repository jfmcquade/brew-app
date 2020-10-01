import etl_task.extract as e
import etl_task.transform as t
import etl_task.load as l

people = []

e.load_from_csv("./etl_task/Import_User_Sample_en.csv", people)

people_formatted = t.format_names(people)

l.load_people_list_to_db(people_formatted)