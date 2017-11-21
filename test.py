import sys, os, datetime

date = str(datetime.date.today())

dir_name = "D:/학업자료/pycharm/diary/"

filename = date + ".txt"

full_filename = dir_name + filename
print(full_filename)