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

    def csv_dict(self):
        return self.csv_dict

    def csv_list(self):
        return self.csv_list
