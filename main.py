import sys

import project_manage
import role_access
from csv_extract import CSV

run = True
while run:
    login_data = CSV('login.csv')
    login_data_list = CSV.csv_list(login_data)
    login_current_user = project_manage.login(login_data_list)
    role_allow = login_current_user[3]
    run_system = login_current_user[4]
    while run_system:
        user = role_access.Default
        student_edit = False
        if role_allow == "student":
            print("accessed as student")
            user = role_access.Student(login_current_user)
            student_edit = True
            page1 = user.page1()





