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
                 advisor_pending_request_dict=_advisor_pending_request_dict,
                 person_data_dict=_project_data_dict):
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
        print("6.Exit:")
        admin_input_1 = input("input number here: ")
        if admin_input_1 == "6":
            sys.exit()
        if admin_input_1 == "1":
            print("what would you like to change?")
            print("1.Read all files:")
            print("2. Add a File")
            print("3. Delete a File")
            fl = input("what would you like to do?")
            if fl == "1":
                print()
                print()
                print(self.login_data_x)
                print()
                print()
            if fl == "2":
                print("type data you would like to add:")
                k1 = input("input a 7 digit ID (example.1234567)")
                while True:
                    if k1 in self.login_data_dict["ID"]:
                        print("this ID already exists")
                        print("please type a new ID")
                        k1 = input("input a 7 digit ID (example. Neon)")
                    else:
                        break
                k2 = input("input a username (example.1234567)")
                while True:
                    if k2 in self.login_data_dict["username"]:
                        print("this username already exists")
                        print("please type a new username")
                        k2 = input("input a new username (example. Neon1)")
                    else:
                        break
                k3 = input("input a password (example.123456789)")
                print("roles available right now (admin, student, faculty): ")
                k4 = input("what role would you like this user to have?: ")
                temp_login_data = project_manage.AddLogin(k1, k2, k3, k4)
                temp_login_data.create_data()
            if fl == "3":
                print("what data would you like to delete:")
                delete_login = input("enter the ID you would like to delete")
                login_del = project_manage.AddLogin(delete_login)
                login_del.delete_data()
        if admin_input_1 == "2":
            print()
            print()
            print(self.person_data)
            print()
            print()
        if admin_input_1 == "3":
            print("what would you like to change?")
            print("1.Read all files:")
            print("2. Add a File")
            print("3. Delete a File")
            fl = input("what would you like to do?")
            if fl == "1":
                print()
                print()
                print(self.project_data_dict)
                print()
                print()
            if fl == "2":
                print("enter a valid ProjectID (ex.PJ69), also dont make duplicate ProjectIDs:")
                k1 = input("enter PJ: ")
                while True:
                    if k1 in self.project_data_dict["ProjectID"]:
                        print("this ProjectID already exists")
                        print("please type a new ID")
                        k1 = input("enter a valid ProjectID "
                                   "(ex.PJ69), also dont make duplicate ProjectIDs:")
                    else:
                        break
                k2 = input("input a Title: ")
                k3 = input("input Lead: ")
                k4 = input("input Member1: ")
                k5 = input("input Member2: ")
                k6 = input("input Advisor: ")
                k7 = input("input status: ")
                temp_project_data = project_manage.AddProject(k1, k2, k3, k4, k5, k6, k7)
                temp_project_data.create_data()
            if fl == "3":
                print("what data would you like to delete:")
                delete_project= input("enter the ID you would like to delete")
                project_del = project_manage.AddProject(delete_project)
                project_del.delete_data()
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
    def __init__(self, login_data_sys, login_data_dict=_login_data_dict,
                 project_data_dict=_project_data_dict
                 ,member_pending_request_dict=_member_pending_request_dict,
                 advisor_pending_request_dict=_advisor_pending_request_dict):
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
            status_student = ""
            while page1_1:
                print("--------------------------")
                print("current projects:")
                for i in self.project_data_dict:
                    if self.login_data["ID"] in [i["Lead"], i["Member1"], i["Member2"]]:
                        print(f"ProjectID:" + " " + i["ProjectID"] + " " +
                              f"Title:" + " " + i["Title"] + " " +
                              f"Status" + " " + i["Status"])
                        print("Project Proposal information: " + i["information"])
                    if self.login_data["ID"] == i["Lead"]:
                        status_student = "lead"
                    if self.login_data["ID"] in [i["Member1"], i["Member2"]]:
                        status_student = "member"
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
                    temp_invite_val = 0
                    for member_dict in self.member_pending_request_dict:
                        if (self.login_data["ID"] == member_dict["to_be_member"]
                                and member_dict["Response"] == "pending"):
                            temp_invite_val += 1
                            print(f"invite for project:" + " " + member_dict["ProjectID"]
                                  + " " + "by: "
                                  + member_dict["Inviter"])
                    page1_2_3 = True
                    while page1_2_3:
                        if temp_invite_val != 0:
                            edit_invite = input("which project would you like to accept?: ")
                            temp_com = project_manage.ConfirmInvite(edit_invite)
                            temp_com.respond_invite_member()
                        else:
                            print()
                            print("no invites")
                            print()
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
                            print("Project info: " + project_dict["information"])
                            print("Project Status: " + project_dict["Status"])
                            page1_2_2 = True
                            page1_2 = False
                    while page1_2_2:
                        if status_student == "lead":
                            print()
                            print("Your Role is: " + self.login_data["role"])
                            print("------------------------------")
                            print("Type 1 to invite Member:")
                            print("Type 2 to invite Advisor:")
                            print("Type 3 to change information:")
                            print("Type 4 to exit:")
                            print("------------------------------")
                            change_page_1_2_2 = input("input:")
                            if change_page_1_2_2 == "1":
                                member_code = input("member ID: ")
                                member1_invite = project_manage.Invite(access_project,
                                                                       self.login_data["ID"],
                                                                       member_code,
                                                                       "pending",
                                                                       datetime.date.today())
                                member1_invite.create_invite_member()
                            if change_page_1_2_2 == "2":
                                advisor_code = input("Advisor ID: ")
                                advisor_invite = project_manage.Invite(access_project,
                                                                       self.login_data["ID"],
                                                                       advisor_code,
                                                                       "pending",
                                                                       datetime.date.today())
                                advisor_invite.create_invite_advisor()
                            if change_page_1_2_2 == "3":
                                new_info = input("what would you like to rewrite: ")
                                info = project_manage.NewInformation(access_project, new_info)
                                info.change_info()
                            if change_page_1_2_2 == "4":
                                sys.exit()
                            page1_2_2 = False
                        if status_student == "member":
                            print()
                            print("Your Role is: " + self.login_data["role"])
                            print("------------------------------")
                            print("Type 1 to change information:")
                            print("Type 2 to exit:")
                            print("------------------------------")
                            change_page_1_2_2 = input("input:")
                            if change_page_1_2_2 == "1":
                                new_info = input("what would you like to rewrite: ")
                                info = project_manage.NewInformation(access_project, new_info)
                                info.change_info()
                            if change_page_1_2_2 == "1":
                                sys.exit()

                if main_choose == 1:
                    project_id_num = f"PJ{len(self.project_data_dict) + 1}"
                    title = input("Project title: ")
                    basic_info = input("what will this project be about: ")
                    lead_member = self.login_data["ID"]
                    member1 = "None"
                    member2 = "None"
                    advisor = "None"
                    print("creation successful, pls restart program to access :)")
                    new_project_create = project_manage.Project(project_id_num, title,
                                                                lead_member,
                                                                member1, member2,
                                                                advisor, basic_info)
                    new_project_create.create_project()
                    return False

                    # project = project_manage.Project(project_id_num, title, lead_member,
                    # member1, member2, advisor)
                    # project.create_project()
                else:
                    return True, ""


