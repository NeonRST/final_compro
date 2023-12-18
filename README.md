# Final project for 2023's 219114/115 Programming I
   - Senior project managing program

# Dev Notes
* **info**
   - if for some reason the project has any problems whatsoever please get in touch with me via DM in Discord (while pylint checking an error could have occurred)
   - the system is functional to some degree, but loopholes could be present due to time constraints not all bugs were accounted for (pls comment the errors or problems in private comments in GC)
   - the function names are self-explanatory so i did not put much information in this readme file 
   - if you have any questions concerning the code contact me via DM
# List of Files
 * **Python Files**
     - **main.py**
         - Main file to run 
     - **project_manage.py**
         - `class Project` (creates projects)
         - `class Invite` (creates invites)
         - `class ConfirmInvite` (Confirm invites)
     - **csv_extract.py**
         - `class CSV` (extract CSV files)
     - **allow_access.py**
         - `class Admin` (main functions for admin)
         - `class Student` (main functions for students)
         - `class Faculty` (main functions for Faculty)

* **CSV Files**
    - `persons.csv`
    - `login.csv`
    - `Advisor_pending_request.csv`
    - `Member_pending_request.csv`
    - `Project.csv`

* **How to run my project**
    - run main.py and use a user from the list below for easy access
    - the system does not support real time updates, so you will have to rerun the file and exit everytime you make changes to the .csv files
    * **test users**
    - 0000000,a,1,student
    - 1111111,b,1,student
    - 2222222,r,1,admin
    - 3333333,e,1,faculty

# All CLasses and Method
* **main.py**
  - this file is used to run the program by determining role access based on login data
  - Student
  - USER = role_access.Student(user_sys)  
  - 
  - Admin
  - USER = role_access.Admin(user_sys)
  - 
  - Faculty
  - USER = role_access.Faculty(user_sys)

* **csv_extract.py**
  - this file is used to extract .csv data
  - 
  | Role/Type       | Action                | Method                       | Class | Completion |
  |-----------------|-----------------------|------------------------------|-------|-----------:|
  | System          | Object Constructor    | def __init__(self, csv_file) | CSV   |       100% |
  | System          | Return .csv in a dict | def csv_dict(self)           | CSV   |       100% |
  | System          | Return .csv in a list | def csv_list(self):          | CSV   |       100% |


 **project_manage.py**
  - this file is used for storing the different classes for different uses
  - 
  | Role/Type | Action                                                          | Method/Function                                                                                                      | Class            | Completion |
  |-----------|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|------------------|-----------:|
  | System    | checks username and password from the .csv to grant user access | def login():                                                                                                         | None             |       100% |
  | student   | Object Constructor for Projects                                 | def __init__(self, project_id_num=000, title="", lead_member="", member1="", member2="",advisor="", information=""): | Project          |       100% |
  | student   | adding information to project.csv files                         | def create_project(self):                                                                                            | Project          |       100% |
  | student   | Object Constructor for invites                                  | def __init__(self, project_id, inviter, to_be,response,response_date):                                               | Invite           |       100% |
  | student   | adding information to member_pending_request.csv files          | def create_invite_member(self):                                                                                      | Invite           |       100% |
  | student   | adding information to advisor_pending_request.csv files         | def create_invite_advisor(self):                                                                                     | Invite           |       100% |
  | faculty   | Object Constructor for ConfirmInvite                            | def __init__(self, project_id, status=""):                                                                           | ConfirmInvite    |       100% |
  | faculty   | confirming member_pending_request.csv files                     | def respond_invite_member(self):                                                                                     | ConfirmInvite    |       100% |
  | faculty   | confirming advisor_pending_request.csv files                    | def respond_invite_advisor(self):                                                                                    | ConfirmInvite    |       100% |
  | faculty   | typing opinion for projects                                     | def respond_status(self):                                                                                            | ConfirmInvite    |       100% |
  | admin     | Object Constructor for AddLogin                                 | def __init__(self, userid, username="", userpassword="", userrole=""):                                               | AddLogin         |       100% |
  | admin     | creates data for login.csv                                      | def create_data(self):                                                                                               | AddLogin         |       100% |
  | admin     | delete data for login.csv                                       | def delete_data(self):                                                                                               | AddLogin         |       100% |
  | admin     | Object Constructor for AddProject                               | def __init__(self, project_id, title, lead, member1, member2, advisor, status, information):                         | AddProject       |       100% |
  | admin     | create data                                                     | def create_data(self):                                                                                               | AddProject       |       100% |
  | admin     | delete data                                                     | def delete_data(self):                                                                                               | AddProject       |       100% |
  | admin     | Object Constructor for NewInformation                           | def __init__(self, pj_id, new_info):                                                                                 | NewInformation   |       100% |
  | admin     | info updater                                                    | def change_info(self):                                                                                               | NewInformation   |       100% |
  | admin     | info getter                                                     | def info_read(self):                                                                                                 | NewInformation   |       100% |

# Missing feature 
  - #### Let member able to leave group.
  - #### Letting admins change the user invite rows in .csv files
  - ### three member evaluation for confirmation

