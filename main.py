import sys
import project_manage
import database

run = True

while run:
    login_data = database.CSV('login.csv')
    login_user = project_manage.login(login_data)
    project_data = database.CSV('project.csv')
    run_system = login_user[2]
    if run_system:
        print("what would you like to do?")
        print("--------------------------")
        print("1.create new project")
        print("2.check current project status")
        print("3.check invites")
        print("4.exit")
        print("--------------------------")
        choose_1 = int(input("input: "))
        if choose_1 == 4:
            sys.exit()
        if choose_1 == 1:
            project_id_num = f"00{len(project_data)}"
            title = input("Project title: ")
            lead_member = login_user[1]
            member1 = "none"
            member2 = "none"
            advisor = "none"
            project = project_manage.Project(project_id_num, title, lead_member, member1, member2, advisor)
            project.create_project()
            print("creation successful")

        if choose_1 == 2:
            pass
        print("check>")
        project_data = database.CSV("project.csv")
        print(project_data)
