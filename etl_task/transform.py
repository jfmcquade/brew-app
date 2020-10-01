def format_names(people):
    people_both_names = []
    for full_name in people:
        both_names = full_name.title().split(" ")
        people_both_names.append(both_names)
    return people_both_names
