"""This python file holds the classes for different users and the login system"""

# import database module
import csv
import os

from csv_extract import CSV

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# create all the corresponding tables for those csv files
login_data = CSV('login.csv')
login_data_list = CSV.csv_list(login_data)
login_data_dict = CSV.csv_dict(login_data)
person_data = CSV('persons.csv')
person_data_list = CSV.csv_list(login_data)
person_data_dict = CSV.csv_dict(login_data)
project_data = CSV('project.csv')
project_data_list = CSV.csv_list(project_data)
project_data_dict = CSV.csv_dict(project_data)
member_pending_request = CSV('member_pending_request.csv')
member_pending_request_list = CSV.csv_list(member_pending_request)
member_pending_request_dict = CSV.csv_dict(member_pending_request)
advisor_pending_request = CSV('advisor_pending_request.csv')
advisor_pending_request_list = CSV.csv_list(advisor_pending_request)
advisor_pending_request_dict = CSV.csv_dict(advisor_pending_request)


# define a function called login
def login():
    """this function logs you in"""
    print("Senior project managing program")
    print()
    # login_name = input("Username: ")
    # login_password = input("Password: ")
    while True:
        log = False
        login_name = input("Username: ")
        login_password = input("Password: ")
        for i in login_data_dict:
            if login_name == i["username"] and login_password == i["password"]:
                log = True
                if log:
                    print()
                    print("login in successful")
                    print()
                    print("logged in as " + i["username"])
                    print("ID: " + i["ID"])
                    print("Role: " + i["role"])
                    return True, i
        print("login in failed")
        print()
        print("try again")


class Project:
    """class for project objects"""
    def __init__(self, project_id_num=000, title="", lead_member="", member1="", member2="",
                 advisor="", information=""):
        self.project_id_num = project_id_num
        self.title = title
        self.lead_member = lead_member
        self.member1 = member1
        self.member2 = member2
        self.advisor = advisor
        self.status = "pending"
        self.information = information

    def create_project(self):
        """create project"""
        project_data_dict.append({'ProjectID': f"{self.project_id_num}",'Title': f"{self.title}",
                                'Lead': f"{self.lead_member}","Member1": f"{self.member1}",
                                  "Member2": f"{self.member2}","Advisor": f"{self.advisor}",
                                "Status": f"{self.status}", 'information': f"{self.information}"})
        file = open('project.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status',
                         'information'])
        for dictionary in project_data_dict:
            writer.writerow(dictionary.values())
        file.close()

    def get_info(self):
        return self.information


