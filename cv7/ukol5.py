def find_students(*args):    
    print("Pocet predmetu: {0}".format(len(args)))

    students_dict = {}

    subject_counter = 1
    for lst in args:
        for student in lst:
            if not student in students_dict:
                students_dict[student] = [subject_counter]
            else:
                students_dict[student].append(subject_counter)
        subject_counter += 1

    return students_dict

def number_of_subjects(students_dict, subjects_target):
    students_with_1_subject = []
    for student in students_dict:
        if len(students_dict.get(student)) == subjects_target:
            students_with_1_subject.append(student)
    return students_with_1_subject


lst1 = ["Svätopluk", "Pribina", "Rastislav", "Otakar", "Gejza"]
lst2 = ["Gejza", "Svetlana", "Milena"]
lst3 = ["Pribina", "Gejza", "Rastislav"]

print(number_of_subjects(find_students(lst1, lst2, lst3), 2))