class Faculty:
    def __init__(self, login_data_sys, login_data_dict=_login_data_dict,
                 project_data_dict=_project_data_dict
                 , member_pending_request_dict=_member_pending_request_dict,
                 advisor_pending_request_dict=_advisor_pending_request_dict,
                 person_data_dict=_persons_data_dict):
        self.login_data = login_data_sys
        self.login_data_dict = login_data_dict
        self.project_data_dict = project_data_dict
        self.member_pending_request_dict = member_pending_request_dict
        self.advisor_pending_request_dict = advisor_pending_request_dict
        self.person_data_dict = person_data_dict

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
                if (self.login_data["ID"] == advisor_dict["to_be_advisor"] and
                        advisor_dict["Response"] == "pending"):
                    print(
                        f"invite for project:" + " " + advisor_dict["ProjectID"] + " " + "by:" + " "
                        + advisor_dict["Inviter"])
            page1_2_3 = True
            while page1_2_3:
                edit_invite = input("which project would you like to accept? (Example.PJ0)): ")
                temp_com = project_manage.ConfirmInvite(edit_invite)
                temp_com.respond_invite_advisor()
                page1_2_3 = False
        if main_choose == 2:
            for j in range(len(self.project_data_dict)):
                if self.login_data["ID"] == self.project_data_dict[j]["Advisor"]:
                    print("ProjectID: " + self.project_data_dict[j]["ProjectID"])
                    print("Title: " + self.project_data_dict[j]["Title"])
                    for i in self.person_data_dict:
                        if i["ID"] == self.project_data_dict[j]["Lead"]:
                            print("Lead Member: " + i["first"] + " " + i["last"])
                        if i["ID"] == self.project_data_dict[j]["Member1"]:
                            print("Member1: " + i["first"] + " " + i["last"])
                        if i["ID"] == self.project_data_dict[j]["Member2"]:
                            print("Member2: " + i["first"] + " " + i["last"])
                    print()
                    allow = input("Write opinion: ")
                    allow_edit = project_manage.ConfirmInvite(self.project_data_dict[j]["ProjectID"]
                                                              , allow)
                    allow_edit.respond_status()
        if main_choose == 3:
            sys.exit()







