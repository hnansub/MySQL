# # 1, Import libraries:
import mysql.connector
from mysql.connector import Error

#
#
# # __________________________________________
#
#
# # 2. Connects to the MySQL database server:
def create_connection(host_name, user_name, user_password,db_name, unix_socket):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            unix_socket=unix_socket
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("localhost", "root", "root","company_app","/Applications/MAMP/tmp/mysql/mysql.sock")
#
#
# # __________________________________________
#
#
# # 3. Create the database:
# def create_database(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print("Database created successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")


# create_database_query = "CREATE DATABASE company_app"
# create_database(connection, create_database_query)
#
#
# # __________________________________________
#
#
# # 4. Create function to excute queries:
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
#
#
# # __________________________________________
#
#
# # 5. Create queries for creating tables:
# create_employees_table = """
# CREATE TABLE employees (
#   id INTEGER PRIMARY KEY AUTO_INCREMENT,
#   name TEXT NOT NULL,
#   age INTEGER,
#   gender TEXT,
#   nationality TEXT
# ) ENGINE = InnoDB;
# """

# create_position_table = """
# CREATE TABLE IF NOT EXISTS position (
#   id INTEGER PRIMARY KEY AUTO_INCREMENT,
#   name TEXT NOT NULL,
#   salary INTEGER
# ) ENGINE = InnoDB
# """

# create_department_table = """
# CREATE TABLE IF NOT EXISTS department (
#   id INTEGER PRIMARY KEY AUTO_INCREMENT,
#   name TEXT NOT NULL,
#   description TEXT
# ) ENGINE = InnoDB
# """

# create_emplposition_table = """
# CREATE TABLE IF NOT EXISTS emplposition (
#   id INTEGER PRIMARY KEY AUTO_INCREMENT,
#   emply_id INTEGER NOT NULL,
#   position_id INTEGER NOT NULL,
#   FOREIGN KEY (emply_id) REFERENCES employees (id),
#   FOREIGN KEY (position_id) REFERENCES position (id)
# ) ENGINE = InnoDB
# """

# create_empldepart_table = """
# CREATE TABLE IF NOT EXISTS empldepart (
#   id INTEGER PRIMARY KEY AUTO_INCREMENT,
#   emply_id INTEGER NOT NULL,
#   depart_id INTEGER NOT NULL,
#   FOREIGN KEY (emply_id) REFERENCES employees (id),
#   FOREIGN KEY (depart_id) REFERENCES department (id)
# ) ENGINE = InnoDB
# """

# create_empl_rate_table = """
# CREATE TABLE IF NOT EXISTS empl_rate (
#   id INTEGER PRIMARY KEY AUTO_INCREMENT,
#   emply_id INTEGER NOT NULL,
#   rate INTEGER,
#   FOREIGN KEY (emply_id) REFERENCES employees (id)
#   ) ENGINE = InnoDB
# """

# execute_query(connection, create_employees_table)
# execute_query(connection, create_position_table)
# execute_query(connection, create_department_table)
# execute_query(connection, create_emplposition_table)
# execute_query(connection, create_empldepart_table)
# execute_query(connection, create_empl_rate_table)
#
# # __________________________________________
#
# # 6. Create INSERT queries:
# create_employees = """
# INSERT INTO
#   employees (name, age, gender, nationality)
# VALUES
#   ('Emily Anderson', 34, 'Female', 'American'),
#   ('Rajesh Kapoor', 42, 'male', 'Indian'),
#   ('Maria Rodriguez', 29, 'female', 'Mexican'),
#   ('James Smith', 45, 'male', 'British'),
#   ('Chloe Martin', 30, 'female', 'French');
# """

# create_position = """
# INSERT INTO
#   position (name, salary)
# VALUES
#   ('Software Engineer', 7200),
#   ('Marketing Manager', 9167),
#   ('Financial Analyst', 6350),
#   ('Penetration Tester', 10250),
#   ('Human Resources Specialist', 5160);
# """

# create_department = """
# INSERT INTO
#   department (name, description)
# VALUES
#   ('Engineering/Development', 'The Engineering or Development department is responsible for designing, developing, and maintaining software applications and systems. Software engineers work on coding, debugging, testing, and ensuring the functionality and performance of software products.'),
#   ('Marketing', 'The Marketing department is in charge of promoting the companys products or services to the target audience. Marketing Managers oversee marketing strategies, campaigns, branding, and market research to attract and retain customers, increase brand awareness, and drive sales.'),
#   ('Finance', 'The Finance department is responsible for managing the companys financial resources, budgets, and investments. Financial Analysts evaluate financial data, create forecasts, analyze trends, and provide insights to support decision-making related to budgeting, investments, and financial planning.'),
#   ('Cybersecurity', 'The Cybersecurity department is focused on protecting the companys digital assets and data from cyber threats. Penetration Testers, also known as Ethical Hackers, are responsible for assessing the security of the organizations systems and networks by attempting to exploit vulnerabilities to identify and fix security weaknesses.'),
#   ('Human Resources (HR)', 'The HR department manages the companys workforce, including recruitment, employee relations, benefits administration, training, and development. Human Resources Specialists handle tasks such as hiring, onboarding, employee performance management, and ensuring compliance with labor laws and company policies.');
# """

