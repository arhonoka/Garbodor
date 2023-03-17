import csv
import os
from pprint import pprint

calendar_csv = '27-08-26.csv'
path = os.path.join(os.getcwd() , calendar_csv)

def create_SQL(list):
    # if data exists
    # update gabage_calender set ();

    # if data not exist
    # insert gabage_calender set ();
    pprint(list)

with open(path, encoding="sjis") as f:
    reader = csv.reader(f)
    row_list = [row for row in reader]

create_SQL(row_list)