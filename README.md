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

* **How to run my project**
    - run main.py and use a user from the list below for easy access
    * **test users**
    - 0000000,a,1,student
    - 1111111,b,1,student
    - 2222222,r,1,admin
    - 3333333,e,1,faculty

* **CSV Files**
    - `persons.csv`
    - `login.csv`
    - `Advisor_pending_request.csv`
    - `Member_pending_request.csv`
    - `Project.csv`
  

| Role            | Action                  | Method                   | Class   | Completion |
|-----------------|-------------------------|--------------------------|---------|-----------:|
| admin           | get,set login data      | login_data_x             | Admin   |       100% |
| admin           | get,set person data     | person_data              | Admin   |       100% |
| admin           | get,set project         | project_data             | Admin   |       100% |
| admin           | get,set member_invite   | member_invite_data       | Admin   |       100% |
| admin           | get,set advisor_invite  | advisor_invite_data      | Admin   |       100% |
| admin           | admin UI                | page_admin               | Admin   |        70% |
| student         | student UI              | page1                    | Student |       100% |
| faculty/advisor | Faculty UI              | page_faculty             | Faculty |       100% |
| faculty/advisor | Return person_data_dict | read_person              | Faculty |       100% |