# create_emplposition = """
# INSERT INTO
#   emplposition (emply_id, position_id)
# VALUES
#   (1, 1),
#   (2, 2),
#   (3, 3),
#   (4, 4),
#   (5, 5);
# """

# create_empldepart = """
# INSERT INTO
#   empldepart (emply_id, depart_id)
# VALUES
#   (1, 1),
#   (2, 2),
#   (2, 2),
#   (3, 3),
#   (4, 4),
#   (5, 5);
# """

# create_empl_rate = """
# INSERT INTO
#   empl_rate (emply_id, rate)
# VALUES
#   ( 1, 3),
#   ( 2, 3),
#   ( 3, 2),
#   ( 4, 5),
#   ( 5, 4);
# """
#
# execute_query(connection, create_employees)
# execute_query(connection, create_position)
# execute_query(connection, create_department)
# execute_query(connection, create_emplposition)
# execute_query(connection, create_empldepart)
# execute_query(connection, create_empl_rate)
#
# # __________________________________________
#
# 7. function for read the query same selection queries:
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
#
#
# # __________________________________________
#
#
# 8. Create SELECT queries:
# select_employees = "SELECT * FROM employees"
# employees = execute_read_query(connection, select_employees)

# if  employees:
#     for employee in employees:
#         print(employee)
# else:
#     print("No employees")

#
# # __________________________________________
#
#
# 9.  Create SELECT query with using condition 'Where' :
# Select_Female_employees = """
# SELECT * FROM
#     employees
# WHERE 
#     gender = 'Female' 
# AND
#     age > 30S
# """

# f_employyes = execute_read_query(connection, Select_Female_employees)

# if f_employyes:
#     for employee in f_employyes:
#         print(employee)
# else:
#     print("No employees found")

#
# # __________________________________________
#
#
# # 10. Create SELECT query with using condition 'Where' and 'Join' , and keyword 'AS' for alias a column name :
#
# select_emp_from_pos = """
# SELECT e.name AS EmployeeName, e.age AS Age, e.gender AS Gender, e.nationality AS Nationality, p.name AS Position, p.salary AS Salary 
# FROM employees AS e
# JOIN emplposition AS ep ON e.id = ep.emply_id
# JOIN position AS p ON ep.position_id = p.id
# JOIN empldepart AS ed ON e.id = ed.emply_id
# JOIN department AS d ON ed.depart_id = d.id
# WHERE d.name = 'Engineering/Development' AND p.salary > 2000;
# """
# select_emp_use_pos = execute_read_query(connection, select_emp_from_pos)

# if select_emp_use_pos:
#     for employee in select_emp_use_pos:
#         print(employee)
# else:
#     print("No employees found, we not have a Software Eng employees")

#
# # __________________________________________
#
#
# # 11. Create Update queries:
# update_emp_salary = """ 
#   UPDATE employees
#   SET
#     age = 30
#   WHERE
#     id = 3
# """
# execute_query( connection, update_emp_salary )
#
# 
# # __________________________________________
#
# Arabi Note:
# شكلي تحمست وطلع معي هالكود 
# اذا مافهمت الي سويته هنا اني خليته يتاكد اذا كان العمر 30 راح يطبع لي البيانات حسب العمر وراح يتحقق من العمر عن طريق رقم الاندكس
# للي بالدورة هذي مو اهداف الدورة نهائيا كل الي عليك تفهم السطر رقم 304,305 وتكون عارف تسوي لووب لطباعة
# وراح اترك لكم كود الطباعة الاساسي في السطر 311 - 315
############################################################################################################################################
# Let's we working now ;)
# # __________________________________________
## 13. Create Select query for check the result after update queries:
# SELECT_result_update = "SELECT * FROM employees "
# execute_select_update = execute_read_query(connection, SELECT_result_update)

## you can use this code for print with out check what is age for emploeey 

# if execute_select_update:
#     for employee in execute_select_update:
#         print(employee)
# else:
#     print("Not found employees")

# and you can this code for print and check if we have employee with age = 30

# if execute_select_update:
#     # Check if the result contains the employee with age 30 and id = 3
#     employee_found = False
#     for employee in execute_select_update:
#         if employee[0] == 3 and employee[2] == 30:  # Let's say the id is in the first column (index 0) , we want to verify the age and id, so the required index is 0 , 3  :)
#             print("Employee found:")
#             print("Employee ID:", employee[0])
#             print("Name:", employee[1])
#             print("Age:", employee[2])
#             print("Gender:", employee[3])
#             print("Nationality:", employee[4])
#             employee_found = True
#             break  
    
#     if not employee_found:
#         print("Employee with Age '30' and Id '3' not found")
# else:
#     print("No results found")

#
#
# # __________________________________________
#
#
## 12. Create Delete queries:
# delete_employee = "DELETE FROM employees WHERE id = 7"
# execute_query(connection, delete_employee)



# @s4crip ;)
