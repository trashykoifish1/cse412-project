from flask import Flask, render_template, request, redirect, url_for, jsonify
import psycopg2

DATABASE_NAME = "cse412-project"
DATABASE_HOST = "localhost"
USER = "khoi"
PASSWORD = "1234"
PORT = "5432"
students = []

app = Flask(__name__)

conn = psycopg2.connect(database=DATABASE_NAME,
                        host=DATABASE_HOST,
                        user=USER,
                        password=PASSWORD,
                        port=PORT)
cursor = conn.cursor()


### ID Generation
def gen_uni_id():
    cursor.execute("""
        SELECT MAX(uni_id)
        FROM university_person
    """)
    output = cursor.fetchone()
    print(output)
    # print(output[0] + 1)
    if output[0] is None:
        return 100
    else:
        return output[0] + 1


def gen_stu_id():
    cursor.execute("""
        SELECT MAX(stu_id)
        FROM student
    """)
    output = cursor.fetchone()
    print(output)
    # print(output[0] + 1)
    if output[0] is None:
        return 1000
    else:
        return output[0] + 1


def gen_fa_id():
    cursor.execute("""
        SELECT MAX(fa_id)
        FROM faculty
    """)
    output = cursor.fetchone()
    print(output)
    # print(output[0] + 1)
    if output[0] is None:
        return 2000
    else:
        return output[0] + 1


def gen_prof_id():
    cursor.execute("""
        SELECT MAX(prof_id)
        FROM professor
    """)
    output = cursor.fetchone()
    print(output)
    # print(output[0] + 1)
    if output[0] is None:
        return 3000
    else:
        return output[0] + 1


## Student back-end
def fetch_student_with_id(stu_id):
    query = """
    SELECT first_name, last_name, phone_number, email, addr, gpa, tuition, enr_yr, gender
    FROM university_person as up, student as s
    WHERE up.uni_id = s.uni_id
    AND s.stu_id = %s
    """
    cursor.execute(query, (stu_id,))
    fetched = cursor.fetchone()
    first_name = fetched[0]
    last_name = fetched[1]
    phone_number = fetched[2]
    email = fetched[3]
    addr = fetched[4]
    gpa = fetched[5]
    tuition = fetched[6]
    enr_yr = fetched[7]
    gender = fetched[8]
    student = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "email": email,
        "addr": addr,
        "gpa": gpa,
        "tuition": tuition,
        "enr_yr": enr_yr,
        "gender": gender,
    }
    return student


def fetch_students():
    output = []
    cursor.execute("""SELECT stu_id, first_name, last_name, phone_number, email, addr, gpa, tuition, enr_yr
    FROM university_person as up, student as s
    WHERE up.uni_id = s.uni_id
    ORDER BY stu_id;""")
    fetched = cursor.fetchall()
    for student in fetched:
        stu_id = student[0]
        first_name = student[1]
        last_name = student[2]
        phone_number = student[3]
        email = student[4]
        addr = student[5]
        gpa = student[6]
        tuition = student[7]
        enr_yr = student[8]
        output.append({
            "stu_id": stu_id,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "email": email,
            "addr": addr,
            "gpa": gpa,
            "tuition": tuition,
            "enr_yr": enr_yr,
        })
    return output


@app.route('/manage_students')
def index():
    return render_template('index.html', students=fetch_students())


@app.route('/manage_students/edit/<int:stu_id>', methods=['GET', 'POST'])
def edit_student(stu_id):
    if request.method == 'POST':
        # Update the student information
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        addr = request.form['addr']
        gpa = float(request.form['gpa'])
        tuition = float(request.form['tuition'])
        enr_yr = request.form['enr_yr']
        gender = request.form['gender']
        query = """
            UPDATE university_person as up
            SET first_name = %s, last_name = %s, phone_number = %s, email = %s, addr = %s, gender = %s
            FROM student as s
            WHERE s.uni_id = up.uni_id
            AND s.stu_id = %s;
        """
        cursor.execute(query, (first_name, last_name, phone_number, email, addr, gender, stu_id))
        query = """
            UPDATE student
            SET gpa = %s, tuition = %s, enr_yr = %s
            WHERE stu_id = %s
        """
        cursor.execute(query, (gpa, tuition, enr_yr, stu_id))
        conn.commit()
        return redirect(url_for('index'))

    return render_template('edit_student.html', student=fetch_student_with_id(stu_id))


@app.route('/manage_students/delete/<int:stu_id>')
def delete_student(stu_id):
    # Delete the student
    query = """
        DELETE FROM university_person
        USING student
        WHERE student.uni_id = university_person.uni_id
        AND student.stu_id = %s;
    """
    cursor.execute(query, (stu_id,))
    conn.commit()
    return redirect(url_for('index'))


