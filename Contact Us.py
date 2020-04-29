import tkinter

top = tkinter.Tk()

def printName():
    import tkinter

    bot = tkinter.Tk()

    FirstText = FirstEntry.get()
    FirstName = tkinter.Label(bot, bg='white', text='First Name: ' + FirstText)
    FirstName.pack()

    LastText = LastEntry.get()
    LastName = tkinter.Label(bot, bg='white', text = 'Last Name: ' + LastText)
    LastName.pack()

    EText = EEntry.get()
    Email = tkinter.Label(bot, bg='white', text='E-mail: ' + EText)
    Email.pack()

    BusinessText= BusinessEntry.get()
    Business = tkinter.Label(bot, bg='white', text='Business Phone: ' + BusinessText)
    Business.pack()

    CompanyText = CompanyEntry.get()
    Company = tkinter.Label(bot, bg='white', text='Company/Name: ' + CompanyText)
    Company.pack()

    JobText = JobEntry.get()
    Job = tkinter.Label(bot, bg='white', text= 'Job Title: ' + JobText)
    Job.pack()

    AddressText = AddressEntry.get()
    Address = tkinter.Label(bot, bg='white', text='Address: ' + AddressText)
    Address.pack()

    CityText = CityEntry.get()
    City = tkinter.Label(bot, bg='white', text='City: ' + CityText)
    City.pack()

    StateText = StateEntry.get()
    State = tkinter.Label(bot, bg='white', text='State/Province: ' + StateText)
    State.pack()

    ZipText = ZipEntry.get()
    Zip = tkinter.Label(bot, bg='white', text='Zip/Postal Code: ' + ZipText)
    Zip.pack()

    CountryText = CountryEntry.get()
    Country = tkinter.Label(bot, bg='white', text='Country/Region : ' + CountryText)
    Country.pack()

    TopicText = TopicEntry.get()
    Topic = tkinter.Label(bot, bg='white', text='Topic: ' + TopicText)
    Topic.pack()

    bot.mainloop()


FirstLabel = tkinter.Label(top, bg='white', text='First Name')
FirstLabel.pack()
FirstEntry = tkinter.Entry(top)
FirstEntry.pack()

LastLabel = tkinter.Label(top, bg='white', text='Last Name')
LastLabel.pack()
LastEntry = tkinter.Entry(top)
LastEntry.pack()

ELabel = tkinter.Label(top, bg='white', text='E-mail')
ELabel.pack()
EEntry = tkinter.Entry(top)
EEntry.pack()

BusinessLabel = tkinter.Label(top, bg='white', text='Business Phone')
BusinessLabel.pack()
BusinessEntry = tkinter.Entry(top)
BusinessEntry.pack()

CompanyLabel = tkinter.Label(top, bg='white', text='Company/Name')
CompanyLabel.pack()
CompanyEntry = tkinter.Entry(top)
CompanyEntry.pack()

JobLabel = tkinter.Label(top, bg='white', text='Job Title')
JobLabel.pack()
JobEntry = tkinter.Entry(top)
JobEntry.pack()

AddressLabel = tkinter.Label(top, bg='white', text='Address')
AddressLabel.pack()
AddressEntry = tkinter.Entry(top)
AddressEntry.pack()

CityLabel = tkinter.Label(top, bg='white', text='City')
CityLabel.pack()
CityEntry = tkinter.Entry(top)
CityEntry.pack()

StateLabel = tkinter.Label(top, bg='white', text='State/Province')
StateLabel.pack()
StateEntry = tkinter.Entry(top)
StateEntry.pack()

ZipLabel = tkinter.Label(top, bg='white', text='Zip/Postal Code')
ZipLabel.pack()
ZipEntry = tkinter.Entry(top)
ZipEntry.pack()

CountryLabel = tkinter.Label(top, bg='white', text='Country/Region')
CountryLabel.pack()
CountryEntry = tkinter.Entry(top)
CountryEntry.pack()

TopicLabel = tkinter.Label(top, bg='white', text='Topic')
TopicLabel.pack()
TopicEntry = tkinter.Entry(top)
TopicEntry.pack()

SubmitButton = tkinter.Button(top, bg='white', text='Submit', command=printName)
SubmitButton.pack()

top.mainloop()