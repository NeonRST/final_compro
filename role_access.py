import sys
import project_manage
import datetime
from csv_extract import CSV

login_data = CSV('login.csv')
login_data_list_temp = CSV.csv_list(login_data)
_login_data_dict = CSV.csv_dict(login_data)
persons_data = CSV("persons.csv")
_persons_data_dict = CSV.csv_dict(persons_data)
project_data = CSV('project.csv')
_project_data_dict = CSV.csv_dict(project_data)
member_pending_request = CSV('member_pending_request.csv')
_member_pending_request_dict = CSV.csv_dict(member_pending_request)
advisor_pending_request = CSV('advisor_pending_request.csv')
_advisor_pending_request_dict = CSV.csv_dict(advisor_pending_request)


class Default:
    def __init__(self):
        pass


class Admin:
    def __init__(self, login_data_sys, login_data_dict=_login_data_dict,
                 project_data_dict=_project_data_dict
                 , member_pending_request_dict=_member_pending_request_dict,
                 advisor_pending_request_dict=_advisor_pending_request_dict, person_data_dict=_project_data_dict):
        self.login_data = login_data_sys
        self.login_data_dict = login_data_dict
        self.person_data_dict = person_data_dict
        self.project_data_dict = project_data_dict
        self.member_pending_request_dict = member_pending_request_dict
        self.advisor_pending_request_dict = advisor_pending_request_dict

    @property
    def login_data_x(self):
        return self.login_data_dict

    @login_data_x.setter
    def login_data_x(self, new_data):
        self.login_data_dict = new_data

    @property
    def person_data(self):
        return self.person_data_dict

    @person_data.setter
    def person_data(self, new_data):
        self.project_data_dict = new_data

    @property
    def project_data(self):
        return _project_data_dict

    @project_data.setter
    def project_data(self, new_data):
        self.project_data_dict = new_data

    @property
    def member_invite_data(self):
        return self.member_pending_request_dict

    @member_invite_data.setter
    def member_invite_data(self, new_data):
        self.member_pending_request_dict = new_data

    @property
    def advisor_invite_data(self):
        return self.advisor_pending_request_dict

    @advisor_invite_data.setter
    def advisor_invite_data(self, new_data):
        self.advisor_pending_request_dict = new_data

    def page_admin(self):
        print("what would you like to do see")
        print("1.check all login data:")
        print("2.check all persons data:")
        print("3.check all project data:")
        print("4.check all member invite data:")
        print("5.check all advisor invite data:")
        admin_input_1 = input("input number here: ")
        if admin_input_1 == "1":
            print()
            print()
            print(self.login_data_x)
            print()
            print()
        if admin_input_1 == "2":
            print()
            print()
            print(self.person_data)
            print()
            print()
        if admin_input_1 == "3":
            print()
            print()
            print(self.project_data)
            print()
            print()
        if admin_input_1 == "4":
            print()
            print()
            print(self.member_pending_request_dict)
            print()
            print()
        if admin_input_1 == "5":
            print()
            print()
            print(self.advisor_pending_request_dict)
            print()
            print()

    def add(self):
        pass


