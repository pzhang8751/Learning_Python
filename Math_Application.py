
from tkinter import *
from math import *
from PIL import ImageTk, Image

class Math():
    def __init__(self):
        self.xLabel = 10
        self.xEntry = 275
        self.yOne = 25
        self.yTwo = 50
        self.yThree = 75
        self.yAnswer2 = 75
        self.yAnswer3 = 100
        self.CalculateButtonX = 200
        self.CalculateButtonY = 125
        self.clearButtonX = 300
        self.clearButtonY = 125
        self.home()

    def home(self):
        self.main = Tk()
        self.main.title('Math Applications')
        self.main.geometry("750x500")
        self.main.resizable(0,0)
        title = Label(self.main, text='Math Formulas', fg='red', font=('arial', 50, 'bold')).place(x=10,y=5)

        Choose_Label = Label(self.main, text="Pick a formula below and we'll solve it!", font=('arial', 25)).place(x=10,y=75)
        Choose_Label2 = Label(self.main, text='Formula:', font=('arial',20)).place(x=250,y=200)
        canvas = Canvas(self.main, width=92, height=125)
        canvas.place(x=600,y=20)
        img = ImageTk.PhotoImage(Image.open("calculator.png"))
        canvas.create_image(0, 0, anchor=NW, image=img)

        self.formula_entry = StringVar(self.main)
        formulas = {'Area of Square', 'Area of Rectangle', 'Area of Right Triangle', 'Area of Rhombus', 'Area of Circle'
                    , 'Perimeter of Square', 'Perimeter of Rectangle', 'Circumference of Circle', 'Exponential Decay',
                    'Exponential Growth', 'Annual Interest', 'Quadratic Formula', 'Arithmetic Sequence',
                    'Geometric Sequence', 'Distance Formula', 'Pythagorean Theorem', 'Volume of Cube/Rect-Prisim',
                    'Volume of Sphere', 'Surface Area of Cube/Rect-Prisim', 'Surface Area of Cylinder',
                    'Surface Area of Sphere', 'Midpoint Formula', 'Find Linear Equation'}
        Formula_OptionMenu = OptionMenu(self.main, self.formula_entry, *sorted(formulas)).place(x=375,y=205)
        SubmitButton = Button(self.main, fg='blue', font=10, text='  Submit  ', command=self.submit).place(x=350, y=300)
        self.main.mainloop()

    def clear_special_one_entry(self):
        self.Entry0.set('')
        self.answer.set('')

    def calculatearea_special_square(self):
        b = self.Entry0.get()
        if b == '':
            self.answer.set('Please enter a length')
        elif float(b)<0:
            self.answer.set('Can not have negative length')
        else:
            answer2 = float(b)**2
            self.answer.set(str(answer2))

    def Area_of_Square(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('350x125')
        self.a.resizable(0, 0)

        label1 = Label(self.a,text='Length of Side:').place(x=self.xLabel, y=25)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a,textvariable=self.Entry0).place(x=100,y=25)
        Label2 = Label(self.a, text='Area:').place(x=self.xLabel, y=self.yTwo)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=100, y=50)

        Calculate_Button = Button(self.a,text='calulate',command=self.calculatearea_special_square).place(x=25,y=75)
        Clear_Button = Button(self.a,text='clear',command=self.clear_special_one_entry()).place(x=150,y=75)
        self.a.mainloop()

    def clear_area(self):
        self.Entry0.set('')
        self.Entry2.set('')
        self.answer.set('')

    def calculatearea_rectangle(self):
        b = self.Entry0.get()
        c = self.Entry2.get()
        if b == '':
            self.answer.set('Please enter a length')
        elif c == '':
            self.answer.set('Please enter a width')
        elif float(b)<0 or float(c)<0:
            self.answer.set('Can not calculate with negative #(s)')
        else:
            answer2 = float(b)*float(c)
            self.answer.set(str(answer2))

    def Area_of_Rectangle(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('300x200')
        self.a.resizable(0,0)

        label1 = Label(self.a,text='Length of Rectangle').place(x=10,y=25)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a,textvariable=self.Entry0).place(x=125,y=25)
        label2 = Label(self.a,text='Width of Rectangle').place(x=10,y=50)
        self.Entry2 = StringVar(self.a)
        Entry3 = Entry(self.a,textvariable=self.Entry2).place(x=125,y=50)
        label3 = Label(self.a, text='Area').place(x=10,y=75)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=125, y=75)
        Calculate_Button = Button(self.a,text='calculate',command=self.calculatearea_rectangle).place(x=50,y=100)
        Clear_Button = Button(self.a,text='clear',command=self.clear_area).place(x=150,y=100)
        self.a.mainloop()

    def calculatearea_righttriangle(self):
        b = self.Entry0.get()
        c = self.Entry2.get()
        if b == '':
            self.answer.set('Please enter a base')
        elif c == '':
            self.answer.set('Please enter a height')
        elif float(b)<0 or float(c)<0:
            self.answer.set('Can not calculate with negative #(s)')
        else:
            answer2 = float(b)*float(c)*0.5
            self.answer.set(str(answer2))

    def Area_of_Right_Triangle(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('300x200')
        self.a.resizable(0, 0)

        label1 = Label(self.a,text='Base of Triangle:').place(x=10,y=25)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a,textvariable=self.Entry0).place(x=150,y=25)
        label2 = Label(self.a,text='Height of Triangle:').place(x=10,y=50)
        self.Entry2 = StringVar(self.a)
        Entry3 = Entry(self.a,textvariable=self.Entry2).place(x=150,y=50)
        label3 = Label(self.a, text='Area:').place(x=10,y=75)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=150,y=75)

        Calculate_Button = Button(self.a,text='calculate',command=self.calculatearea_righttriangle).place(x=50,y=125)
        Clear_Button = Button(self.a,text='clear',command=self.clear_area).place(x=150,y=125)
        self.a.mainloop()

    def calculatearea_rhombus(self):
        b = self.Entry0.get()
        c = self.Entry2.get()
        if b == '':
            self.answer.set('Please enter a length')
        elif c == '':
            self.answer.set('Please enter a width')
        elif float(b)<0 or float(c)<0:
            self.answer.set('Can not calculate with negative #(s)')
        else:
            answer2 = float(b)*float(c)
            self.answer.set(str(answer2))

    def Area_of_Rhombus(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('300x150')
        self.a.resizable(0,0)

        label1 = Label(self.a,text='Length of Rhombus:').place(x=10,y=25)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a,textvariable=self.Entry0).place(x=125,y=25)
        label2 = Label(self.a,text='Width of Rhombus:').place(x=10,y=50)
        self.Entry2 = StringVar(self.a)
        Entry3 = Entry(self.a,textvariable=self.Entry2).place(x=125,y=50)
        label3 = Label(self.a, text='Area:').place(x=10,y=75)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=125, y=75)
        Calculate_Button = Button(self.a, text='calculate', command=self.calculatearea_rhombus).place(x=50, y=100)
        Clear_Button = Button(self.a, text='clear', command=self.clear_area).place(x=150, y=100)
        self.a.mainloop()

    def calculatearea_circle(self):
        b = self.Entry0.get()
        if b == '':
            self.answer.set('Please enter a radius')
        elif float(b)<0:
            self.answer.set('Can not have negative radius')
        else:
            answer2 = pi*(float(b)**2)
            self.answer.set(str(answer2))

    def Area_of_Circle(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('300x150')
        self.a.resizable(0, 0)

        label1 = Label(self.a,text='Radius of Circle:').place(x=10,y=25)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a,textvariable=self.Entry0).place(x=110,y=25)
        Label2 = Label(self.a, text='Area:').place(x=10,y=50)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=110,y=50)

        Calculate_Button = Button(self.a,text='calculate',command=self.calculatearea_circle).place(x=50,y=100)
        Clear_Button = Button(self.a,text='clear',command=self.clear_special_one_entry).place(x=150,y=100)
        self.a.mainloop()

    def calculateperimeter_square(self):
        b = self.Entry0.get()
        if b == '':
            self.answer.set('Please enter a length')
        if float(b)<0:
            self.answer.set('Can not have negative length')
        else:
            answer2 = float(b)*4
            self.answer.set(str(answer2))

    def Perimeter_Square(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('300x150')
        self.a.resizable(0, 0)

        label1 = Label(self.a, text='Length of Side:').place(x=10,y=25)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a, textvariable=self.Entry0).place(x=110,y=25)
        Label2 = Label(self.a, text='Perimeter:').place(x=10,y=50)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=110, y=50)

        Calculate_Button = Button(self.a, text='calculate', command=self.calculateperimeter_square).place(x=50, y=100)
        Clear_Button = Button(self.a, text='clear', command=self.clear_special_one_entry()).place(x=150, y=100)
        self.a.mainloop()

    def calculateperimeter_rectangle(self):
        b = self.Entry0.get()
        c = self.Entry2.get()
        if b == '':
            self.answer.set('Please enter a length')
        elif c == '':
            self.answer.set('Please enter a width')
        elif float(b)<0 or float(c)<0:
            self.answer.set('Can not calculate with negative #(s)')
        else:
            answer2 = (float(b)*2)+(float(c)*2)
            self.answer.set(str(answer2))

    def Perimeter_of_Rectangle(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('300x150')
        self.a.resizable(0,0)

        label1 = Label(self.a,text='Length of Rectangle:').place(x=10,y=25)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a,textvariable=self.Entry0).place(x=125,y=25)
        label2 = Label(self.a,text='Width of Rectangle:').place(x=10,y=50)
        self.Entry2 = StringVar(self.a)
        Entry3 = Entry(self.a,textvariable=self.Entry2).place(x=125,y=50)
        label3 = Label(self.a, text='Perimeter:').place(x=10,y=75)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=125, y=75)
        Calculate_Button = Button(self.a,text='calculate',command=self.calculateperimeter_rectangle).place(x=50,y=100)
        Clear_Button = Button(self.a,text='clear',command=self.clear_area).place(x=150,y=100)

    def calculatecircumference_circle(self):
        b = self.Entry0.get()
        if b == '':
            self.answer.set('Please enter a radius')
        elif float(b)<0:
            self.answer.set('Can not have negative radius')
        else:
            answer2 = float(b)*2*pi
            self.answer.set(str(answer2))

    def Circumference_Circle(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('300x150')
        self.a.resizable(0, 0)

        label1 = Label(self.a, text='Radius:').place(x=10,y=25)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a, textvariable=self.Entry0).place(x=100,y=25)
        Label2 = Label(self.a, text='Circumference:').place(x=10,y=50)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=100, y=50)

        Calculate_Button = Button(self.a, text='calculate', command=self.calculatecircumference_circle).place(x=50, y=100)
        Clear_Button = Button(self.a, text='clear', command=self.clear_special_one_entry).place(x=150, y=100)
        self.a.mainloop()

    def clearExponentialGrowth_Decay(self):
        self.EntryOriginal.set('')
        self.Entry0.set('')
        self.Entry2.set('')
        self.answer.set('')

    def calculateexponential_decay(self):
        b = self.Entry0.get()
        c = self.Entry2.get()
        d = self.EntryOriginal.get()
        if d == '':
            self.answer.set('Please enter an original value')
        elif b == '':
            self.answer.set('Please enter a decay rate')
        elif c == '':
            self.answer.set('Please enter an amount of time')
        elif float(b)<0 or float(c)<0 or float(d)<0:
            self.answer.set('Can not calculate with negative #(s)')
        else:
            answer2 = ((1-(float(b)/float(100))) ** float(c)) * float(d)
            self.answer.set(str(answer2))

    def exponential_decay(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('350x175')
        self.a.resizable(0,0)

        originalLabel = Label(self.a, text='Original Value:').place(x=10,y=25)
        self.EntryOriginal = StringVar(self.a)
        OriginalEntry = Entry(self.a, textvariable=self.EntryOriginal).place(x=200,y=25)
        label1 = Label(self.a,text='Decay Rate Percentage (yearly):').place(x=10,y=50)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a,textvariable=self.Entry0).place(x=200,y=50)
        label2 = Label(self.a,text='Time Passed (year(s)):').place(x=10,y=75)
        self.Entry2 = StringVar(self.a)
        Entry3 = Entry(self.a,textvariable=self.Entry2).place(x=200,y=75)
        label3 = Label(self.a, text='Value after Time:').place(x=10,y=100)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=150, y=100)
        Calculate_Button = Button(self.a,text='calculate',command=self.calculateexponential_decay).place(x=50,y=125)
        Clear_Button = Button(self.a,text='clear',command=self.clearExponentialGrowth_Decay).place(x=150,y=125)

    def calculateexponential_growth(self):
        b = self.Entry0.get()
        c = self.Entry2.get()
        d = self.EntryOriginal.get()
        if d == '':
            self.answer.set('Please enter an original value')
        elif b == '':
            self.answer.set('Please enter a growth rate')
        elif c == '':
            self.answer.set('Please enter an amount of time')
        elif float(b)<0 or float(c)<0 or float(d)<0:
            self.answer.set('Can not calculate with negative #(s)')
        else:
            answer2 = ((1+(float(b)/float(100))) ** float(c)) * float(d)
            self.answer.set(str(answer2))

    def exponential_growth(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('350x175')
        self.a.resizable(0,0)

        originalLabel = Label(self.a, text='Original Value:').place(x=10,y=25)
        self.EntryOriginal = StringVar(self.a)
        OriginalEntry = Entry(self.a, textvariable=self.EntryOriginal).place(x=200,y=25)
        label1 = Label(self.a,text='Growth Rate Percentage (yearly):').place(x=10,y=50)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a,textvariable=self.Entry0).place(x=200,y=50)
        label2 = Label(self.a,text='Time Passed (year(s)):').place(x=10,y=75)
        self.Entry2 = StringVar(self.a)
        Entry3 = Entry(self.a,textvariable=self.Entry2).place(x=200,y=75)
        label3 = Label(self.a, text='Value after Time:').place(x=10,y=100)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=150, y=100)
        Calculate_Button = Button(self.a,text='calculate',command=self.calculateexponential_growth).place(x=50,y=125)
        Clear_Button = Button(self.a,text='clear',command=self.clearExponentialGrowth_Decay).place(x=150,y=125)

    def calculateannual_interest(self):
        b = self.Entry0.get()
        c = self.Entry2.get()
        d = self.EntryOriginal.get()
        if d == '':
            self.answer.set('Please enter an original value')
        elif b == '':
            self.answer.set('Please enter a interest rate')
        elif c == '':
            self.answer.set('Please enter an amount of time')
        elif float(b)<0 or float(c)<0 or float(d)<0:
            self.answer.set('Can not calculate with negative #(s)')
        else:
            answer2 = ((1 + (float(b) / float(100))) ** float(c)) * float(d)
            self.answer.set(str(answer2))

    def Annual_Interest(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('350x175')
        self.a.resizable(0, 0)

        originalLabel = Label(self.a, text='Original Value:').place(x=10,y=25)
        self.EntryOriginal = StringVar(self.a)
        OriginalEntry = Entry(self.a, textvariable=self.EntryOriginal).place(x=200,y=25)
        label1 = Label(self.a, text='Interest Rate (yearly):').place(x=10,y=50)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a, textvariable=self.Entry0).place(x=200,y=50)
        label2 = Label(self.a, text='Time Passed (year(s)):').place(x=10,y=75)
        self.Entry2 = StringVar(self.a)
        Entry3 = Entry(self.a, textvariable=self.Entry2).place(x=200,y=75)
        label3 = Label(self.a, text='Value after Time:').place(x=10,y=100)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=150,y=100)
        Calculate_Button = Button(self.a, text='calculate', command=self.calculateannual_interest).place(x=50, y=125)
        Clear_Button = Button(self.a, text='clear', command=self.clearExponentialGrowth_Decay).place(x=150, y=125)

    def calculatequad_formula(self):
        b = self.Entry0.get()
        c = self.Entry2.get()
        d = self.EntryOriginal.get()
        if d == '':
            self.answer.set('Please enter a value for a')
        elif b == '':
            self.answer.set('Please enter a value for b')
        elif c == '':
            self.answer.set('Please enter a value for c')
        else:
            answer2 = (-float(b) + sqrt((float(b)**2)-(4*float(c)*float(d))))/(2*float(d))
            answer3 = (-float(b) - sqrt((float(b)**2)-(4*float(c)*float(d))))/(2*float(d))
            self.answer.set(str(answer2)+' , '+str(answer3))

    def Quadratic_Formula(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('300x175')
        self.a.resizable(0, 0)

        originalLabel = Label(self.a, text="What is A's value?").place(x=10,y=25)
        self.EntryOriginal = StringVar(self.a)
        OriginalEntry = Entry(self.a, textvariable=self.EntryOriginal).place(x=150,y=25)
        label1 = Label(self.a, text="What is B's value?").place(x=10,y=50)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a, textvariable=self.Entry0).place(x=150,y=50)
        label2 = Label(self.a, text="What is C's value?").place(x=10,y=75)
        self.Entry2 = StringVar(self.a)
        Entry3 = Entry(self.a, textvariable=self.Entry2).place(x=150,y=75)
        label3 = Label(self.a, text="X's value(s)").place(x=10,y=100)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=150, y=100)
        Calculate_Button = Button(self.a, text='calculate', command=self.calculatequad_formula).place(x=50, y=125)
        Clear_Button = Button(self.a, text='clear', command=self.clearExponentialGrowth_Decay).place(x=150, y=125)

    def calculatearithemtic_sequence(self):
        d = self.EntryOriginal.get()
        b = self.Entry0.get()
        c = self.Entry2.get()
        if d == '':
            self.answer.set('Please enter a first term')
        elif b == '':
            self.answer.set('Please enter a common difference')
        elif c == '':
            self.answer.set('Please enter a term')
        else:
            answer2 = float(d) + (float(b)*(float(c)-1))
            self.answer.set(str(answer2))

    def Arithmetic_Sequence(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('500x175')
        self.a.resizable(0, 0)

        originalLabel = Label(self.a, text="What is the first term in the sequence (A(1)):").place(x=self.xLabel,y=self.yOne)
        self.EntryOriginal = StringVar(self.a)
        OriginalEntry = Entry(self.a, textvariable=self.EntryOriginal).place(x=self.xEntry,y=self.yOne)
        label1 = Label(self.a, text="What is the common difference of the sequence:").place(x=self.xLabel,y=self.yTwo)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a, textvariable=self.Entry0).place(x=self.xEntry,y=self.yTwo)
        label2 = Label(self.a, text="What term are you looking for:").place(x=self.xLabel,y=self.yThree)
        self.Entry2 = StringVar(self.a)
        Entry3 = Entry(self.a, textvariable=self.Entry2).place(x=self.xEntry,y=self.yThree)
        label3 = Label(self.a, text="Nth term's value is:").place(x=self.xLabel,y=self.yAnswer3)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=self.xEntry,y=self.yAnswer3)
        Calculate_Button = Button(self.a, text='calculate', command=self.calculatearithemtic_sequence).place(x=self.CalculateButtonX,y=self.CalculateButtonY)
        Clear_Button = Button(self.a, text='clear', command=self.clearExponentialGrowth_Decay).place(x=self.clearButtonX,y=self.clearButtonY)

    def calculategeometric_sequence(self):
        d = self.EntryOriginal.get()
        b = self.Entry0.get()
        c = self.Entry2.get()
        if d == '':
            self.answer.set('Please enter a first term')
        elif b == '':
            self.answer.set('Please enter a common ratio')
        elif c == '':
            self.answer.set('Please enter a term')
        else:
            answer2 = float(d) * (float(b)**(float(c)-1))
            self.answer.set(str(answer2))

    def Geometric_Sequence(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('400x175')
        self.a.resizable(0, 0)

        originalLabel = Label(self.a, text="What is the first term in the sequence (A(1))?").place(x=10,y=25)
        self.EntryOriginal = StringVar(self.a)
        OriginalEntry = Entry(self.a, textvariable=self.EntryOriginal).place(x=250,y=25)
        label1 = Label(self.a, text="What is the common ratio of the sequence?").place(x=10,y=50)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a, textvariable=self.Entry0).place(x=250,y=50)
        label2 = Label(self.a, text="What term are you looking for?").place(x=10,y=75)
        self.Entry2 = StringVar(self.a)
        Entry3 = Entry(self.a, textvariable=self.Entry2).place(x=250,y=75)
        label3 = Label(self.a, text="Nth term's value is:").place(x=10,y=100)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=200, y=100)
        Calculate_Button = Button(self.a, text='calculate', command=self.calculategeometric_sequence).place(x=50, y=125)
        Clear_Button = Button(self.a, text='clear', command=self.clearExponentialGrowth_Decay).place(x=150, y=125)

    def clearDistance(self):
        self.coordinate1_x_value.set('')
        self.coordinate1_y_value.set('')
        self.coordinate2_x_value.set('')
        self.coordinate2_y_value.set('')
        self.answer.set('')

    def calculatedistance_formula(self):
        x1 = self.coordinate1_x_value.get()
        y1 = self.coordinate1_y_value.get()
        x2 = self.coordinate2_x_value.get()
        y2 = self.coordinate2_y_value.get()
        if x1 == '':
            self.answer.set('Please enter the x coordinate for the first point')
        elif y1 == '':
            self.answer.set('Please enter the y coordinate for the first point')
        elif x2 == '':
            self.answer.set('Please enter the x coordinate for the second point')
        elif y2 == '':
            self.answer.set('Please enter the y coordinate for the second point')
        else:
            answer2 = sqrt((((float(x2)-float(x1))**2)+((float(y2)-float(y1))**2)))
            self.answer.set(str(answer2))

    def Distance_Formula(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('400x300')
        self.a.resizable(0, 0)

        coordinate1 = Label(self.a, text='Coordinate 1:').place(x=20,y=50)
        coordinate1_x = Label(self.a, text='X coordinate').place(x=125,y=25)
        coordinate1_y = Label(self.a, text='Y coordinate').place(x=250,y=25)
        self.coordinate1_x_value = StringVar(self.a)
        self.coordinate1_y_value = StringVar(self.a)
        coordinate1_x_entry = Entry(self.a, textvariable=self.coordinate1_x_value).place(x=100,y=50)
        coordinate1_y_entry = Entry(self.a, textvariable=self.coordinate1_y_value).place(x=225,y=50)
        coordinate2 = Label(self.a, text='Coordinate 2:').place(x=20,y=100)
        self.coordinate2_x_value = StringVar(self.a)
        self.coordinate2_y_value = StringVar(self.a)
        coordinate2_x_entry = Entry(self.a, textvariable=self.coordinate2_x_value).place(x=100, y=100)
        coordinate2_y_entry = Entry(self.a, textvariable=self.coordinate2_y_value).place(x=225, y=100)
        distanceLabel = Label(self.a, text='Distance between coordinates').place(x=125,y=125)
        self.answer = StringVar(self.a)
        answerLabel = Label(self.a, textvariable=self.answer).place(x=100, y=150)
        Calculate_Button = Button(self.a, text='  calculate  ', command=self.calculatedistance_formula).place(x=50,y=200)
        Clear_Button = Button(self.a, text='  clear  ', command=self.clearDistance).place(x=275, y=200)

    def clearA(self):
        self.leg1.set('')
        self.hypotenuse.set('')
        self.answer.set('')

    def calculateA(self):
        a = self.leg1.get()
        c = self.hypotenuse.get()
        if a =='':
            self.answer.set('Please enter a leg value')
        elif c =='':
            self.answer.set('Please enter a hypotenuse value')
        elif float(a)<0 or float(c)<0:
            self.answer.set("Can not solve with negative #(s)")
        else:
            answer2 = sqrt((float(c)**2)-(float(a)**2))
            self.answer.set(str(answer2))

    def A(self):
        self.b = Tk()
        self.b.geometry('350x175')
        self.b.resizable(0, 0)

        Leg1_label = Label(self.b, text="What is the other leg's value:").place(x=10,y=25)
        self.leg1 = StringVar(self.b)
        leg1Entry = Entry(self.b, textvariable=self.leg1).place(x=200,y=25)
        Hypotenuse_Label = Label(self.b, text="What is the hypotenuse's value:").place(x=10,y=50)
        self.hypotenuse = StringVar(self.b)
        hypotenuseEntry = Entry(self.b, textvariable=self.hypotenuse).place(x=200,y=50)
        answerLabel = Label(self.b,text='The other leg value is:').place(x=10,y=75)
        self.answer = StringVar(self.b)
        answerLabel = Label(self.b, textvariable=self.answer).place(x=200,y=75)
        Calculate_Button = Button(self.b, text='  calculate  ', command=self.calculateA).place(x=50,y=125)
        Clear_Button = Button(self.b, text='  clear  ', command=self.clearA).place(x=150,y=125)

    def calculateC(self):
        a = self.leg1.get()
        c = self.hypotenuse.get()
        if a == '':
            self.answer.set('Please enter a leg value')
        elif c == '':
            self.answer.set('Please enter a leg value')
        elif float(a) < 0 or float(c) < 0:
            self.answer.set("Can not solve with negative #(s)")
        else:
            answer2 = sqrt((float(c) ** 2) + (float(a) ** 2))
            self.answer.set(str(answer2))

    def C(self):
        self.b = Tk()
        self.b.geometry('350x175')
        self.b.resizable(0, 0)

        Leg1_label = Label(self.b, text="What is the first leg's value").place(x=10,y=25)
        self.leg1 = StringVar(self.b)
        leg1Entry = Entry(self.b, textvariable=self.leg1).place(x=200,y=25)
        Hypotenuse_Label = Label(self.b, text="What is the other leg's value").place(x=10,y=50)
        self.hypotenuse = StringVar(self.b)
        hypotenuseEntry = Entry(self.b, textvariable=self.hypotenuse).place(x=200,y=50)
        answerLabel = Label(self.b, text='The hypotenuse is').place(x=10,y=75)
        self.answer = StringVar(self.b)
        answerLabel = Label(self.b, textvariable=self.answer).place(x=200,y=75)
        Calculate_Button = Button(self.b, text='  calculate  ', command=self.calculateC).place(x=50,y=125)
        Clear_Button = Button(self.b, text='  clear  ', command=self.clearA).place(x=150,y=125)

    def Pythagorean_Theorem(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('175x110')
        self.a.resizable(0, 0)

        SolveAB = Button(self.a, text='Solve for A/B (leg)',command=self.A).place(x=10,y=10)

        SolveC = Button(self.a, text='Solve for C (hypotenuse)', command=self.C).place(x=10,y=60)

    def calculate_volumeCube(self):
        d = self.EntryOriginal.get()
        b = self.Entry0.get()
        c = self.Entry2.get()
        if d == '':
            self.answer.set('Please enter a height')
        elif b == '':
            self.answer.set('Please enter a width')
        elif c == '':
            self.answer.set('Please enter a length')
        elif float(d)<0 or float(b)<0 or float(c)<0:
            self.answer.set('Can not solve with negatives')
        else:
            answer2 = float(d) * float(b) * float(c)
            self.answer.set(str(answer2))

    def Volume_of_Cube(self):
        self.a = Tk()
        self.a.geometry('300x175')
        self.a.resizable(0, 0)
        self.a.title(self.formula_entry.get())

        originalLabel = Label(self.a, text="Height of 3D object:").place(x=10, y=25)
        self.EntryOriginal = StringVar(self.a)
        OriginalEntry = Entry(self.a, textvariable=self.EntryOriginal).place(x=150, y=25)
        label1 = Label(self.a, text="Width of 3D object:").place(x=10, y=50)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a, textvariable=self.Entry0).place(x=150, y=50)
        label2 = Label(self.a, text="Length of 3D object:").place(x=10, y=75)
        self.Entry2 = StringVar(self.a)
        Entry3 = Entry(self.a, textvariable=self.Entry2).place(x=150, y=75)
        label3 = Label(self.a, text="Volume of 3D object:").place(x=10, y=100)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=150, y=100)
        Calculate_Button = Button(self.a, text='calculate', command=self.calculate_volumeCube).place(x=50, y=125)
        Clear_Button = Button(self.a, text='clear', command=self.clearExponentialGrowth_Decay).place(x=150, y=125)

    def clearVolume(self):
        self.answer.set('')
        self.EntryOriginal.set('')
        self.Entry0.set('')

    def calculate_volumeCylinder(self):
        d = self.EntryOriginal.get()
        b = self.Entry0.get()
        if d == '':
            self.answer.set('Please enter a height')
        elif b == '':
            self.answer.set('Please enter a radius')
        elif float(d)<0 or float(b)<0:
            self.answer.set('can not solve with negatives')
        else:
            answer2 = float(d) * (float(b) ** 2 * pi)
            self.answer.set(str(answer2))

    def Volume_of_Cylinder(self):
        self.a = Tk()
        self.a.geometry('300x175')
        self.a.resizable(0, 0)
        self.a.title(self.formula_entry.get())

        originalLabel = Label(self.a, text="Height of Cylinder:").place(x=10, y=25)
        self.EntryOriginal = StringVar(self.a)
        OriginalEntry = Entry(self.a, textvariable=self.EntryOriginal).place(x=150, y=25)
        label1 = Label(self.a, text="Radius of Cylinder:").place(x=10, y=50)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a, textvariable=self.Entry0).place(x=150, y=50)
        label3 = Label(self.a, text="Volume of 3D object:").place(x=10, y=75)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=150, y=75)
        Calculate_Button = Button(self.a, text='calculate', command=self.calculate_volumeCylinder).place(x=50, y=125)
        Clear_Button = Button(self.a, text='clear', command=self.clearVolume).place(x=150, y=125)

    def calculateSphereVolume(self):
        b = self.Entry0.get()
        if b == '':
            self.answer.set('Please enter a radius')
        elif float(b)<0:
            self.answer.set('Can not solve with negative numbers')
        else:
            answer2 = (4/3) * ((float(b) ** 3) * pi)
            self.answer.set(str(answer2))

    def Volume_of_Sphere(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('300x150')
        self.a.resizable(0, 0)

        label1 = Label(self.a, text='Radius:').place(x=10, y=25)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a, textvariable=self.Entry0).place(x=110, y=25)
        Label2 = Label(self.a, text='Volume:').place(x=10, y=50)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=110, y=50)

        Calculate_Button = Button(self.a, text='calculate', command=self.calculateSphereVolume).place(x=50, y=100)
        Clear_Button = Button(self.a, text='clear', command=self.clear_special_one_entry).place(x=150, y=100)
        self.a.mainloop()

    def calculateSFcube(self):
        a = self.EntryOriginal.get()
        b = self.Entry0.get()
        if a == '':
            self.answer.set('Please enter a length')
        elif b == '':
            self.answer.set('Please enter a width')
        elif float(a)<0 or float(b)<0:
            self.answer.set('Can not solve with negatives')
        else:
            answer2 = float(a) * float(b) * 6
            self.answer.set(str(answer2))

    def clear(self):
        self.EntryOriginal.set('')
        self.Entry0.set('')
        self.answer.set('')

    def SFcube(self):
        self.a = Tk()
        self.a.geometry('300x175')
        self.a.resizable(0, 0)
        self.a.title(self.formula_entry.get())

        originalLabel = Label(self.a, text="Length:").place(x=10, y=25)
        self.EntryOriginal = StringVar(self.a)
        OriginalEntry = Entry(self.a, textvariable=self.EntryOriginal).place(x=150, y=25)
        label1 = Label(self.a, text="Width:").place(x=10, y=50)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a, textvariable=self.Entry0).place(x=150, y=50)
        label3 = Label(self.a, text="Surface Area:").place(x=10, y=75)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=150, y=75)
        Calculate_Button = Button(self.a, text='calculate', command=self.calculateSFcube).place(x=50, y=125)
        Clear_Button = Button(self.a, text='clear', command=self.clear).place(x=150, y=125)

    def calculateSFcylinder(self):
        a = self.EntryOriginal.get()
        b = self.Entry0.get()
        if a == '':
            self.answer.set('Please enter a height')
        elif b == '':
            self.answer.set('Please enter a radius')
        elif float(a)<0 or float(b)<0:
            self.answer.set('Can not solve with negatives')
        else:
            answer2 = (float(a) * float(b) * 2 * pi) + ((float(b) ** 2 * pi) * 2)
            self.answer.set(str(answer2))

    def SFcylinder(self):
        self.a = Tk()
        self.a.geometry('300x175')
        self.a.resizable(0, 0)
        self.a.title(self.formula_entry.get())

        originalLabel = Label(self.a, text="Height:").place(x=10, y=25)
        self.EntryOriginal = StringVar(self.a)
        OriginalEntry = Entry(self.a, textvariable=self.EntryOriginal).place(x=150, y=25)
        label1 = Label(self.a, text="Radius:").place(x=10, y=50)
        self.Entry0 = StringVar(self.a)
        Entry1 = Entry(self.a, textvariable=self.Entry0).place(x=150, y=50)
        label3 = Label(self.a, text="Surface Area:").place(x=10, y=75)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=150, y=75)
        Calculate_Button = Button(self.a, text='calculate', command=self.calculateSFcylinder).place(x=50, y=125)
        Clear_Button = Button(self.a, text='clear', command=self.clear).place(x=150, y=125)

    def calculateSFsphere(self):
        a = self.Entry0.get()
        if a == '':
            self.answer.set('Please enter a radius')
        elif float(a)<0:
            self.answer.set('Can not solve with negative numbers')
        else:
            answer2 = 4 * float(a) ** 2 * pi
            self.answer.set(str(answer2))

    def SFsphere(self):
        self.a = Tk()
        self.a.geometry('300x150')
        self.a.resizable(0, 0)
        self.a.title(self.formula_entry.get())

        originalLabel = Label(self.a, text="Radius:").place(x=10, y=25)
        self.Entry0 = StringVar(self.a)
        OriginalEntry = Entry(self.a, textvariable=self.Entry0).place(x=150, y=25)
        label3 = Label(self.a, text="Surface Area:").place(x=10, y=50)
        self.answer = StringVar(self.a)
        answer_label = Label(self.a, textvariable=self.answer).place(x=150, y=50)
        Calculate_Button = Button(self.a, text='calculate', command=self.calculateSFsphere).place(x=50, y=100)
        Clear_Button = Button(self.a, text='clear', command=self.clear_special_one_entry).place(x=150, y=100)

    def calculatemidpoint_formula(self):
        x1 = self.coordinate1_x_value.get()
        y1 = self.coordinate1_y_value.get()
        x2 = self.coordinate2_x_value.get()
        y2 = self.coordinate2_y_value.get()
        if x1 == '':
            self.answer.set('Please enter the x coordinate for the first point')
        elif y1 == '':
            self.answer.set('Please enter the y coordinate for the first point')
        elif x2 == '':
            self.answer.set('Please enter the x coordinate for the second point')
        elif y2 == '':
            self.answer.set('Please enter the y coordinate for the second point')
        else:
            answer2 = (float(x1) + float(x2))/2
            answer3 = (float(y1) + float(y2))/2
            self.answer.set('(' + str(answer2)+' , '+str(answer3)+')')

    def MidPoint_Formula(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('400x300')
        self.a.resizable(0, 0)

        coordinate1 = Label(self.a, text='Coordinate 1:').place(x=20,y=50)
        coordinate1_x = Label(self.a, text='X coordinate').place(x=125,y=25)
        coordinate1_y = Label(self.a, text='Y coordinate').place(x=250,y=25)
        self.coordinate1_x_value = StringVar(self.a)
        self.coordinate1_y_value = StringVar(self.a)
        coordinate1_x_entry = Entry(self.a, textvariable=self.coordinate1_x_value).place(x=100,y=50)
        coordinate1_y_entry = Entry(self.a, textvariable=self.coordinate1_y_value).place(x=225,y=50)
        coordinate2 = Label(self.a, text='Coordinate 2:').place(x=20,y=100)
        self.coordinate2_x_value = StringVar(self.a)
        self.coordinate2_y_value = StringVar(self.a)
        coordinate2_x_entry = Entry(self.a, textvariable=self.coordinate2_x_value).place(x=100, y=100)
        coordinate2_y_entry = Entry(self.a, textvariable=self.coordinate2_y_value).place(x=225, y=100)
        distanceLabel = Label(self.a, text='Midpoint between coordinates:').place(x=125,y=125)
        self.answer = StringVar(self.a)
        answerLabel = Label(self.a, textvariable=self.answer).place(x=100, y=150)
        Calculate_Button = Button(self.a, text='  calculate  ', command=self.calculatemidpoint_formula).place(x=50,y=200)
        Clear_Button = Button(self.a, text='  clear  ', command=self.clearDistance).place(x=275, y=200)

    def calculateLinearEquation(self):
        x1 = self.coordinate1_x_value.get()
        y1 = self.coordinate1_y_value.get()
        x2 = self.coordinate2_x_value.get()
        y2 = self.coordinate2_y_value.get()
        if x1 == '':
            self.answer.set('Please enter the x coordinate for the first point')
        elif y1 == '':
            self.answer.set('Please enter the y coordinate for the first point')
        elif x2 == '':
            self.answer.set('Please enter the x coordinate for the second point')
        elif y2 == '':
            self.answer.set('Please enter the y coordinate for the second point')
        elif float(x1) == float(x2) and float(y1) == float(y2):
            self.answer.set('Please enter two different coordinates')
        else:
            slope_answer = (float(y2) - float(y1)) / (float(x2) - float(x1))
            y_intercept = float(y1) - (float(slope_answer) * float(x1))
            self.answer.set('y = ' + str(slope_answer) + '(x) + ' + str(y_intercept))

    def Find_line_equation(self):
        self.a = Tk()
        self.a.title(self.formula_entry.get())
        self.a.geometry('400x300')
        self.a.resizable(0, 0)

        coordinate1 = Label(self.a, text='Coordinate 1:').place(x=20, y=50)
        coordinate1_x = Label(self.a, text='X coordinate').place(x=125, y=25)
        coordinate1_y = Label(self.a, text='Y coordinate').place(x=250, y=25)
        self.coordinate1_x_value = StringVar(self.a)
        self.coordinate1_y_value = StringVar(self.a)
        coordinate1_x_entry = Entry(self.a, textvariable=self.coordinate1_x_value).place(x=100, y=50)
        coordinate1_y_entry = Entry(self.a, textvariable=self.coordinate1_y_value).place(x=225, y=50)
        coordinate2 = Label(self.a, text='Coordinate 2:').place(x=20, y=100)
        self.coordinate2_x_value = StringVar(self.a)
        self.coordinate2_y_value = StringVar(self.a)
        coordinate2_x_entry = Entry(self.a, textvariable=self.coordinate2_x_value).place(x=100, y=100)
        coordinate2_y_entry = Entry(self.a, textvariable=self.coordinate2_y_value).place(x=225, y=100)
        distanceLabel = Label(self.a, text='Linear equation:').place(x=125, y=125)
        self.answer = StringVar(self.a)
        answerLabel = Label(self.a, textvariable=self.answer).place(x=100, y=150)

        Calculate_Button = Button(self.a, text='  calculate  ', command=self.calculateLinearEquation).place(x=50,y=200)
        Clear_Button = Button(self.a, text='  clear  ', command=self.clearDistance).place(x=275, y=200)

    def submit(self):
        if self.formula_entry.get() == 'Area of Square':
            self.Area_of_Square()
        elif self.formula_entry.get() == 'Area of Rectangle':
            self.Area_of_Rectangle()
        elif self.formula_entry.get() == 'Area of Right Triangle':
            self.Area_of_Right_Triangle()
        elif self.formula_entry.get() == 'Area of Rhombus':
            self.Area_of_Rhombus()
        elif self.formula_entry.get() == 'Area of Circle':
            self.Area_of_Circle()
        elif self.formula_entry.get() == 'Perimeter of Square':
            self.Perimeter_Square()
        elif self.formula_entry.get() == 'Perimeter of Rectangle':
            self.Perimeter_of_Rectangle()
        elif self.formula_entry.get() == 'Circumference of Circle':
            self.Circumference_Circle()
        elif self.formula_entry.get() == 'Exponential Decay':
            self.exponential_decay()
        elif self.formula_entry.get() == 'Exponential Growth':
            self.exponential_growth()
        elif self.formula_entry.get() == 'Annual Interest':
            self.Annual_Interest()
        elif self.formula_entry.get() == 'Quadratic Formula':
            self.Quadratic_Formula()
        elif self.formula_entry.get() == 'Arithmetic Sequence':
            self.Arithmetic_Sequence()
        elif self.formula_entry.get() == 'Geometric Sequence':
            self.Geometric_Sequence()
        elif self.formula_entry.get() == 'Distance Formula':
            self.Distance_Formula()
        elif self.formula_entry.get() == 'Pythagorean Theorem':
            self.Pythagorean_Theorem()
        elif self.formula_entry.get() == 'Volume of Cube/Rect-Prisim':
            self.Volume_of_Cube()
        elif self.formula_entry.get() == 'Volume of Cylinder':
            self.Volume_of_Cylinder()
        elif self.formula_entry.get() == 'Volume of Sphere':
            self.Volume_of_Sphere()
        elif self.formula_entry.get() == 'Surface Area of Cube/Rect-Prisim':
            self.SFcube()
        elif self.formula_entry.get() == 'Surface Area of Cylinder':
            self.SFcylinder()
        elif self.formula_entry.get() == 'Surface Area of Sphere':
            self.SFsphere()
        elif self.formula_entry.get() == 'Midpoint Formula':
            self.MidPoint_Formula()
        elif self.formula_entry.get() == 'Find Linear Equation':
            self.Find_line_equation()
        return




v = Math()




