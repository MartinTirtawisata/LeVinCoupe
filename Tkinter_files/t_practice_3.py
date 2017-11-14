class Login(Frame):

    db_name = 'LeVinEmployee.db'

    def __init__(self, master):
        super().__init__(master)

        self.ue_label = Label(self, text="Email")
        self.pw_label = Label(self, text="Password")

        self.userEmail = Entry(self)
        self.userPassword = Entry(self, show="*")

        self.ue_label.grid(row=0, sticky=E)
        self.pw_label.grid(row=1, sticky=E)
        self.userEmail.grid(row=0, column=1)
        self.userPassword.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.loginbtn = Button(self, text="Login", command=self.check_login())
        self.loginbtn.grid(columnspan=2)

        self.pack()

    def check_login(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Employee WHERE(Email = '" + str(self.userEmail) + "') AND (Password = '" + str(self.userPassword) + "')")
                self.query_result = cursor.fetchone()
        except (KeyError) as e:
            print(e)

        self.userEmail = str(self.userEmail.get())
        self.userPassword = str(self.userPassword.get())

        if self.userEmail == "JO" and self.userPassword=="Jo":
            tm.showinfo("Login info", "Welcome" + self.userEmail)
        else:
            tm.showerror("Login error", "Incorrect username")





# cur.execute("SELECT * FROM Employee WHERE(Email = '" + userEmail + "') AND (Password = '" + userPassword + "')")
#
#                     results = cur.fetchall()
#
#                     if userEmail == results[0][7] and userPassword == results[0][8]:
#                         print("\nLogin successful!")
#                         break
#                 except:
#                     print("\nConnection Failed. You entered a wrong email or password. Please try again.")



class Main_Menu(Frame):

    def __init__(self, master):
        self.button_A = Button(root_menu, text="Register an Employee", command=t_check_register)
        self.button_B = Button(root_menu, text="Associate Wine's Characteristic and Quality", command=t_check_association)
        self.button_C = Button(root_menu, text="Test Wine Characteristic Frequency Distribution based on Quality")
        self.button_D = Button(root_menu, text="Ask Additional Questions or Add Additional Features")
        self.button_E = Button(root_menu, text="Quit", bg="red")
        self.button_A.pack()
        self.button_B.pack()
        self.button_C.pack()
        self.button_D.pack()
        self.button_E.pack()

    def t_check_register():
        root_menu.destroy()
        return t_register()


root = Tk()
Login(root)
root.mainloop()

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
