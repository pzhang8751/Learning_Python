
from tkinter import *
import sqlite3

top = Tk()
top.title("House Rent Tracker")
top.geometry("900x600")
title = Label(top, text='House Rent Tracker', fg='red', font=('arial', 50, 'bold')).pack()

con = sqlite3.connect("House.db")
c = con.cursor()

Day = Label(top, font=('arial', 20, 'bold'), text='Day').place(x=150, y=100)
Month = Label(top, font=('arial', 20, 'bold'), text='Month').place(x=150, y=150)
Year = Label(top, font=('arial', 20, 'bold'), text='Year').place(x=150, y=200)
FirstLabel = Label(top, font=('arial', 20, 'bold'), text='First Name').place(x=150, y=250)
LastLabel = Label(top, font=('arial', 20, 'bold'), text='Last Name').place(x=150, y=300)
RentLabel = Label(top, font=('arial', 20, 'bold'), text='Rent Owed').place(x=150, y=350)
RentPaidLabel = Label(top, font=('arial', 20, 'bold'), text='Rent Paid').place(x=150, y=400)

house_number = StringVar(top)
house_number.set('----')

house_selector = StringVar(top)
house_selector.set('----')

homes = {'Number1101', 'Number1120', 'Number1002', 'Number1013', 'Number1260', 'Number1247'}

houseHome = OptionMenu(top, house_number, *homes).place(x=500, y=110)
HouseSelectors = OptionMenu(top, house_selector, *homes).place(x=700, y=265)

Day_D = StringVar(top)
Month_M = StringVar(top)
Year_Y = StringVar(top)
FirstName = StringVar(top)
LastName = StringVar(top)
RentOwed = StringVar(top)
RentPaid = StringVar(top)

day = Entry(top, textvariable=Day_D).place(x=300, y=110)
month = Entry(top, textvariable=Month_M).place(x=300, y=160)
year = Entry(top, textvariable=Year_Y).place(x=300, y=210)
First = Entry(top, textvariable=FirstName).place(x=300, y=260)
Last = Entry(top, textvariable=LastName).place(x=300, y=310)
RentO = Entry(top, textvariable=RentOwed).place(x=300, y=360)
RentP = Entry(top, textvariable=RentPaid).place(x=300, y=410)

def SubmittedResponse():
    bot = Tk()
    bot.title("Response Submitted")
    submitted_response = Label(bot, text='You have submitted a response.')
    submitted_response.pack()
    bot.mainloop()


def submit():

    c.execute(
        'CREATE TABLE IF NOT EXISTS ' + str(house_number.get()) +
        ' (Date TEXT, First_Name TEXT, Last_Name TEXT, Rent_Owed INTEGER, Rent_Paid INTEGER)')

    date = str(Month_M.get()) + "/" + str(Day_D.get()) + "/" + str(Year_Y.get())
    print(date)

    c.execute('INSERT INTO ' + house_number.get() + '(Date, First_Name, Last_Name, Rent_Owed, Rent_Paid) VALUES (?,?,?,?,?)', (date, FirstName.get(), LastName.get(), RentOwed.get(), RentPaid.get()))
    con.commit()

    house_number.set('----')
    Day_D.set('')
    Month_M.set('')
    Year_Y.set('')
    FirstName.set('')
    LastName.set('')
    RentPaid.set('')
    RentOwed.set('')

    SubmittedResponse()

def clear():
    house_number.set('----')
    Day_D.set('')
    Month_M.set('')
    Year_Y.set('')
    FirstName.set('')
    LastName.set('')
    RentPaid.set('')
    RentOwed.set('')

def DatatBase():
    right = Tk()
    right.geometry('400x175')
    right.title(str(house_selector.get()) + 'Database')
    c.execute('SELECT * FROM ' + str(house_selector.get()))

    frame = Frame(right)
    frame.place(x=0, y=0)
    Lb = Listbox(frame, height=100, width=150, font=("arial", 12))
    Lb.pack(side=LEFT, fill=Y)
    scroll = Scrollbar(frame, orient=VERTICAL)
    scroll.config(command=Lb.yview)
    scroll.pack(side=RIGHT, fill=Y)
    Lb.config(yscrollcommand=scroll.set)
    Lb.insert(0, 'Date, Name, Rent Owed, Rent Paid')
    data = c.fetchall()
    for row in data:
        Lb.insert(1, row)

    L7 = Label(right, text=house_selector.get() + '      ', font=("arial", 16)).place(x=400, y=100)

    right.mainloop()


SubmitButton = Button(top, fg='blue', font=10, text='  Submit  ', bg='white', command=submit).place(x=600, y=110)
ClearButton = Button(top, fg='red', font=10, text='  Clear  ', bg='white', command=clear).place(x=600, y=160)
OpenDB = Button(top, font=10, text='  Open DataBase  ', bg='white', command=DatatBase).place(x=500, y=260)

top.mainloop()