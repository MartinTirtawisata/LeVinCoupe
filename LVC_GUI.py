from tkinter import *

#Creates a window
root = Tk()


root.mainloop()


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
----------organizing grid layout and binding functions into layouts
def checkState():
    #this prints out the type of data
    if var.get() == 1:
        print("checkbox is checked")
    else:
        print("not checked")

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")

entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, column=0, sticky=E)
#stickey = E as East; stick to the right
label_2.grid(row=1, column=0, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

var = IntVar()
#this is a tkinter variable...??

check = Checkbutton(root, text="Keep me signed in", command=checkState, variable=var) #Remove bracket for function argument
#command -- is one of the methods

check.grid(columnspan=2)
#column span to take two column
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




