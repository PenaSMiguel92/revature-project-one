## Project One - Prescription Store:

The current system is messy and errors can occur.
A store where Patients can login, see their prescriptions, buy refills, and see a history of their purchased prescriptions.

## Note:
- Please run the prescription_store.sql file on the MySQL Workbench before running this application.
- The entire project is inside a virtual environment folder called project-one. 
- config/ directory needs to be created with a .csv file inside with the following data:
    - user, password, host, and database values in quotes. 
- This is primarily meant as a security feature, but can be easily overided by hard coding the values.
- The config/ folder was added to the .gitignore file, so that sensitive information isn't uploaded to github.
- I wrote a script that generates medications and cost randomly, using real names from this API:
    - ``https://lhncbc.nlm.nih.gov/RxNav/APIs/PrescribableAPIs.html``

## Features:
- Focus on CLI, but once core features are implemented -> tkinter GUI
- Doctors can login, prescribe a medication to a patient, and see the medication details.
- Admin can see all orders and users, add/update/remove medications, removing/editing of users, apply/drop doctor role to users. 
- This application shall create users, prescriptions, and orders. 
- This application shall read users, prescriptions, and orders. 
- This application shall update users, prescriptions, and orders.
- This application shall delete users, prescriptions, but not orders.
- Three or more tables/collections could be medications, users, prescriptions, roles, and orders.
    - medications should hold records of all medications, their primary key id, name, and their cost per refill.
    - users should hold records of all users, their primary key id, first, last, role foreign key, username, and hashed password.
    - prescriptions should hold records of all prescriptions, their primary key id, doctor id foreign key, patient id foreign key, medication id
    - roles should hold records of all possible roles, their primary key id, role name (Patient, Doctor, Admin)
    - orders should hold records of all orders, including their primary key id, user id foreign key, amount, medication id foreign key, and date.
- The login feature will be handled by a control object that creates and manages users and their roles.
- Each class should have access to a Log method that handles logging events automatically, similar to input_validation from project-zero.

## Tech Stack:
    Python 3.12.4
        - dataclasses module for making a codebase similar to Java when working with databases.
        - mysql.connector for connecting to mysql database.
        - requests module for API calls, just once.
    VS Code
    MySQL
        - Four tables/collections -> JOIN queries necessary.
        - MySQL has nicer syntax for joining multiple tables.
        - MySQL has stricter rules -> less likely to be buggy.
    Git
