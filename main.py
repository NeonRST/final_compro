"""this is the main file for the senior project management system"""
import project_manage
import role_access

RUN = True
while RUN:
    x = project_manage.login()
    RUN_SYSTEM = x[0]
    user_sys = x[1]
    while RUN_SYSTEM:
        if user_sys["role"] == "student":
            print("Logged in as student")
            USER = role_access.Student(user_sys)
            USER.page1()
        if user_sys["role"] == "admin":
            print("Logged in as Admin")
            USER = role_access.Admin(user_sys)
            USER.page_admin()
        if user_sys["role"] == "faculty":
            print("Logged in as faculty")
            USER = role_access.Faculty(user_sys)
            USER.page_faculty()
