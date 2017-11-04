from tkinter import *

def Login():
    global root_login

    root_login = Tk()
    root_login.title("LeVinCoupe - Login")

    label_email = Label(root_login, text="Email")
    label_password = Label(root_login, text="Password")
    button_sign_in = Button(root_login, text="Log in", command=check_login)
    label_email.grid(row=0, column=0, sticky=E)
    label_password.grid(row=1, column=0, sticky=E)
    button_sign_in.grid(row=2, column=2, sticky=E)

    entry_email = Entry(root_login)
    entry_password = Entry(root_login, show='*')
    entry_email.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)

    var = IntVar()
    # this is a tkinter variable...??

    check = Checkbutton(root_login, text="Keep me signed in", command=checkState, variable=var)  # Remove bracket for function argument
    # command -- is one of the methods

    check.grid(row=2, column=0, columnspan=2)
    # column span to take two column

    root_login.mainloop()

def check_login():

    root_login.destroy()
    main_menu()

def checkState():
    #this prints out the type of data
    if var.get() == 1:
        print("checkbox is checked")
    else:
        print("not checked")

def main_menu():
    root_menu = Tk()
    root_menu.title("LeVinCoupe Title")
    button_A = Button(root_menu, text="Register an Employee")
    button_B = Button(root_menu, text="Associate Wine's Characteristic and Quality")
    button_C = Button(root_menu, text="Test Wine Characteristic Frequency Distribution based on Quality")
    button_D = Button(root_menu, text="Ask Additional Questions or Add Additional Features")
    button_E = Button(root_menu, text="Quit")
    button_A.pack()
    button_B.pack()
    button_C.pack()
    button_D.pack()
    button_E.pack()
    root_menu.mainloop()

    def menu():
        print("\n===============================================================================")
        print("a. Register other employees")
        print("b. Test wine associations based on characteristic and quality")
        print("c. Create wine frequency distribution based on value of wine characteristic and wine quality")
        print("d. Ask additional questions or add features")
        print("e. Quit")
        print("=================================================================================")



#------------------------Main System-----------------

Login()




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




