# import database module
import csv, os
import database

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
# define a funcion called initializing

# def initializing(_exit=True):
#     while _exit:
#         read_csv()

# here are things to do in this function:

# create an object to read all csv files that will serve as a persistent state for this program


def login(user_csv):
    print("Senior project managing program")
    print()
    login_name = input("Username: ")
    login_password = input("Password: ")
    log = False
    pos = 0
    for i in user_csv:
        if login_name == i[1] and login_password == i[2]:
            log = True
            break
        pos += 1
    if not log:
        print()
        print("login in failed")
        return None
    if log:
        print()
        print("login in successful")
        print()
        print(f"logged in as {user_csv[pos][1]}")
        print(f"ID: {user_csv[pos][0]}")
        print(f"Role: {user_csv[pos][3]}")
        return {user_csv[pos][0]}, {user_csv[pos][3]}, True
    # create all the corresponding tables for those csv files


class Project:
    def __init__(self, project_id_num, title, lead_member, member1, member2, advisor):
        self.project_id_num = project_id_num
        self.title = title
        self.lead_member = lead_member
        self.member1 = member1
        self.member2 = member2
        self.advisor = advisor
        self.status = "pending"

    def create_project(self):
        data_to_append = [self.project_id_num, self.title, self.lead_member, self.member1, self.member2, self.advisor, self.status]
        file = open('project.csv', 'a', newline='')
        writer = csv.writer(file)
        writer.writerow(data_to_append)

    def pro_check(self, project_id):
        project_data = database.CSV('project.csv')
        for i in project_data:

# define a funcion called login


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
