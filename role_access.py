import sys
import project_manage
from csv_extract import CSV
import database

class Default:
    def __init__(self, login_data):
        self.login_data = login_data


class Student(Default):
    def __init__(self, login_data, project_data_list, project_data_dict):
        super().__init__(login_data)
        self.project_data_list = project_data_list
        self.project_data_dict = project_data_dict

    def page1(self):
        print("what would you like to do?")
        print("--------------------------")
        print("current projects:")
        for i in self.project_data_list:
            if i[2] == self.login_data:
                print(f"projectID: {i[0]} Title: {i[1]}, Status {i[6]}")
        print("--------------------------")
        print("1.create new project")
        print("2.check current project status")
        print("3.exit")
        print("--------------------------")
        main_choose = int(input("input: "))
        if main_choose == 3:
            sys.exit()
        if main_choose == 2:
            access_project = input("enter code (ex.(PJ0))")
            for key, value in self.project_data_dict:
                if value == access_project:


        if main_choose == 1:
            project_id_num = f"PJ{len(self.project_data_list)}"
            title = input("Project title: ")
            lead_member = self.login_data[1]
            member1 = "none"
            member2 = "none"
            advisor = "none"
            project = project_manage.Project(project_id_num, title, lead_member, member1, member2, advisor)
            project.create_project()
            print("creation successful")









