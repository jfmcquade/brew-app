import csv

def load_from_csv(filepath, people):
    with open(filepath, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                full_name = row[1]
                people.append(full_name)
                line_count += 1
        return people