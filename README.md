# Student Management Web App
> This is a CRUD system for managing students, professors, courses and departments of a university (ASU).

## User Guide
- Refer to [USERMANUAL.md](USERMANUAL.md)
## Installation
- Install [Python](https://www.python.org/downloads/)
- Install [PostgreSQL](https://www.postgresql.org/download/)
- Clone the project
```
$ git clone https://github.com/trashykoifish1/cse412-project
```
- Or download the [zip](https://github.com/trashykoifish1/cse412-project/archive/refs/heads/main.zip)

### Initializing Database
- Create an admin role in your database with the username `cse412` and password `1234`
```
CREATE ROLE cse412 WITH
	LOGIN
	SUPERUSER
	CREATEDB
	CREATEROLE
	INHERIT
	REPLICATION
	CONNECTION LIMIT -1
	PASSWORD '1234';
```
- Create a new database with the name `cse412-project`
```
CREATE DATABASE "cse412-project"
    WITH
    OWNER = khoi
    ENCODING = 'UTF8'
    LOCALE_PROVIDER = 'libc'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
```
> Using database_dump.sql
- [pgAdmin4](https://www.pgadmin.org/docs/pgadmin4/development/restore_dialog.html)
- [psql](https://www.postgresql.org/docs/8.0/backup.html)

- Navigate to your `cse412-project` database and run the following commands
```
------- Entity Sets -------
CREATE TABLE admin_user
(
admin_id INTEGER NOT NULL,
password VARCHAR(20) NOT NULL,
user_name VARCHAR(20) NOT NULL,
PRIMARY KEY (admin_id)
);

CREATE TABLE university_person
(
uni_id INTEGER NOT NULL,
first_name VARCHAR(15),
last_name VARCHAR(15),
phone_number VARCHAR(10),
email VARCHAR(30),
addr VARCHAR(30),
gender CHAR,
PRIMARY KEY (uni_id)
);

CREATE TABLE student
(
uni_id INTEGER NOT NULL REFERENCES university_person(uni_id) ON DELETE CASCADE,
stu_id INTEGER NOT NULL UNIQUE,
gpa FLOAT,
tuition FLOAT,
enr_yr VARCHAR(4),
PRIMARY KEY (uni_id)
);

CREATE TABLE faculty
(
uni_id INTEGER NOT NULL REFERENCES university_person(uni_id) ON DELETE CASCADE,
fa_id INTEGER NOT NULL UNIQUE,
salary FLOAT,
PRIMARY KEY (uni_id)
);


CREATE TABLE professor
(
uni_id INTEGER NOT NULL REFERENCES faculty(uni_id) ON DELETE CASCADE,
fa_id INTEGER NOT NULL REFERENCES faculty(fa_id) ON DELETE CASCADE,
prof_id INTEGER NOT NULL UNIQUE,
PRIMARY KEY (uni_id)
);

CREATE TABLE course
(
course_id INTEGER NOT NULL,
room_id INTEGER NOT NULL,
des VARCHAR(30),
req INTEGER,
addr VARCHAR(30),
PRIMARY KEY (course_id, room_id)
);

CREATE TABLE department
(
dept_id INTEGER NOT NULL,
des VARCHAR(30),
capacity INTEGER,
fund FLOAT,
PRIMARY KEY (dept_id)
);

------- Relationships -------
CREATE TABLE manages
(
admin_id INTEGER NOT NULL REFERENCES admin_user(admin_id) ON DELETE CASCADE,
system_id INTEGER NOT NULL,
PRIMARY KEY (admin_id, system_id)
);

CREATE TABLE enrolls_in
(
student_uni_id INTEGER NOT NULL REFERENCES student(uni_id) ON DELETE CASCADE,
course_id INTEGER NOT NULL,
room_id INTEGER NOT NULL,
PRIMARY KEY (student_uni_id, course_id, room_id),
FOREIGN KEY (course_id, room_id) REFERENCES course(course_id, room_id)
	ON DELETE CASCADE
);

CREATE TABLE teaches
(
uni_id INTEGER NOT NULL REFERENCES professor(uni_id) ON DELETE CASCADE,
course_id INTEGER NOT NULL,
room_id INTEGER NOT NULL,
PRIMARY KEY (uni_id, course_id, room_id),
FOREIGN KEY (course_id, room_id) REFERENCES course(course_id, room_id)
	ON DELETE CASCADE
);

CREATE TABLE has
(
course_id INTEGER NOT NULL,
room_id INTEGER NOT NULL,
dept_id INTEGER NOT NULL REFERENCES department(dept_id) ON DELETE CASCADE,
PRIMARY KEY (course_id, room_id, dept_id),
FOREIGN KEY (course_id, room_id) REFERENCES course(course_id, room_id)	
	ON DELETE CASCADE
);

CREATE TABLE works_in
(
uni_id INTEGER NOT NULL REFERENCES faculty(uni_id) ON DELETE CASCADE,
dept_id INTEGER NOT NULL REFERENCES department(dept_id) ON DELETE CASCADE,
PRIMARY KEY (uni_id, dept_id)
);
```


### Using PyCharm
- Download [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/?section=windows)
- Open the project using PyCharm and navigate to the Terminal

![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/93d164c4-9576-4ada-8139-fcc4e98ba8d1)

- Check if `pip` is installed

```
$ pip --version
```

- If pip is not installed, refer to pip [installation guide](https://pip.pypa.io/en/stable/installation/)

- Run this command in the PyCharm terminal

```
$ pip3 install -r requirements.txt
```

![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/cb4a0c23-1d6c-4744-abe0-6a73380eec57)

- If there is still errors from the packages in PyCharm, hover over the package name and click `Install [package-name]`
- Run the project from `main.py`
- Navigate to http://127.0.0.1:5000/ to start using the web application
  
### Using Terminal
- Navigate to the project folder using the terminal
- Install the requirements
```
$ pip install -r requirements.txt
```

![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/4f892a26-103e-46c5-9326-ead97f3c64ba)

- Run the app
```
$ flask --app main run
```
![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/6a870acb-e25b-4375-86ca-f107831d4d10)
- Navigate to http://127.0.0.1:5000/ to start using the web application

