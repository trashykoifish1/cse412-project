# User Manual
## Requirement:
Assuming the user has already installed:
- [PostgreSQL](https://www.postgresql.org/)
- [Python](https://www.python.org/)
- For a detailed installation guide, refer to [README.md](README.md)
## Manual:
### Login page

![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/59c13b1f-e9f9-4ca6-8173-dc28791922f1)

Upon starup, the user will be greeted with a login page, if an account has already been created or given to you, put in your ```username``` and ```password``` and click ```Sign In```. If not click the ```Create User``` button.

### Create user
![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/7ed9bc0b-608e-44e1-bc62-66977d8b8ab2)

Enter your desired ```username``` and ```password``` along with the ```secret code``` provided to you. For the purpose of testing, you can enter ```cse412``` as the secret code. After a user has been succesfully created, proceed to ```login```.

After successfully logged in, you can proceed with the main functionalities of the program.

---
### Managing Student
> To switch between different functionalities, use the navigation bar on the left side of the screen

![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/4c729f37-212f-4f22-b13b-56c0a3f138f3)

 Upon first login, your student database will be empty, to create a new student, click the ```Add New Student``` button on the top right of the page.

 Enter all the required information for a student, then click the ```Add Student``` button. If you change your mind, click ```Cancel```

![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/1c7165c9-be2b-458a-ba4f-09386dd8064e)
![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/d156db6c-fe2f-4133-bd6b-606f94152fe3)

 After adding, the student will appear in your ```Manage Student``` page.
![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/a12601c7-a70d-4ed7-ab59-eca7b9c56c59)

> To ```delete``` or ```edit``` a student, you can click the trash can icon or the pen icon respectively.

### Managing Professor
> Managing professor is similar to managing student, with identical functions for the ```Add New Professor``` button as well as the ```delete``` and ```edit``` functions.

![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/f41added-aa6e-47a7-89a3-ce4c311ab529)

### Managing Course
> This is where you can manage all the courses offered, the ```Add New Course```, ```delete``` and ```edit``` functions are similar to the last two, additionally, there is a ```Assign Course``` function.

![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/e0e6bb76-b22d-49eb-932a-f990f5b04ac8)

Upon deletion, a course would not be erased from the database, instead, it still exists but without an assigned ```professor```, the ```Assign Course``` function exists so that users can reassign these courses to new professors.

![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/daacaf18-5f91-48cb-a296-f87550875fe3)

Select an ```Unasigned Course``` and a ```Professor```, then click ```Assign Course```

### Managing Department
> This is where you can manage all the departments of the school, ```Add New Department```, ```delete```, ```edit``` and ```Assign Faculty``` work similarly to Managing Course.

```Assign Faculty```: when a new Professor is created, they will not be apart of any departments, in order to assign this professor to a department, you can use this button, functionality and user interface wise it is similar to ```Assign Course``` 

![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/f677844d-deb9-4fd1-b190-304c1bcabd07)

Additionally, there is a ```More Info``` function in addition to ```delete``` and ```edit``` in the ```Actions``` section

![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/c8758a54-ebca-4a89-bb19-fb98971b5d86)

This is where all the faculties of a certain department will be listed. You can also ```Add Faculty```, ```delete``` and ```edit``` any faculty member of that department

![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/800f9a2a-53e0-4b7e-8894-748a387753b5)

### Logout
In order to logout, you can click the ASU logo on the top left of the page

![image](https://github.com/trashykoifish1/cse412-project/assets/112349723/1c8e240b-ca42-4925-88b4-678f1d09a782)
