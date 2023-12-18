# Final project for 2023's 219114/115 Programming I
# Final project for 2023's 219114/115 Programming I

* **List of Files**
    * **Python Files**
        - **main.py**
            - Main file to run 
        - **project_manage.py**
            - `class Project` (creates projects)
            - `class Invite` (creates invites)
            - `class ConfirmInvite` (Confirm invites)
        - **csv_extract.py**
            - `class CSV` (extract CSV files)

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