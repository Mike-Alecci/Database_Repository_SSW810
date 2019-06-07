import datetime
from prettytable import PrettyTable
import os

def practice_datetime():
    """This function just provides some simple examples of using Python's datetime module"""
    date1 = "Feb 27, 2000"
    date2 = "Feb 27, 2017"
    date3 = "Jan 1, 2017"
    date4 = "Oct 31, 2017"
    d1 = datetime.datetime.strptime(date1, '%b %d, %Y')
    d2 = datetime.datetime.strptime(date2, '%b %d, %Y')
    d3 = datetime.datetime.strptime(date3, '%b %d, %Y')
    d4 = datetime.datetime.strptime(date4, '%b %d, %Y')
    d5 = d1 + datetime.timedelta(days = 3)
    d6 = d2 + datetime.timedelta(days = 3)
    difference = d4 -d3
    d1_str = d1.strftime('%b %d, %Y')
    d2_str = d2.strftime('%b %d, %Y')
    d3_str = d3.strftime('%b %d, %Y')
    d4_str = d4.strftime('%b %d, %Y')
    d5_str = d5.strftime('%b %d, %Y')
    d6_str = d6.strftime('%b %d, %Y')
    print("3 days after {} is {}".format(d1_str, d5_str))
    print("3 days after {} is {}".format(d2_str, d6_str))
    print("{} occurs {} days before {}".format(d3_str, difference.days, d4_str))
    return None

practice_datetime()

def scanning_dir_files(dir_name):
    """This function scans all files in a given directory and provides a summary analysis of all .py files 
       contained within the directory, EG number of classes, functions, lines and characters"""
    pt = PrettyTable(field_names= ['File Name', 'Could Open', 'Classes', 'Functions', 'Lines', 'Characters'])
    list_to_test = list()
    try:
        file_list = os.listdir(path = dir_name)
        os.chdir(dir_name)
    except NotADirectoryError:
        print("Can't open the directory: {}".format(dir_name))
        return      #if we cant open the directory we want to stop immediately
    for f in file_list:
        if f.strip().endswith(".py"):
            file_name = f
            try:
                fp = open(f, 'r')
                could_open = "Yes"
            except FileNotFoundError:
                could_open = "No"
                print("Can't open file: {}".format(f)) 
            else:
                with fp:
                    cnt_class, cnt_function, cnt_lines, cnt_characters = 0, 0, 0, 0
                    for line in fp:
                        if line.strip().startswith("class "):
                            cnt_class += 1
                        elif line.strip().startswith("def "):
                            cnt_function += 1
                        cnt_characters += len(line)
                        cnt_lines += 1
            pt.add_row([file_name, could_open, cnt_class, cnt_function, cnt_lines, cnt_characters])
            list_to_test.append([file_name, could_open, cnt_class, cnt_function, cnt_lines, cnt_characters])
    print(pt)
    return list_to_test


