import sys

import project_manage
import role_access
from role_access import Student
from csv_extract import CSV

run = True
while run:
    login_data = CSV('login.csv')
    login_data_list = CSV.csv_list(login_data)
    login_data_dict = CSV.csv_dict(login_data)
    project_data = CSV('project.csv')
    project_data_list = CSV.csv_list(project_data)
    project_data_dict = CSV.csv_dict(project_data)
    login_current_user = project_manage.login(login_data_list)
    role_allow = login_current_user[3]
    run_system = login_current_user[4]
    while run_system:
        user = role_access.Default
        student_edit = False
        if role_allow == "student":
            print("accessed as student")
            user = role_access.Student(login_current_user, login_data_dict, project_data_list,
                                       project_data_dict)
            student_edit = True
        while student_edit:
            page1 = user.page1()
            if len(page1[1]) == 6:
                new_project_create = project_manage.Project(page1[1][0], page1[1][1], page1[1][2],
                                                            page1[1][3], page1[1][4], page1[1][5])
                new_project_create.create_project()
                student_edit = False
                page1 = role_access.Default




