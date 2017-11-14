from tkinter import *
from tkinter import ttk

# (t) in front is to indicate that it is a tkinter function
# (check) a function that validates

def start_program():
    t_login()

def t_login():
    global root_login
    global mainframe

    root_login = Tk()
    root_login.title("LeVinCoupe - Login")
    root_login.geometry('500x300+300+400')

    label_email = Label(root_login, text="Email")
    label_password = Label(root_login, text="Password")
    button_sign_in = Button(root_login, text="Log in", command=t_check_login)
    label_email.grid(row=0, column=0, sticky=E)
    label_password.grid(row=1, column=0, sticky=E)
    button_sign_in.grid(row=2, column=2, sticky=E)

    entry_email = Entry(root_login)
    entry_password = Entry(root_login, show='*')
    entry_email.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)

    var = IntVar()
    # this is a tkinter variable...??
    check = Checkbutton(root_login, text="Keep me signed in", command=t_checkState, variable=var)  # Remove bracket for function argument
    # command -- is one of the methods
    check.grid(row=2, column=0, columnspan=2)
    # column span to take two column
    root_login.mainloop()

def t_check_login():
    root_login.destroy()
    return t_main_menu()

def t_checkState():
    #this prints out the type of data
    if var.get() == 1:
        print("checkbox is checked")
    else:
        print("not checked")

def t_main_menu():
    global root_menu
    root_menu = Tk()
    root_menu.title("LeVinCoupe Title")

    button_A = Button(root_menu, text="Register an Employee", command=t_check_register)
    button_B = Button(root_menu, text="Associate Wine's Characteristic and Quality", command=t_check_association)
    button_C = Button(root_menu, text="Test Wine Characteristic Frequency Distribution based on Quality")
    button_D = Button(root_menu, text="Ask Additional Questions or Add Additional Features")
    button_E = Button(root_menu, text="Quit", bg="red")
    button_A.pack()
    button_B.pack()
    button_C.pack()
    button_D.pack()
    button_E.pack()
    root_menu.mainloop()

def t_check_register():
    root_menu.destroy()
    return t_register()

def t_register():
    #Need Employee ID, First Name, Last Name,  Address, City, State, Zip Code, Email, Password
    root_register = Tk()
    root_register.title("LeVinCoupe Employee Register")

    label_emp_id = Label(root_register, text="Enter Employee ID")
    label_fname = Label(root_register, text="Enter First Name")
    label_lname = Label(root_register, text="Enter Last Name")
    label_address = Label(root_register, text="Enter Address")
    label_city = Label(root_register, text="Enter City")
    label_state = Label(root_register, text="Enter State")
    label_zip_code = Label(root_register, text="Enter Zip Code")
    label_email = Label(root_register, text="Enter Email")
    label_password = Label(root_register, text="Enter Password")
    entry_emp_id = Entry(root_register)
    entry_fname = Entry(root_register)
    entry_lname = Entry(root_register)
    entry_address = Entry(root_register)
    entry_city = Entry(root_register)
    entry_state = Entry(root_register)
    entry_zip_code = Entry(root_register)
    entry_email = Entry(root_register)
    entry_password = Entry(root_register)

    label_emp_id.grid(row=0, column=0)
    label_fname.grid(row=1, column=0)
    label_lname.grid(row=2, column=0)
    label_address.grid(row=3, column=0)
    label_city.grid(row=4, column=0)
    label_state.grid(row=5, column=0)
    label_zip_code.grid(row=6, column=0)
    label_email.grid(row=7, column=0)
    label_password.grid(row=8, column=0)
    entry_emp_id.grid(row=0, column=1)
    entry_fname.grid(row=1, column=1)
    entry_lname.grid(row=2, column=1)
    entry_address.grid(row=3, column=1)
    entry_city.grid(row=4, column=1)
    entry_state.grid(row=5, column=1)
    entry_zip_code.grid(row=6, column=1)
    entry_email.grid(row=7, column=1)
    entry_password.grid(row=8, column=1)

    button_sign_up = Button(root_register, text="Sign Up")
    button_sign_up.grid(columnspan=3)
    root_register.mainloop()

def t_check_association():
    root_menu.destroy()
    t_association()

def t_association():
    global root_association
    root_association = Tk()
    root_association.title("LeVinCoupe Association")

    button_a = Button(root_association, text="Volatile Acidity and Wine Quality", command=t_wine_type)
    button_b = Button(root_association, text="Fixed Acidity and Wine Quality")
    button_c = Button(root_association, text="Alcohol Percentage and Wine Quality")
    button_d = Button(root_association, text="Residual Sugar and Wine Quality")

    button_a.pack()
    button_b.pack()
    button_c.pack()
    button_d.pack()

    root_association.mainloop()

def t_wine_type():
    root_association.destroy()

    root_wine_type = Tk()

    button_red = Button(root_wine_type, text="Red")
    button_white = Button(root_wine_type, text="White")

    button_red.pack()
    button_white.pack()

    root_wine_type.mainloop()



#------------------------Main System-----------------

start_program()



'''
def checkClicked(event):
        print("it's clicked")

    button1 = Button(root, text="Click here")
    button1.bind("<Button-1>", checkClicked)
    # binding - is the second method to include functions

    button1.pack()

'''
'''
canvas = Canvas(root, width=200, height=100)
canvas.pack()


black_line = canvas.create_line(0,0,200,50)
red_line = canvas.create_line(0,100,200,50,fill="red")
'''
'''
----using a class to create an event-------
class LearningGUI:

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(master, text="printing message", command=self.printMessage)

        self.quitButton = Button(master, text="Quit", command=master.quit) # master.quit is a tkinter built in method

        self.printButton.pack(side=LEFT)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("wow this works")

'''

'''
-----Creating mouseclick events----
def leftClick(event):
    print("Left")

def rightClick(event):
    print("Right")

def middleClick(event):
    print("MiddleScroll")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-3>", rightClick)
frame.bind("<Button-3>", middleClick)
frame.pack()
'''

'''
------using event binding to include button & function ----
def checkClicked(event):
    print("it's clicked")
button1 = Button(root, text="Click here")
button1.bind("<Button-1>",checkClicked)
#binding - is the second method to include functions

button1.pack()
'''


'''
-------------Widgets------------
one = Label(root,text="One",fg="white",bg="black")
# fg = floor ground (font), bg = background
one.pack()
two = Label(root,text="Two",fg="black",bg="yellow")
two.pack(fill=X)
#fill the background color into X axis direction; horizontal
three = Label(root,text="Three",fg="green",bg="purple")
three.pack(side=LEFT, fill=Y)
four = Label(root,text="Four",fg="green",bg="purple")
four.pack(fill=BOTH, expand=True)
#for expanding both Y and X direction

'''



''' Frames: something of a rectangle; panes'''
'''
How to organize frames
topFrame = Frame(root)
topFrame.pack()
#pack is always used if we want it to include inside the window

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")
#the argument for the button: (Where do you want it, the text of it, and color of button

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
'''






# import tkinter as tk
#
# class Demo1:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
#         self.button1.pack()
#         self.frame.pack()
#
#     def new_window(self):
#         self.newWindow = tk.Toplevel(self.master)
#         self.app = Demo2(self.newWindow)
#
# class Demo2:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
#         self.quitButton.pack()
#         self.frame.pack()
#
#     def close_windows(self):
#         self.master.destroy()
#
# def main():
#     root = tk.Tk()
#     app = Demo1(root)
#     root.mainloop()
#
# if __name__ == '__main__':
#     main()


# from tkinter import *
#
#
# window = Tk()
#
# window.geometry('500x300+300+400')
#
# window.mainloop()