@app.route('/manage_students/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # Fetch form data
        add_first_name = request.form['add_first_name']
        add_last_name = request.form['add_last_name']
        add_phone_number = request.form['add_phone_number']
        add_email = request.form['add_email']
        add_address = request.form['add_address']
        add_gpa = request.form['add_gpa']
        add_tuition = request.form['add_tuition']
        add_enrollment_year = request.form['add_enrollment_year']
        add_gender = request.form['add_gender']

        # Generate a unique IDs
        new_stu_id = gen_stu_id()
        new_uni_id = gen_uni_id()
        query = """
            INSERT INTO university_person VALUES
            (%s, %s, %s, %s, %s, %s, %s);
            INSERT INTO student VALUES
            (%s, %s, %s, %s, %s);
        """
        cursor.execute(query, (new_uni_id, add_first_name, add_last_name, add_phone_number, add_email, add_address,
                               add_gender, new_uni_id, new_stu_id, float(add_gpa), float(add_tuition),
                               add_enrollment_year))
        conn.commit()
        return redirect(url_for('index'))

    return render_template('add_student.html')


### Manage professor back-end:

def fetch_profs():
    output = []
    cursor.execute("""
        SELECT prof_id, first_name, last_name, phone_number, email, addr, salary
        FROM university_person as up, professor as p, faculty as f
        WHERE up.uni_id = p.uni_id
        AND p.uni_id = f.uni_id
        ORDER BY prof_id;
    """)
    fetched = cursor.fetchall()
    for prof in fetched:
        prof_id = prof[0]
        first_name = prof[1]
        last_name = prof[2]
        phone_number = prof[3]
        email = prof[4]
        addr = prof[5]
        salary = prof[6]
        output.append({
            "prof_id": prof_id,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "email": email,
            "addr": addr,
            "salary": salary,
        })
    return output


def fetch_professor_with_id(prof_id):
    query = """
        SELECT first_name, last_name, phone_number, email, addr, salary, gender
        FROM university_person as up, professor as p, faculty as f
        WHERE up.uni_id = p.uni_id
        AND p.uni_id = f.uni_id
        AND p.prof_id = %s
    """
    cursor.execute(query, (prof_id,))
    fetched = cursor.fetchone()
    first_name, last_name, phone_number, email, addr, salary, gender = fetched
    professor = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "email": email,
        "addr": addr,
        "salary": salary,
        "gender": gender,
    }
    return professor


@app.route('/manage_professors')
def manage_prof():
    return render_template('manage_prof.html', professors=fetch_profs())


@app.route('/manage_professors/add_professor', methods=['GET', 'POST'])
def add_prof():
    if request.method == 'POST':
        # Fetch form data
        add_first_name = request.form['add_first_name']
        add_last_name = request.form['add_last_name']
        add_phone_number = request.form['add_phone_number']
        add_email = request.form['add_email']
        add_address = request.form['add_address']
        add_salary = request.form['add_salary']
        add_gender = request.form['add_gender']

        # Generate unique IDs
        new_prof_id = gen_prof_id()
        new_fa_id = gen_fa_id()
        new_uni_id = gen_uni_id()
        query = """
                INSERT INTO university_person VALUES
                (%s, %s, %s, %s, %s, %s, %s);
                INSERT INTO faculty VALUES
                (%s, %s, %s);
                INSERT INTO professor VALUES
                (%s, %s, %s);
            """
        cursor.execute(query, (new_uni_id, add_first_name, add_last_name, add_phone_number, add_email, add_address,
                               add_gender, new_uni_id, new_fa_id, float(add_salary),
                               new_uni_id, new_fa_id, new_prof_id))
        conn.commit()
        return redirect(url_for('manage_prof'))

    return render_template('add_prof.html')


@app.route('/manage_professors/delete/<int:prof_id>')
def delete_prof(prof_id):
    # Delete the professor
    query = """
        DELETE FROM university_person
        USING professor
        WHERE professor.uni_id = university_person.uni_id
        AND professor.prof_id = %s;
    """
    cursor.execute(query, (prof_id,))
    conn.commit()
    return redirect(url_for('manage_prof'))


@app.route('/manage_professors/edit/<int:prof_id>', methods=['GET', 'POST'])
def edit_prof(prof_id):
    if request.method == 'POST':
        # Update the professor information
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        addr = request.form['addr']
        salary = float(request.form['salary'])
        gender = request.form['gender']

        query = """
            UPDATE university_person as up
            SET first_name = %s, last_name = %s, phone_number = %s, email = %s, addr = %s, gender = %s
            FROM professor as p, faculty as f
            WHERE p.uni_id = up.uni_id
            AND p.uni_id = f.uni_id
            AND p.prof_id = %s;
        """
        cursor.execute(query, (first_name, last_name, phone_number, email, addr, gender, prof_id))

        query = """
            UPDATE faculty
            SET salary = %s
            WHERE uni_id IN (
                SELECT uni_id FROM professor WHERE prof_id = %s
            );
        """
        cursor.execute(query, (salary, prof_id))

        conn.commit()
        return redirect(url_for('manage_prof'))

    return render_template('edit_prof.html', professor=fetch_professor_with_id(prof_id))


if __name__ == '__main__':
    app.run(debug=True)
