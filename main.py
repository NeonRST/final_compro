import sys
import project_manage
import role_access
from role_access import Student
from csv_extract import CSV

run = True
while run:
    login_data = CSV('login.csv')
    login_data_list = CSV.csv_list(login_data)
    login_user = project_manage.login(login_data_list)
    role_allow = login_user[3]
    run_system = login_user[4]
    if run_system:
        user = role_access.Default(login_user)
        if role_allow == "student":
            user = role_access.Student(user)




