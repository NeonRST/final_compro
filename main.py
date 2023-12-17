import sys

import project_manage
import role_access
from csv_extract import CSV

run = True
while run:
    project_manage.login()
    role_allow = [3]
    run_system = [4]
    while run_system:
        user = role_access.Default
        student_edit = False
        if role_allow == "student":
            print("accessed as student")
            user = role_access.Student(login_current_user)
            student_edit = True
            page1 = user.page1()





