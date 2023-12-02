from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2

DATABASE_NAME = "cse412-project"
DATABASE_HOST = "localhost"
USER = "cse412"
PASSWORD = "1234"
PORT = "5432"
students = []

app = Flask(__name__)
app.secret_key = 'cse412-project'

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


def gen_admin_id():
    cursor.execute("""
        SELECT MAX(admin_id)
        FROM admin_user
    """)
    output = cursor.fetchone()
    if output[0] is None:
        return 1
    else:
        return output[0] + 1


def gen_course_id():
    cursor.execute("""
        SELECT MAX(course_id)
        FROM course
    """)
    output = cursor.fetchone()
    if output[0] is None:
        return 500
    else:
        return output[0] + 1


def gen_room_id():
    cursor.execute("""
            SELECT MAX(room_id)
            FROM course
        """)
    output = cursor.fetchone()
    if output[0] is None:
        return 100
    else:
        return output[0] + 1


def gen_dept_id():
    cursor.execute("""
        SELECT MAX(dept_id)
        FROM department
    """)
    output = cursor.fetchone()
    if output[0] is None:
        return 700
    else:
        return output[0] + 1


## Login back-end
def verify_user(username, password):
    """
    This function returns true if the user is found in the database, false if not
    :param username:
    :param password:
    :return:
    """
    query = """
        SELECT admin_id 
        FROM admin_user 
        WHERE user_name = %s 
        AND password = %s;
    """
    cursor.execute(query, (username, password,))
    output = cursor.fetchone()
    if output is None:
        return False
    else:
        return True


def user_name_exist(username):
    query = """
        SELECT admin_id 
        FROM admin_user 
        WHERE user_name = %s;
    """
    cursor.execute(query, (username,))
    output = cursor.fetchone()
    if output is None:
        return False
    else:
        return True


def create_new_user(username, password):
    if user_name_exist(username):
        return 1
    else:
        new_admin_id = gen_admin_id()
        query = """
            INSERT INTO admin_user VALUES
            (%s, %s, %s)
        """
        cursor.execute(query, (new_admin_id, password, username))
        conn.commit()
        return 0


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Authentication logic
        if verify_user(username, password):
            return redirect(url_for('index'))

        # If authentication fails, render an error message
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')


@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        secret_code = request.form['secret_code']

        if secret_code == "cse412":
            if create_new_user(username, password) == 0:
                flash('Admin user created successfully!', 'success')
                return redirect(url_for('login'))
            elif create_new_user(username, password) == 1:
                flash('User already exists!', 'error')
        else:
            flash('Invalid secret code. Admin user not created.', 'danger')

    return render_template('create_user.html')


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


# Manage course backend
def fetch_courses():
    output = []
    query = """
        SELECT c.course_id, c.room_id, c.des, c.req, c.addr, up.first_name, up.last_name, p.uni_id
        FROM university_person AS up
        JOIN professor AS p ON up.uni_id = p.uni_id
        JOIN teaches AS t ON p.uni_id = t.uni_id
        JOIN course AS c ON t.course_id = c.course_id AND t.room_id = c.room_id
        ORDER BY c.course_id;
    """
    cursor.execute(query)
    fetched = cursor.fetchall()
    for course in fetched:
        course_id, room_id, des, req, addr, prof_first_name, prof_last_name, prof_uni_id = course
        output.append({
            "course_id": course_id,
            "room_id": room_id,
            "des": des,
            "req": req,
            "addr": addr,
            "professor": {
                "uni_id": prof_uni_id,
                "first_name": prof_first_name,
                "last_name": prof_last_name,
            }
        })
    return output


def fetch_professors_for_dropdown():
    output = []
    cursor.execute("""
        SELECT prof_id, first_name, last_name
        FROM university_person as up, professor as p
        WHERE up.uni_id = p.uni_id
        ORDER BY prof_id;
    """)
    fetched = cursor.fetchall()
    for professor in fetched:
        prof_id, first_name, last_name = professor
        output.append({
            "prof_id": prof_id,
            "first_name": first_name,
            "last_name": last_name,
        })
    return output


def fetch_course_with_id(course_id, uni_id):
    print(f"Fetching with {course_id}, {uni_id}")
    query = """
        SELECT c.course_id, c.room_id, c.des, c.req, c.addr, p.prof_id, p.uni_id
        FROM course AS c
        JOIN teaches AS t ON c.course_id = t.course_id AND c.room_id = t.room_id
        JOIN professor as p ON t.uni_id = p.uni_id
        WHERE c.course_id = %s
        AND t.uni_id = %s;
    """
    cursor.execute(query, (course_id, uni_id))
    fetched = cursor.fetchone()

    if fetched:
        course = {
            "course_id": fetched[0],
            "room_id": fetched[1],
            "des": fetched[2],
            "req": fetched[3],
            "addr": fetched[4],
            "prof_id": fetched[5],
            "uni_id": fetched[6],
        }
        return course
    else:
        return None


