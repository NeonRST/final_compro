# import database module
import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
# define a funcion called initializing

def initializing(_exit=True):
    while _exit:
        read_csv()

# here are things to do in this function:

    # create an object to read all csv files that will serve as a persistent state for this program


def read_csv():
    Users = []
    with open(os.path.join(__location__, 'login.csv')) as f:
        rows = csv.DictReader(f)
        for r in rows:
            Users.append(dict(r))
    data_list = []
    for i in Users:
        temp_list = []
        for key, val in i.items():
            temp_list.append(val)
        data_list.append(temp_list)
    return data_list

    # create all the corresponding tables for those csv files


def read_project():
    Projects = []
    with open(os.path.join(__location__, 'project.csv')) as f:
        rows = csv.DictReader(f)
        for r in rows:
            Projects.append(dict(r))
    data_list = []
    for i in Projects:
        temp_list = []
        for key, val in i.items():
            temp_list.append(val)
        data_list.append(temp_list)
    print(data_list)
    print(Projects)
    print("hello")
    return data_list


def read_Member_pending_request():
    Member_pending_requests = []
    with open(os.path.join(__location__, 'member_pending_request.csv')) as f:
        rows = csv.DictReader(f)
        for r in rows:
            Member_pending_requests.append(dict(r))
    data_list = []
    for i in Member_pending_requests:
        temp_list = []
        for key, val in i.items():
            temp_list.append(val)
        data_list.append(temp_list)
    return data_list

# define a funcion called login
userlist = initializing()


def login(user_csv):
    login_name = input("enter your name: ")
    login_password = input("enter your password: ")
    log = False
    pos = 0
    for i in user_csv:
        if login_name == i[1] and login_password == i[2]:
            log = True
            break
        pos += 1
    if not log:
        print("login in failed")
        return None
    if log:
        print("login in successful")
        print(f"logged in as {user_csv[pos][1]}")
        print(f"ID: {user_csv[pos][0]}")
        print(f"Role: {user_csv[pos][3]}")
        return {user_csv[pos][0]}, {user_csv[pos][3]}


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
