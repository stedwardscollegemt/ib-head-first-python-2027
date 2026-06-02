FILEPATH = "data/students_file.txt"
student_records = []

def create_new_student(name, age, save_to_file = False):
    new_student_record = [name, age]
    student_records.append(new_student_record)
    if save_to_file == True:
        with open(FILEPATH, "a") as data_file:
            data_file.write(f"{name},{age}\n");
    return new_student_record

def read_all():
    try:
        with open(FILEPATH) as students_file:
            content = students_file.read()
            for line in content.split("\n"):
                if line != "":
                    name, age = line.split(",")
                    student_records.append([name, int(age)])
    except IOError:
        print("Error. We could not open the file.")
    return student_records

def update_student_record(name_old, age_old, name_new, age_new, save_to_file = False):
    for index in range(len(student_records)):
        student_record = student_records[index]
        if student_record[0] == name_old and student_record[1] == age_old:
            student_records[index][0] = name_new
            student_records[index][1] = age_new
    if save_to_file:
        update_to_file()

def update_to_file():
    with open(FILEPATH, "w") as data_file:
        for student_record in student_records:
            name, age = student_record[0], student_record[1]
            data_file.write(f"{name},{age}\n");

# TODO: delete a student record