"""this module is used for CSV file extraction"""
import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class CSV:
    """class for .csv file types"""
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.csv_dict = []
        self.csv_list = []
        with open(os.path.join(__location__, self.csv_file)) as file:
            rows = csv.DictReader(file)
            for row in rows:
                self.csv_dict.append(dict(row))
        for i in self.csv_dict:
            temp_list = []
            for val in i.values():
                temp_list.append(val)
            self.csv_list.append(temp_list)

    def csv_dict(self):
        """returns csv_dict"""
        return self.csv_dict

    def csv_list(self):
        """returns csv_list"""
        return self.csv_list
