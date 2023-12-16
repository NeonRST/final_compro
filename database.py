# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file
from csv_extract import CSV

login_data_raw = CSV('login.csv')
login_data_dict = CSV.csv_dict(login_data_raw)
person_data_raw = CSV('persons.csv')
person_data_dict = CSV.csv_dict(person_data_raw)
class Login:
    def __init__(self, login_data):
        self.login_data = login_data

    @property
    def login_data(self):
        return self.login_data

    @login_data.setter
    def login_data(self, _login_data):
        self.login_data = _login_data


class Persons:
    def __init__(self, person_data):
        self.person_data = person_data

    @property
    def person_data(self):
        return self.person_data

    @person_data.setter
    def person_data(self, person_data):
        self.person_data = person_data

# add in code for a Table class


class Project:
    def __init__(self, project_data):
        self.project_data = project_data

    @property
    def project_data(self):
        return self.project_data

    @project_data.setter
    def project_data(self, project_data):
        self.project_data = project_data



# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated