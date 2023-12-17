import sys
import project_manage
import datetime
from csv_extract import CSV

login_data = CSV('login.csv')
login_data_list_temp = CSV.csv_list(login_data)
_login_data_dict = CSV.csv_dict(login_data)
project_data = CSV('project.csv')
_project_data_dict = CSV.csv_dict(project_data)
member_pending_request = CSV('member_pending_request.csv')
_member_pending_request_dict = CSV.csv_dict(member_pending_request)
advisor_pending_request = CSV('advisor_pending_request.csv')
_advisor_pending_request_dict = CSV.csv_dict(advisor_pending_request)


class Default:
    def __init__(self):
        pass


class Student:
    def __init__(self, login_data_list, login_data_dict=_login_data_dict, project_data_dict=_project_data_dict
                 ,member_pending_request_dict=_member_pending_request_dict, advisor_pending_request_dict=_advisor_pending_request_dict):
        self.login_data_list = login_data_list
        self.login_data_dict = login_data_dict
        self.project_data_dict = project_data_dict
        self.member_pending_request_dict = member_pending_request_dict
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
                        if self.login_data_list[0] == member_dict["to_be_member"] and member_dict["Response"] == "pending":
                            print(f"invite for project:" + " " + member_dict["ProjectID"] + " " + "by:" + " "
                                  + member_dict["Inviter"])
                    page1_2_3 = True
                    while page1_2_3:
                        edit_invite = input("which project would you like to edit?")
                        temp_com = project_manage.ConfirmInvite(edit_invite)
                        temp_com.respond_invite_member()
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
                        print("invite Member = 1")
                        print("invite Advisor = 2")
                        print("change status = 3")
                        change_page_1_2_2 = input("input:")
                        if change_page_1_2_2 == "1":
                            member_code = input("member ID: ")
                            member1_invite = project_manage.Invite(access_project, self.login_data_list[0], member_code, "pending", datetime.date.today())
                            member1_invite.create_invite_member()
                        if change_page_1_2_2 == "2":
                            advisor_code = input("Advisor ID: ")
                            advisor_invite = project_manage.Invite(access_project,
                                                                   self.login_data_list[0],
                                                                   advisor_code, "pending",
                                                                   datetime.date.today())
                            advisor_invite.create_invite_advisor()
                        if change_page_1_2_2 == "3":
                            pass
                        page1_2_2 = False

                if main_choose == 1:
                    project_id_num = f"PJ{len(self.project_data_dict) + 1}"
                    title = input("Project title: ")
                    lead_member = self.login_data_list[0]
                    member1 = "none"
                    member2 = "none"
                    advisor = "none"
                    print("creation successful, pls restart program to access :)")
                    page1_2 = False
                    page1_1 = False
                    new_project_create = project_manage.Project(project_id_num, title,
                                                                lead_member,
                                                                member1, member2,
                                                                advisor)
                    new_project_create.create_project()
                    return False


                    # project = project_manage.Project(project_id_num, title, lead_member, member1, member2, advisor)
                    # project.create_project()
                else:
                    return True, ""


# if val[1] = 'admin':
#     see and do admin related activities
# elif val[1] = 'student':
#     see and do student related activities
# elif val[1] = 'member':
#     see and do member related activities
# elif val[1] = 'lead':
#     see and do lead related activities
# elif val[1] = 'faculty':
#     see and do faculty related activities
# elif val[1] = 'advisor':
#     see and do advisor related activities

# once everyhthing is done, make a call to the exit function