def get_uni_id_for_prof(prof_id):
    query = """
        SELECT uni_id
        FROM professor
        WHERE prof_id = %s
    """
    cursor.execute(query, (prof_id,))
    output = cursor.fetchone()
    return output[0]


@app.route('/manage_courses')
def manage_course():
    return render_template('manage_course.html', courses=fetch_courses())


@app.route('/manage_courses/add_course', methods=['GET', 'POST'])
def add_course():
    professors = fetch_professors_for_dropdown()

    if request.method == 'POST':
        # Fetch form data
        add_course_id = gen_course_id()
        add_room_id = gen_room_id()
        add_des = request.form['add_des']
        add_req = request.form['add_req']
        add_addr = request.form['add_addr']
        add_taught_by = int(request.form['add_taught_by'])
        add_uni_id = int(get_uni_id_for_prof(add_taught_by))

        if add_req == "":
            add_req = None

        # Insert new course
        query = """
            INSERT INTO course VALUES
            (%s, %s, %s, %s, %s);
            INSERT INTO teaches VALUES
            (%s, %s, %s);
        """
        cursor.execute(query, (add_course_id, add_room_id, add_des,
                               add_req, add_addr, add_uni_id, add_course_id, add_room_id))
        conn.commit()

        return redirect(url_for('manage_course'))

    return render_template('add_course.html', professors=professors)


@app.route('/manage_courses/delete_course/<int:course_id>/<int:uni_id>')
def delete_course(course_id, uni_id):
    # Delete the course
    query = """
        DELETE FROM teaches
        WHERE course_id = %s
        AND uni_id = %s;
    """
    cursor.execute(query, (course_id, uni_id))
    conn.commit()
    return redirect(url_for('manage_course'))


@app.route('/manage_courses/edit_course/<int:course_id>/<int:uni_id>', methods=['GET', 'POST'])
def edit_course(course_id, uni_id):
    professors = fetch_professors_for_dropdown()
    course = fetch_course_with_id(course_id, uni_id)

    if request.method == 'POST':
        # Fetch form data
        edit_des = request.form['edit_des']
        edit_req = request.form['edit_req']
        edit_addr = request.form['edit_addr']
        edit_taught_by = int(request.form['edit_taught_by'])
        edit_uni_id = int(get_uni_id_for_prof(edit_taught_by))

        if edit_req == "":
            edit_req = None

        # Update course information
        query = """
            UPDATE course
            SET des = %s, req = %s, addr = %s
            WHERE course_id = %s;

            UPDATE teaches
            SET uni_id = %s
            WHERE course_id = %s;
        """
        cursor.execute(query, (edit_des, edit_req, edit_addr, course_id, edit_uni_id, course_id))
        conn.commit()

        return redirect(url_for('manage_course'))

    return render_template('edit_course.html', course=course, professors=professors)


# Assign course backend
def fetch_unassigned_courses():
    output = []
    query = """
        SELECT c.course_id, c.room_id, c.des, c.req, c.addr
        FROM course AS c
        LEFT JOIN teaches AS t ON c.course_id = t.course_id AND c.room_id = t.room_id
        WHERE t.uni_id IS NULL;
    """
    cursor.execute(query)
    unassigned_courses = cursor.fetchall()
    if unassigned_courses:
        for course in unassigned_courses:
            course_id, room_id, des, req, addr = course
            output.append({
                "course_id": course_id,
                "room_id": room_id,
                "des": des,
                "addr": addr,
            })
    return output


@app.route('/manage_courses/assign_course', methods=['GET', 'POST'])
def assign_course():
    unassigned_courses = fetch_unassigned_courses()
    print(unassigned_courses)
    professors = fetch_professors_for_dropdown()

    if request.method == 'POST':
        # Fetch form data
        assign_course_id = request.form['assign_course_id']
        assign_room_id = request.form['assign_room_id']
        assign_taught_by = int(request.form['assign_taught_by'])
        assign_uni_id = int(get_uni_id_for_prof(assign_taught_by))

        # Assign the course
        query = """
            INSERT INTO teaches VALUES (%s, %s, %s);
        """
        cursor.execute(query, (assign_uni_id, assign_course_id, assign_room_id))
        conn.commit()

        return redirect(url_for('manage_course'))

    return render_template('assign_course.html', unassigned_courses=unassigned_courses, professors=professors)