class Invite:
    """class for confirmation object"""
    def __init__(self, project_id, inviter, to_be,response,response_date):
        self.project_id = project_id
        self.inviter = inviter
        self.to_be_member = to_be
        self.to_be_advisor = to_be
        self.response = response
        self.response_date = response_date

    def create_invite_member(self):
        """method for inviting members"""
        (member_pending_request_dict.
         append({'ProjectID': f"{self.project_id}", 'Inviter': f"{self.inviter}",
                 'to_be_member': f"{self.to_be_member}",
                 "Response": f"{self.response}", "Response_date": f"{self.response_date}"}))
        file = open('member_pending_request.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(["ProjectID","Inviter","to_be_member","Response","Response_date"])
        for dictionary in member_pending_request_dict:
            writer.writerow(dictionary.values())
        file.close()

    def create_invite_advisor(self):
        """method for inviting advisors"""
        advisor_pending_request_dict.append(
            {'ProjectID': f"{self.project_id}", 'Inviter': f"{self.inviter}",
             'to_be_advisor': f"{self.to_be_advisor}", "Response": f"{self.response}",
             "Response_date": f"{self.response_date}"})
        file = open('advisor_pending_request.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(["ProjectID", "Inviter", "to_be_advisor", "Response", "Response_date"])
        for dictionary in advisor_pending_request_dict:
            writer.writerow(dictionary.values())
        file.close()


class ConfirmInvite:
    """class for invite confirmation"""
    def __init__(self, project_id, status=""):
        self.project_id = project_id
        self.status = status

    def respond_invite_member(self):
        """respond from invite by lead member"""
        for i in range(len(member_pending_request_dict)):
            if member_pending_request_dict[i]["ProjectID"] == self.project_id:
                ans = input("enter accepted or denied: ")
                member_pending_request_dict[i].update({"Response": ans})
        file = open('member_pending_request.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(["ProjectID", "Inviter", "to_be_member", "Response", "Response_date"])
        for dictionary in member_pending_request_dict:
            writer.writerow(dictionary.values())
        file.close()
        #update data
        for i in range(len(project_data_dict)):
            print(project_data_dict[i]["ProjectID"])
            if project_data_dict[i]["ProjectID"] == self.project_id:
                ans = input("enter Your ID to confirm (ex.1111111): ")
                if project_data_dict[i]["Member1"] == "None":
                    project_data_dict[i].update({"Member1": ans})
                elif project_data_dict[i]["Member2"] == "None":
                    project_data_dict[i].update({"Member2": ans})
                else:
                    print("project empty")
        file = open('project.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor',
                         'Status', 'information'])
        for dictionary in project_data_dict:
            writer.writerow(dictionary.values())
        file.close()

    def respond_invite_advisor(self):
        """respond to invite from student"""
        for i in range(len(advisor_pending_request_dict)):
            if advisor_pending_request_dict[i]["ProjectID"] == self.project_id:
                ans = input("enter accepted or denied: ")
                advisor_pending_request_dict[i].update({"Response": ans})
        file = open('advisor_pending_request.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(["ProjectID", "Inviter", "to_be_advisor", "Response", "Response_date"])
        for dictionary in advisor_pending_request_dict:
            writer.writerow(dictionary.values())
        file.close()
        #update data
        for i in range(len(project_data_dict)):
            if project_data_dict[i]["ProjectID"] == self.project_id:
                ans = input("enter Your ID to confirm (ex.1111111): ")
                print(project_data_dict)
                if project_data_dict[i]["Advisor"] == "None":
                    project_data_dict[i].update({"Advisor": ans})
                else:
                    print("advisor full")
        file = open('project.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status',
                         'information'])
        for dictionary in project_data_dict:
            writer.writerow(dictionary.values())
        file.close()

    def respond_status(self):
        """respond to request"""
        for i in range(len(project_data_dict)):
            if project_data_dict[i]["ProjectID"] == self.project_id:
                project_data_dict[i].update({"Status": self.status})
        file = open('project.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status',
                         'information'])
        for dictionary in project_data_dict:
            writer.writerow(dictionary.values())
        file.close()


class AddLogin:
    """login data adder"""
    def __init__(self, userid, username="", userpassword="", userrole=""):
        self.userid = userid
        self.username = username
        self. userpassword = userpassword
        self.userrole = userrole

    def create_data(self):
        """create data"""
        login_data_dict.append({'ID': f"{self.userid}", 'username': f"{self.username}",
                                  'password': f"{self.userpassword}", "role": f"{self.userrole}"})

        file = open('login.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(['ID', 'username', 'password', 'role'])
        file.close()

    def delete_data(self):
        """delete data"""
        for i in range(len(login_data_dict)):
            if login_data_dict[i]["ID"] == self.userid:
                login_data_dict[i].update({'ID': "", 'username': "",
                                           'password': "",
                                           "role": ""})

        file = open('login.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(['ID', 'username', 'password', 'role'])
        for dictionary in login_data_dict:
            writer.writerow(dictionary.values())
        file.close()


class AddProject:
    """class for adding data project"""
    def __init__(self, project_id, title, lead, member1, member2, advisor, status, information):
        self.project_id = project_id
        self.title = title
        self.lead = lead
        self.member1 = member1
        self.member2 = member2
        self.advisor = advisor
        self.status = status
        self.information = information

    def create_data(self):
        """create data"""
        project_data_dict.append({'ProjectID': f"{self.project_id}", 'Title': f"{self.title}",
                                  'Lead': f"{self.lead}", "Member1": f"{self.member1}",
                                  "Member2": f"{self.member2}", "Advisor": f"{self.advisor}",
                                  "Status": f"{self.status}", 'information': self.information})
        with open('project.csv', 'w', newline='') as file:
            writer = csv.writer(file)
        writer.writerow(['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status',
                         'information'])
        for dictionary in project_data_dict:
            writer.writerow(dictionary.values())
        file.close()

    def delete_data(self):
        """delete dat from project data"""
        project_data_dict_size = len(project_data_dict)
        for i in range(project_data_dict_size):
            if project_data_dict[i]["ProjectID"] == self.project_id:
                project_data_dict[i].update(
                    {'ProjectID': "", 'Title': "",
                     'Lead': "", "Member1": "",
                     "Member2": "", "Advisor": "",
                     "Status": ""})
        with open('project.csv', 'w', newline='') as file:
            writer = csv.writer(file)
        writer.writerow(['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status',
                         'information'])
        for dictionary in project_data_dict:
            writer.writerow(dictionary.values())
        file.close()


class NewInformation:
    """class for adding new info"""
    def __init__(self, pj_id, new_info):
        """init for this class"""
        self.pj_id = pj_id
        self.new_info = new_info

    def change_info(self):
        """change info for project"""
        project_data_dict_size = len(project_data_dict)
        for i in range(project_data_dict_size):
            if project_data_dict[i]["ProjectID"] == self.pj_id:
                project_data_dict[i].update({"information": self.new_info})
        file = open('project.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status',
                         'information'])
        for dictionary in project_data_dict:
            writer.writerow(dictionary.values())
        file.close()

    def info_read(self):
        """getter for info"""
        return self.new_info
