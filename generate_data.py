import random
import csv

first_names = []
last_names = []
addresses = []
post_fix_adr = ["Ave", "Rd", "Dr", "Way", "St"]
gender = ["M", "F"]
email_postfix = "@example.com"


def random_phone():
    return random.randint(1000000000, 9999999999)


with open("names/first-names.txt", "r") as file:
    line = file.readline()
    while True:
        if line == "":
            break
        else:
            first_names.append(line.strip("\n"))
            line = file.readline()

with open("names/last-names.txt", "r") as file:
    line = file.readline()
    while True:
        if line == "":
            break
        else:
            last_names.append(line.strip("\n"))
            line = file.readline()

with open("names/places.txt", "r") as file:
    line = file.readline()
    while True:
        if line == "":
            break
        else:
            num = random.randint(100, 999)
            line = line.strip("\n")
            addresses.append(f"{num} {line} {random.choice(post_fix_adr)}")
            line = file.readline()


def first_name():
    return random.choice(first_names)


def last_name():
    return random.choice(last_names)


def addr():
    return random.choice(addresses)


def gen_email(fn, ln):
    return f"{fn}{ln}{email_postfix}"


def enr_year():
    return random.randint(2015, 2023)


def gpa():
    return round(random.uniform(1.5, 4.0), 1)


def tuition():
    return round(random.uniform(5000.0, 150000.0), 1)


def salary():
    return round(random.uniform(10000, 100000), 1)


def generate_data():
    """
    This method generate this university_person.csv, student.csv, and faculty.csv
    """
    uni_id = 100
    stu_id = 1000
    fa_id = 2000
    # Write university person data
    with open("data/university_person.csv", "w", newline='') as u_file:
        with open("data/student.csv", "w", newline='') as s_file:
            with open("data/faculty.csv", "w", newline='') as f_file:
                uni_writer = csv.writer(u_file)
                student_writer = csv.writer(s_file)
                faculty_writer = csv.writer(f_file)
                attr = ["uni_id", "first_name", "last_name", "phone_number", "email", "addr", "gender"]
                uni_writer.writerow(attr)
                attr = ["uni_id", "stu_id", "gpa", "tuition", "enr_yr"]
                student_writer.writerow(attr)
                attr = ["uni_id", "fa_id", "salary"]
                faculty_writer.writerow(attr)

                for i in range(1, 51):
                    first = first_name()
                    last = last_name()
                    email = gen_email(first, last)
                    row = [uni_id, first, last, random_phone(), email, addr(), random.choice(gender)]
                    uni_writer.writerow(row)
                    # Writing student data
                    if i <= 25:
                        row = [uni_id, stu_id, gpa(), tuition(), enr_year()]
                        student_writer.writerow(row)
                        stu_id += 1
                    # Writing faculty data
                    else:
                        row = [uni_id, fa_id, salary()]
                        faculty_writer.writerow(row)
                        fa_id += 1
                    uni_id += 1



def generate_professor():
    """"This function generate the professor.csv based on faculty.csv"""
    prof_id = 3000
    with open("data/faculty.csv", "r", newline='') as f_file:
        reader = csv.reader(f_file, delimiter=',')
        i = 1
        with open("data/professor.csv", "w", newline='') as p_file:
            prof_writer = csv.writer(p_file)
            attr = ["uni_id", "fa_id", "prof_id"]
            prof_writer.writerow(attr)
            for row in reader:
                if row[0] != "uni_id":
                    if i <= 15:
                        p_row = [row[0], row[1], prof_id]
                        prof_writer.writerow(p_row)
                        prof_id += 1
                        i += 1



# generate_data()
# generate_professor()