## Department backend
def fetch_departments():
    output = []
    cursor.execute("""
        SELECT dept_id, des, capacity, fund
        FROM department
        ORDER BY dept_id;
    """)
    fetched = cursor.fetchall()
    for department in fetched:
        dept_id, des, capacity, fund = department
        output.append({
            "dept_id": dept_id,
            "des": des,
            "capacity": capacity,
            "fund": fund,
        })
    return output


def add_department(des, capacity, fund):
    dept_id = gen_dept_id()
    query = """
        INSERT INTO department (dept_id, des, capacity, fund)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (dept_id, des, capacity, fund))
    conn.commit()


def fetch_faculty_from_dept(dept_id):
    output = []
    query = """
        SELECT fa_id, first_name, last_name, salary, f.uni_id
        FROM university_person as up, faculty as f, works_in as w
        WHERE up.uni_id = f.uni_id
        AND f.uni_id = w.uni_id
        AND w.dept_id = %s;
    """
    cursor.execute(query, (dept_id,))
    fetched = cursor.fetchall()
    if fetched:
        for faculty in fetched:
            fa_id, first_name, last_name, salary, uni_id = faculty
            output.append({
                "fa_id": fa_id,
                "first_name": first_name,
                "last_name": last_name,
                "salary": salary,
                "uni_id": uni_id,
            })
    return output


def fetch_faculty_with_fa_id(fa_id):
    query = """
        SELECT first_name, last_name, phone_number, email, addr, salary, gender, f.uni_id
        FROM university_person as up, faculty as f
        WHERE up.uni_id = f.uni_id
        AND f.fa_id = %s
    """
    cursor.execute(query, (fa_id,))
    fetched = cursor.fetchone()
    first_name, last_name, phone_number, email, addr, salary, gender, uni_id = fetched
    output = {
        "fa_id": fa_id,
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "email": email,
        "addr": addr,
        "salary": salary,
        "gender": gender,
        "uni_id": uni_id,
    }

    return output


def fetch_department_with_dept_id(dept_id):
    query = """
            SELECT des, capacity, fund
            FROM department
            WHERE dept_id = %s;
        """
    cursor.execute(query, (dept_id,))
    department_info = cursor.fetchone()

    if department_info:
        department = {
            "dept_id": dept_id,
            "des": department_info[0],
            "capacity": department_info[1],
            "fund": department_info[2],
        }
        return department
    return {}


@app.route('/manage_departments')
def manage_department():
    return render_template('manage_department.html', departments=fetch_departments())


@app.route('/manage_departments/add_department', methods=['GET', 'POST'])
def add_department_route():
    if request.method == 'POST':
        des = request.form['add_des']
        capacity = request.form['add_capacity']
        fund = request.form['add_fund']

        add_department(des, capacity, fund)
        return redirect(url_for('manage_department'))

    return render_template('add_department.html')


@app.route('/manage_departments/delete_department/<int:dept_id>')
def delete_department(dept_id):
    query = """
        DELETE FROM department
        WHERE dept_id = %s;
    """
    cursor.execute(query, (dept_id,))
    conn.commit()
    return redirect(url_for('manage_department'))


@app.route('/manage_departments/edit_department/<int:dept_id>', methods=['GET', 'POST'])
def edit_department(dept_id):
    if request.method == 'POST':
        # Update the department information
        edit_des = request.form['edit_des']
        edit_capacity = int(request.form['edit_capacity'])
        edit_fund = request.form['edit_fund']

        query = """
            UPDATE department
            SET des = %s, capacity = %s, fund = %s
            WHERE dept_id = %s;
        """
        cursor.execute(query, (edit_des, edit_capacity, edit_fund, dept_id))
        conn.commit()

        return redirect(url_for('manage_department'))

    # Fetch department information for pre-populating the form
    query = """
        SELECT des, capacity, fund
        FROM department
        WHERE dept_id = %s;
    """
    cursor.execute(query, (dept_id,))
    department_info = cursor.fetchone()

    if department_info:
        department = {
            "dept_id": dept_id,
            "des": department_info[0],
            "capacity": department_info[1],
            "fund": department_info[2],
        }
        return render_template('edit_department.html', department=department)
    else:
        # Handle department not found
        print("error")


@app.route('/manage_departments/more_info/<int:dept_id>')
def more_info(dept_id):
    # Fetch department information
    query_dept = """
        SELECT des, capacity, fund
        FROM department
        WHERE dept_id = %s;
    """
    cursor.execute(query_dept, (dept_id,))
    department_info = cursor.fetchone()

    if department_info:
        department = {
            "dept_id": dept_id,
            "des": department_info[0],
            "capacity": department_info[1],
            "fund": department_info[2],
        }

        # Fetch faculty members in the department
        faculties = fetch_faculty_from_dept(dept_id)

        return render_template('more_info.html', department=department, faculties=faculties)

    # Handle department not found
    return redirect(url_for('manage_department'))


@app.route('/manage_departments/more_info/<int:dept_id>/add_faculty', methods=['GET', 'POST'])
def add_faculty(dept_id):
    if request.method == 'POST':
        add_first_name = request.form['add_first_name']
        add_last_name = request.form['add_last_name']
        add_phone_number = request.form['add_phone_number']
        add_email = request.form['add_email']
        add_address = request.form['add_address']
        add_salary = request.form['add_salary']
        add_gender = request.form['add_gender']

        # Generate unique IDs
        new_fa_id = gen_fa_id()
        new_uni_id = gen_uni_id()
        query = """
            INSERT INTO university_person VALUES
            (%s, %s, %s, %s, %s, %s, %s);
            INSERT INTO faculty VALUES
            (%s, %s, %s);
            INSERT INTO works_in VALUES
            (%s, %s)
        """
        cursor.execute(query, (new_uni_id, add_first_name, add_last_name, add_phone_number, add_email, add_address,
                               add_gender, new_uni_id, new_fa_id, float(add_salary), new_uni_id, dept_id))
        conn.commit()
        return redirect(url_for('more_info', dept_id=dept_id))

    return render_template('add_faculty.html', department=fetch_department_with_dept_id(dept_id))


@app.route('/manage_departments/more_info/<int:dept_id>/<int:uni_id>')
def delete_faculty(dept_id, uni_id):
    # Delete the professor
    query = """
        DELETE FROM university_person
        USING faculty
        WHERE faculty.uni_id = university_person.uni_id
        AND faculty.uni_id = %s;
    """
    cursor.execute(query, (uni_id,))
    conn.commit()
    return redirect(url_for('more_info', dept_id=dept_id))


@app.route('/manage_departments/more_info/<int:dept_id>/<int:fa_id>/edit', methods=['GET', 'POST'])
def edit_faculty(dept_id, fa_id):
    faculty = fetch_faculty_with_fa_id(fa_id)
    department = fetch_department_with_dept_id(dept_id)
    if request.method == 'POST':
        # Update the professor information
        first_name = request.form['edit_first_name']
        last_name = request.form['edit_last_name']
        phone_number = request.form['edit_phone_number']
        email = request.form['edit_email']
        addr = request.form['edit_address']
        salary = float(request.form['edit_salary'])
        gender = request.form['edit_gender']

        query = """
            UPDATE university_person as up
            SET first_name = %s, last_name = %s, phone_number = %s, email = %s, addr = %s, gender = %s
            FROM faculty as f
            WHERE f.uni_id = up.uni_id
            AND f.fa_id = %s;
        """
        cursor.execute(query, (first_name, last_name, phone_number, email, addr, gender, fa_id))

        query = """
            UPDATE faculty
            SET salary = %s
            WHERE fa_id = %s;
        """
        cursor.execute(query, (salary, fa_id))

        conn.commit()
        return redirect(url_for('more_info', dept_id=dept_id))

    return render_template('edit_faculty.html', department=department,
                           faculty=faculty)


## Assign faculty backend
def fetch_unassigned_faculties():
    output = []
    query = """
        SELECT f.uni_id, f.fa_id, first_name, last_name
        FROM faculty f, university_person as up
        WHERE NOT EXISTS (
            SELECT 1
            FROM works_in w
            WHERE w.uni_id = f.uni_id
        )
        AND f.uni_id = up.uni_id;
    """
    cursor.execute(query)
    unassigned_faculties = cursor.fetchall()
    if unassigned_faculties:
        for faculty in unassigned_faculties:
            uni_id, fa_id, first_name, last_name = faculty
            output.append({
                "uni_id": uni_id,
                "fa_id": fa_id,
                "first_name": first_name,
                "last_name": last_name,
            })
    return output


@app.route('/manage_departments/assign_faculty', methods=['GET', 'POST'])
def assign_faculty():
    unassigned_faculties = fetch_unassigned_faculties()
    departments = fetch_departments()

    if request.method == 'POST':
        # Fetch form data
        assign_uni_id = request.form['assign_uni_id']
        assign_dept_id = request.form['assign_department']

        # Assign the course
        query = """
            INSERT INTO works_in VALUES (%s, %s);
        """
        cursor.execute(query, (assign_uni_id, assign_dept_id,))
        conn.commit()

        return redirect(url_for('manage_department'))

    return render_template('assign_faculty.html',
                           unassigned_faculties=unassigned_faculties,
                           departments=departments)


if __name__ == '__main__':
    app.run(debug=True)
