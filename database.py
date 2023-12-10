# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file
import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class CSV:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.csv_dict = []
        self.csv_list = []
        with open(os.path.join(__location__, self.csv_file)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.csv_dict.append(dict(r))
        for i in self.csv_dict:
            temp_list = []
            for key, val in i.items():
                temp_list.append(val)
            self.csv_list.append(temp_list)


#
# x = CSV('login.csv')
# print(x.csv_list)

# add in code for a Database class

# add in code for a Table class

# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated