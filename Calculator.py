
import sys
from tkinter import *
import tkinter

class Calculator_App(tkinter.Frame):
    def __init__(self, master, **options):
        tkinter.Frame.__init__(self, master, options)
        self.grid()
        self.add_Components()

    def add_Components(self):

        self.display = tkinter.Entry(self, justify='right', bd=34, bg='white', textvariable=txtDisplay)
        self.display.grid(column=0, row=0, columnspan=5, sticky='we')

        buttons = [

            '1', '2', '3', '(', ')',
            '4', '5', '6', '*', '/',
            '7', '8', '9', '+', '-',
            '.', '0', 'CE', 'C', '='

        ]

        varColumn = -1
        varRow = 1

        for button in buttons:
            varColumn += 1

            self.btnClick = ClickButtons(self, value=button, width=4, height=3, padx=16, pady=16, bd=8,
                text=button.replace(' ', ''), relief="raised", )

            if button == "C":
                self.btnClick.configure(command=self.btnClick.Equals_Input)

            elif button == "CE":
                self.btnClick.configure(command=self.btnClick.Equals_Input)

            elif button == "=":
                self.btnClick.configure(command=self.btnClick.Answer_Input)
                self.btnClick.grid(column=varColumn, row=varRow)

            else:
                self.btnClick.configure(command=self.btnClick.Additon_Input)

            self.btnClick.grid(column=varColumn, row=varRow)

            if varColumn == 4:
                varColumn = -1
                varRow += 1


class ClickButtons(tkinter.Button):
    def __init__(self, master, value=NONE, **options):
        tkinter.Button.__init__(self, master, options)

        self.value = value

    def Additon_Input(self):
        global operator
        App_Function.display.config(fg="black")
        operator += self.value

        txtDisplay.set(operator.replace(' ', ''))

    def Equals_Input(self):
        global operator

        if not operator == "":
            selector = operator.split()[-1][-1]

            if selector == '*' or selector == '/':
                operator = operator[0:-3]

            elif selector == '+' or selector == '-':
                operator = operator[0:-2]

            else:

                operator = operator[0:-1]

            txtDisplay.set(operator.replace(' ', ''))

        else:

            txtDisplay.set(operator.replace(' ', ''))

    def Answer_Input(self):
        global operator

        App_Function.display.config(fg="black")

        DisplayAnswer = Functional_Output(operator)
        txtDisplay.set(DisplayAnswer)

        operator = ""

def Functional_Output(Validate_Input):
    print(Validate_Input)
    try:
            while '(' in Validate_Input and ')' in Validate_Input:
                print("am in")
                Validate_Output = Validate_Input.count('(')

                Intake_Input = Validate_Input.find('(')
                fin = Validate_Input.find(')') + 1

                while Validate_Output > 1:
                    Intake_Input = Validate_Input.find('(', Intake_Input+1)
                    Validate_Output -= 1

                receive_value = Validate_Input[Intake_Input:fin]
                receive_input = callable(receive_value.replace('(', '').replace(')', ''))
                Validate_Input = Validate_Input.replace(receive_value, receive_input)

            DisplayAnswer = float(AddFunction(Validate_Input))

    except:
            DisplayAnswer = "Error"

    return DisplayAnswer

def AddFunction(Validate_Input):

    #add_selection = Validate_Input.split()
    add_selection = list(Validate_Input)
    print(add_selection)
    print("I just came in")

    while len(add_selection) != 1:

        for index in range(len(add_selection)):
            if add_selection[index] == '/':
                add_selection[index] = str(float(add_selection[index-1]) / float(add_selection[index+1]))

                add_selection.pop(index+1)
                add_selection.pop(index-1)
                break

            elif add_selection[index] == '*':
                add_selection[index] = str(float(add_selection[index-1]) * float(add_selection[index+1]))

                add_selection.pop(index+1)
                add_selection.pop(index-1)
                break

        if not '/'  in add_selection and not '*' in add_selection:
            while len(add_selection) != 1:
                for index in range(len(add_selection)):
                    add_selection[index] = str(float(add_selection[index]) + float(add_selection[index]))

                    add_selection.pop(index+1)
                    break

    return add_selection(0)


root = tkinter.Tk()
root.resizable(0, 0)
root.title("Calculator")

txtDisplay = tkinter.StringVar()
operator = ""

App_Function = Calculator_App(root)

root.mainloop()


























