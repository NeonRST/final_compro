# import database module
import csv, os
from csv_extract import CSV

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

login_data = CSV('login.csv')
login_data_list = CSV.csv_list(login_data)
login_data_dict = CSV.csv_dict(login_data)
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
                    print(f"logged in as " + i["username"])
                    print(f"ID: " + i["ID"])
                    print(f"Role: " + i["role"])
                    return True, i
        print("login in failed")
        print()
        print("try again")
    # create all the corresponding tables for those csv files


class Project:
    def __init__(self, project_id_num=000, title="", lead_member="", member1="", member2="",
                 advisor=""):
        self.project_id_num = project_id_num
        self.title = title
        self.lead_member = lead_member
        self.member1 = member1
        self.member2 = member2
        self.advisor = advisor
        self.status = "pending"

    def create_project(self):
        print(project_data_dict)
        project_data_dict.append({'ProjectID': f"{self.project_id_num}",'Title': f"{self.title}",
                                'Lead': f"{self.lead_member}","Member1": f"{self.member1}",
                                  "Member2": f"{self.member2}","Advisor": f"{self.advisor}",
                                "Status": f"{self.status}"})
        file = open('project.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(['ProjectID','Title','Lead','Member1','Member2','Advisor','Status'])
        for dictionary in project_data_dict:
            writer.writerow(dictionary.values())
        file.close()


class Invite:
    def __init__(self, project_id, inviter, to_be,response,response_date):
        self.project_id = project_id
        self.inviter = inviter
        self.to_be_member = to_be
        self.to_be_advisor = to_be
        self.response = response
        self.response_date = response_date

    def create_invite_member(self):
        member_pending_request_dict.append({'ProjectID': f"{self.project_id}", 'Inviter': f"{self.inviter}",
                                  'to_be_member': f"{self.to_be_member}", "Response": f"{self.response}",
                                  "Response_date": f"{self.response_date}"})
        file = open('member_pending_request.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(["ProjectID","Inviter","to_be_member","Response","Response_date"])
        for dictionary in member_pending_request_dict:
            writer.writerow(dictionary.values())
        file.close()

    def create_invite_advisor(self):
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
    def __init__(self, project_id, status=""):
        self.project_id = project_id
        self.status = status

    def respond_invite_member(self):
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
                print(project_data_dict)
                if project_data_dict[i]["Member1"] == "None":
                    project_data_dict[i].update({"Member1": ans})
                elif project_data_dict[i]["Member2"] == "None":
                    project_data_dict[i].update({"Member2": ans})
                else:
                    print("project empty")
        file = open('project.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status'])
        for dictionary in project_data_dict:
            writer.writerow(dictionary.values())
        file.close()

    def respond_invite_advisor(self):
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
        writer.writerow(['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status'])
        for dictionary in project_data_dict:
            writer.writerow(dictionary.values())
        file.close()

    def respond_status(self):
        for i in range(len(project_data_dict)):
            if project_data_dict[i]["ProjectID"] == self.project_id:
                project_data_dict[i].update({"Status": self.status})
        file = open('project.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status'])
        for dictionary in project_data_dict:
            writer.writerow(dictionary.values())
        file.close()



# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [ID, role] if valid, otherwise returning None

# define a function called exit

def exits():
    pass

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
   
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

# initializing()
# val = login()

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id


