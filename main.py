#!/usr/bin/env python3

##This will be a python script that creates a command line journal
#This version will use Mysql

from datetime import datetime
import sqlite3


conn = sqlite3.connect('journal.db')

c = conn.cursor()

# c.execute("""CREATE TABLE pages (
#             date integer,
#             subject text,
#             entry text
#             )""")

# conn.commit()
#
# conn.close()


the_date = []
the_entry = []
create_option = ["C", "c"]
open_option = ["O", "o"]
exit_option = ["X", "x"]
select_option = ["S", 's']

get_date = datetime.now()

def create_entry():
    '''Gets inputs from user, appends it to a text file and reloads the menu'''
    global get_date
    subby = input("What's the Subject?: ")
    get_entry = input("What's on your mind?: ")
    the_entry.append(get_entry)
    entry = ''.join(the_entry)

    with conn:
        c.execute("INSERT INTO pages VALUES (:date, :subject, :entry)",
                  {'date': get_date.strftime("%x"), 'subject': subby, 'entry': entry})
    menu()

def open_journal():

    with conn:
        c.execute("SELECT * FROM pages")
        rows = c.fetchall()
        for row in rows:
            print(row[0], "-", row[1],)
    menu()

def select_entry():
    select_date = input("What date would you like to select?: ")
    with conn:
        c.execute("SELECT * FROM pages WHERE date=:date", {'date': select_date})
        rows = c.fetchall()
        for row in rows:
            print(row[0], row[1], row[2])
    menu()

def menu():
    global get_date
    print("Hello, Today is ", get_date.strftime("%x"), ".")
    print("To create a new journal entry type 'C'")
    print("To view your journal summery type 'O'")
    print("To select a journal entry type 'S'")
    print("To exit type 'X'")
    mims = input("What would you like to do?: ")
    if mims in create_option:
        create_entry()
    elif mims in open_option:
        open_journal()
    elif mims in select_option:
        select_entry()
    elif mims in exit_option:
        exit()
    else:
        print("Please type 'C' or 'O' :")
        menu()

menu()