class Student:
    def __init__(self, login_data_sys, login_data_dict=_login_data_dict, project_data_dict=_project_data_dict
                 ,member_pending_request_dict=_member_pending_request_dict, advisor_pending_request_dict=_advisor_pending_request_dict):
        self.login_data = login_data_sys
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
                    if self.login_data["ID"] in [i["Lead"], i["Member1"], i["Member2"]]:
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
                        if self.login_data["ID"] == member_dict["to_be_member"] and member_dict["Response"] == "pending":
                            print(f"invite for project:" + " " + member_dict["ProjectID"] + " " + "by:" + " "
                                  + member_dict["Inviter"])
                    page1_2_3 = True
                    while page1_2_3:
                        edit_invite = input("which project would you like to accept?: ")
                        temp_com = project_manage.ConfirmInvite(edit_invite)
                        temp_com.respond_invite_member()
                        page1_2_3 = False
                if main_choose == 2:
                    access_project = input("enter code (ex.(PJ0)): ")
                    for project_dict in self.project_data_dict:
                        if project_dict["ProjectID"] == access_project:
                            k1 = 0
                            k2 = 0
                            k3 = 0
                            print("ProjectID: " + project_dict["ProjectID"])
                            print("Project Title: " + project_dict["Title"])
                            for i in _persons_data_dict:
                                if i["ID"] == project_dict["Lead"]:
                                    print("Lead Member: " + i["first"] + " " + i["last"])
                                    k1 = 1
                            if k1 == 0:
                                print("Lead Member: None")
                            for i in _persons_data_dict:

                                if i["ID"] == project_dict["Member1"]:
                                    print("Member1: " + i["first"] + " " + i["last"])
                                    k2 = 1
                            if k2 == 0:
                                print("Member1: None")
                            for i in _persons_data_dict:

                                if i["ID"] == project_dict["Member2"]:
                                    print("Member2: " + i["first"] + " " + i["last"])
                                    k3 = 1
                            if k3 == 0:
                                print("Member2: None")
                            print("Advisor: " + project_dict["Advisor"])
                            print("Project Status: " + project_dict["Status"])
                            page1_2_2 = True
                            page1_2 = False
                    while page1_2_2:
                        print("Your Role is: " + self.login_data["role"])
                        print("what would you like to change page 1_2_2")
                        print("Type 1 to invite Member:")
                        print("Type 2 to invite Advisor:")
                        print("Type 3 to change status:")
                        change_page_1_2_2 = input("input:")
                        if change_page_1_2_2 == "1":
                            member_code = input("member ID: ")
                            member1_invite = project_manage.Invite(access_project, self.login_data["ID"], member_code, "pending", datetime.date.today())
                            member1_invite.create_invite_member()
                        if change_page_1_2_2 == "2":
                            advisor_code = input("Advisor ID: ")
                            advisor_invite = project_manage.Invite(access_project,
                                                                   self.login_data["ID"],
                                                                   advisor_code, "pending",
                                                                   datetime.date.today())
                            advisor_invite.create_invite_advisor()
                        if change_page_1_2_2 == "3":
                            pass
                        page1_2_2 = False
                if main_choose == 1:
                    project_id_num = f"PJ{len(self.project_data_dict) + 1}"
                    title = input("Project title: ")
                    lead_member = self.login_data["ID"]
                    member1 = "None"
                    member2 = "None"
                    advisor = "None"
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


class Faculty:
    def __init__(self, login_data_sys, login_data_dict=_login_data_dict,
                 project_data_dict=_project_data_dict
                 , member_pending_request_dict=_member_pending_request_dict,
                 advisor_pending_request_dict=_advisor_pending_request_dict):
        self.login_data = login_data_sys
        self.login_data_dict = login_data_dict
        self.project_data_dict = project_data_dict
        self.member_pending_request_dict = member_pending_request_dict
        self.advisor_pending_request_dict = advisor_pending_request_dict

    def page_faculty(self):
        print("--------------------------")
        print("what would you like to do?")
        print("1.check invites")
        print("2.view advising project")
        print("3.exit")
        print("--------------------------")
        main_choose = int(input("input: "))
        if main_choose == 1:
            for advisor_dict in self.advisor_pending_request_dict:
                if self.login_data["ID"] == advisor_dict["to_be_advisor"] and advisor_dict["Response"] == "pending":
                    print(
                        f"invite for project:" + " " + advisor_dict["ProjectID"] + " " + "by:" + " "
                        + advisor_dict["Inviter"])
            page1_2_3 = True
            while page1_2_3:
                edit_invite = input("which project would you like to accept?: ")
                temp_com = project_manage.ConfirmInvite(edit_invite)
                temp_com.respond_invite_advisor()
                page1_2_3 = False
        if main_choose == 2:
            for j in range(len(self.project_data_dict)):
                if self.login_data["ID"] == self.project_data_dict[j]["Advisor"]:
                    print("ProjectID: " + self.project_data_dict[j]["ProjectID"])
                    print("Title: " + self.project_data_dict[j]["Title"])
                    print("Lead Member: " + self.project_data_dict[j]["Lead"])
                    print("Member1: " + self.project_data_dict[j]["Member1"])
                    print("Member2: " + self.project_data_dict[j]["Member2"])
                    print()
                    allow = input("Write opinion: ")
                    allow_edit = project_manage.ConfirmInvite(self.project_data_dict[j]["ProjectID"]
                                                              , allow)
                    allow_edit.respond_status()
        if main_choose == 3:
            sys.exit()

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





