# Final project for 2023's 219114/115 Programming I

# Dev Notes
* **info**
   - if for some reason the project has any problems what so ever pls contact me via DM in Discord (while pylint checking an error could have occur)
   - 
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
    - run main.py and use a user and is fine
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

| Role    | Action                                       | .csv access    | Class   | Completion |
|---------|----------------------------------------------|----------------|---------|-----------:|
| admin   | can add,delete,read all files in system      | all            | Admin   |        75% |
| student | create projects, check invites               | project.csv    | student |       100% |
| lead    | invite members, invites advisor, update data | project.csv    | student |       100% |
| member  | update data                                  | project.csv    | student |       100% |
| faculty | accept invites                               | none           | faculty |       100% |
| advisor | give opinions on proposals                   | project.csv    | faculty |       100% |


