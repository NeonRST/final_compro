import sys
import project_manage
import datetime

class Default:
    def __init__(self):
        pass


class Student:
    def __init__(self, login_data_list, login_data_dict, project_data_list, project_data_dict,
                 member_pending_request_list, member_pending_request_dict, advisor_pending_request_list, advisor_pending_request_dict):
        self.login_data_list = login_data_list
        self.login_data_dict = login_data_dict
        self.project_data_list = project_data_list
        self.project_data_dict = project_data_dict
        self.member_pending_request_list = member_pending_request_list
        self.member_pending_request_dict = member_pending_request_dict
        self.advisor_pending_request_list = advisor_pending_request_list
        self.advisor_pending_request_dict = advisor_pending_request_dict

    def page1(self):
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
                print("3.check invites")
                print("4.exit")
                print("--------------------------")
                main_choose = int(input("input: "))
                page1_2 = True
                page1_1 = False
            while page1_2:
                if main_choose == 4:
                    sys.exit()
                if main_choose == 3:
                    for member_dict in self.member_pending_request_dict:
                        print(member_dict)
                        if self.login_data_list[0] == member_dict["to_be_member"]:
                            print(f"invite for project:" + " " + member_dict["ProjectID"] + " " + "by:" + " "
                                  + member_dict["Inviter"])
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
                        print("invite Member1 = 1")
                        print("invite Member2 = 2")
                        print("invite Advisor = 3")
                        print("change status = 4")
                        change_page_1_2_2 = input("input:")
                        if change_page_1_2_2 == "1":
                            member_code = input("member ID: ")
                            member1_invite = project_manage.Invite(access_project, self.login_data_list[0], member_code, "pending", datetime.date.today())
                            member1_invite.create_invite_member()
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








