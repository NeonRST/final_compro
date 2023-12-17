import sys

import project_manage
import role_access
from csv_extract import CSV

run = True
while run:
    x = project_manage.login()
    run_system = x[0]
    user_sys = x[1]
    while run_system:
        user = role_access.Default
        if user_sys["role"] == "student":
            print("accessed as student")
            user = role_access.Student(user_sys)
            page1 = user.page1()
            student_edit = True
        if user_sys["role"] == "admin":
            print("accessed as Admin")
            user = role_access.Admin(user_sys)
            page1 = user.page_admin()
        if user_sys["role"] == "faculty":
            print("accessed as faculty")
            user = role_access.Faculty(user_sys)
            page1 = user.page_faculty()






