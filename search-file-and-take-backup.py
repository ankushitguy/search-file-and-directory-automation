
#create a python script to iterate through text file line by line and display each line
#
import os
import sqlite3
import pandas as pd
import shutil

def get_file_path(data_file_name):
    clear_data_file_name = data_file_name.strip()
    conn = sqlite3.connect('file.db')
    cur = conn.cursor()
    # print(data_file_name)
    cur.execute("SELECT name,path FROM Files WHERE (name like '%{}%')".format(clear_data_file_name))
    rows = cur.fetchall()
    # print(rows)
    #create a new dictionary and add the key value pairs
    temp_list = []
    a_dict = {}
    destination = "<DESTINATION LOCATION>"
    if(len(rows)!=0):
        for row in rows:
            # temp_list.append(row[0])
            temp_list.append(row[1])
            # create directory if not exists
            shutil.copyfile(row[1], destination+row[0])
            
            # temp_dict[row[0]] = row[1]
    a_dict[clear_data_file_name] = temp_list

    # print(a_dict)
    return a_dict


# open file for reading
infile = open('FILE_NAMES_TO_SEARCH.txt', 'r')

# create a list of lines
lines = infile.readlines()

# close file
infile.close()

b_dict = {}
# display the lines
x=0
for line in lines:
    # with alive_bar(100,title=f'{x} - {line}') as bar:
    b_dict.update(get_file_path(line))
    print(f'{x} - {line}')
    x=x+1

df = pd.DataFrame.from_dict(b_dict, orient='index')
# print(df)

# save dictionary to csv file
df.to_csv('file_path.csv')

# save dictionary to excel file
# df.to_excel('file_path.xlsx')










