import sys
import project_manage


class Default:
    def __init__(self):
        pass


class Student:
    def __init__(self, login_data_list, login_data_dict, project_data_list, project_data_dict):
        self.login_data_list = login_data_list
        self.login_data_dict = login_data_dict
        self.project_data_list = project_data_list
        self.project_data_dict = project_data_dict

    def page1(self):
        print("hello")
        run = True
        page1_1 = True
        page1_2 = False
        page1_2_3 = False
        page1_2_2 = False
        page1_2_1 = False
        main_choose = 0
        while run:
            while page1_1:
                print("--------------------------")
                print("current projects:")
                for i in self.project_data_dict:
                    if self.login_data_list[0] in [i["Lead"], i["Member1"], i["Member2"]]:
                        print(f"ProjectID:" + " " + i["ProjectID"] + " " +
                              f"Title:" + " " + i["Title"] + " " +
                              f"Status" + " " + i["Status"])
                print("--------------------------")
                print("what would you like to do?")
                print("1.create new project")
                print("2.check current project status")
                print("3.exit")
                print("--------------------------")
                main_choose = int(input("input: "))
                page1_2 = True
                page1_1 = False
            while page1_2:
                if main_choose == 3:
                    sys.exit()
                if main_choose == 2:
                    access_project = input("enter code (ex.(PJ0)): ")
                    for project_dict in self.project_data_dict:
                        if project_dict["ProjectID"] == access_project:
                            print(project_dict["ProjectID"])
                            print(project_dict["Title"])
                            print(project_dict["Lead"])
                            print(project_dict["Member1"])
                            print(project_dict["Member2"])
                            print(project_dict["Advisor"])
                            print(project_dict["Status"])
                            page1_2_2 = True
                            page1_2 = False
                    while page1_2_2:
                        print("what would you like to change page 1_2_2")
                        print("invite Member1")
                        print("invite Member2")
                        print("invite Advisor")
                        print("change status")
                        change_page_1_2_2 = input("input:")
                        page1_2_2 = False

                if main_choose == 1:
                    project_id_num = f"PJ{len(self.project_data_list) + 1}"
                    title = input("Project title: ")
                    lead_member = self.login_data_list[0]
                    member1 = "none"
                    member2 = "none"
                    advisor = "none"
                    print("creation successful, pls restart program to access :)")
                    page1_2 = False
                    page1_1 = False
                    return False, [project_id_num, title, lead_member, member1, member2, advisor]
                    # project = project_manage.Project(project_id_num, title, lead_member, member1, member2, advisor)
                    # project.create_project()
                else:
                    return True, ""








