from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Sample data (replace this with data fetched from the database)
students = [
    {"uni_id": 1, "first_name": "John", "last_name": "Doe", "phone_number": "1234567890",
     "email": "john.doe@example.com", "addr": "123 Main St", "gpa": 3.8, "tuition": 5000.00, "enr_yr": "2022"},
    {"uni_id": 2, "first_name": "Jane", "last_name": "Smith", "phone_number": "9876543210",
     "email": "jane.smith@example.com", "addr": "456 Oak St", "gpa": 3.5, "tuition": 4800.00, "enr_yr": "2021"},
]


@app.route('/')
def index():
    return render_template('index.html', students=students)


@app.route('/edit/<int:uni_id>', methods=['GET', 'POST'])
def edit_student(uni_id):
    student = next((s for s in students if s['uni_id'] == uni_id), None)

    if request.method == 'POST':
        # Update the student information (replace this with database update)
        student['first_name'] = request.form['first_name']
        student['last_name'] = request.form['last_name']
        student['phone_number'] = request.form['phone_number']
        student['email'] = request.form['email']
        student['addr'] = request.form['addr']
        student['gpa'] = float(request.form['gpa'])
        student['tuition'] = float(request.form['tuition'])
        student['enr_yr'] = request.form['enr_yr']

        return redirect(url_for('index'))

    return render_template('edit_student.html', student=student)


@app.route('/delete/<int:uni_id>')
def delete_student(uni_id):
    # Delete the student (replace this with database delete)
    global students
    students = [s for s in students if s['uni_id'] != uni_id]
    return redirect(url_for('index'))


@app.route('/add_student', methods=['GET', 'POST'])
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

        # Generate a unique uni_id (replace this with uni_id logic)
        new_uni_id = len(students) + 1

        # Add the new student to the list (replace this with database insert)
        students.append({
            'uni_id': new_uni_id,
            'first_name': add_first_name,
            'last_name': add_last_name,
            'phone_number': add_phone_number,
            'email': add_email,
            'addr': add_address,
            'gpa': add_gpa,
            'tuition': add_tuition,
            'enr_yr': add_enrollment_year,
            # Add other attributes for the new student
        })

        return redirect(url_for('index'))

    return render_template('add_student.html')


if __name__ == '__main__':
    app.run(debug=True)
