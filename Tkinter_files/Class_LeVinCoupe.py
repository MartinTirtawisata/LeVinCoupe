import matplotlib
matplotlib.use("TkAgg")
import pandas as pd
import scipy.stats
import seaborn
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
import tkinter.messagebox as tm
import sqlite3


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginFrame, MenuFrame, RegisterFrame, AssociationFrame, FreqDistFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginFrame")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class LoginFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        self.label_email = tk.Label(self, text="Email")
        self.label_password = tk.Label(self, text="Password")

        self.entry_email = tk.Entry(self)
        self.entry_password = tk.Entry(self, show="*")

        self.label_email.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_email.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = tk.Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = tk.Button(self, text="Login", command=lambda: self.check_login(controller))
        self.logbtn.grid(columnspan=2)

        self.pack()

    def check_login(self, controller):
        self.controller = controller
        userEmail = self.entry_email.get()
        userPassword = self.entry_password.get()

        try:
            with sqlite3.connect('LeVinEmployee.db') as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM Employee WHERE(Email = '" + userEmail + "') AND (Password = '" + userPassword + "')")
                query_result = cursor.fetchone()
                print(query_result)
        except (KeyError) as e:
            print(e)
        try:
            if userEmail == query_result[7] and userPassword == query_result[8]:
                tm.showinfo("Login info", "Welcome " + query_result[1] + " " + query_result[2])
                controller.show_frame("MenuFrame")
        except:
            tm.showerror("Login error", "Incorrect Email or Password")



class MenuFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.top_Frame = tk.Frame(self, bg="yellow")
        self.top_Frame.pack(side=TOP, fill=BOTH, expand=True)
        self.bot_Frame = tk.Frame(self, bg="green")
        self.bot_Frame.pack(side=BOTTOM, fill=X)

        self.button_A = tk.Button(self.top_Frame, text="Register other employees",
                                  command=lambda: controller.show_frame("RegisterFrame"))
        self.button_A.pack(fill=X)

        self.button_B = tk.Button(self.top_Frame, text="Test wine associations based on characteristic & quality",
                                  command=lambda: controller.show_frame("AssociationFrame"))
        self.button_B.pack(fill=X)

        self.button_C = tk.Button(self.top_Frame,
                          text="Create wine frequency distribution based on value of wine characteristic & quality",
                                  command=lambda: controller.show_frame("FreqDistFrame"))
        self.button_C.pack(fill=X)

        self.button_D = tk.Button(self.top_Frame, text="Test wine associations based on user inputted characteristics")
        self.button_D.pack(fill=X)

        self.back_button = tk.Button(self.bot_Frame, text="Main Menu", command=lambda: controller.show_frame("LoginFrame"))
        self.back_button.pack(side=LEFT)
        self.quit_button = tk.Button(self.bot_Frame, text="Quit", fg="red")
        self.quit_button.pack(side=RIGHT)

class RegisterFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.top_Frame = tk.Frame(self)
        self.top_Frame.pack(side=TOP)
        self.bot_Frame = tk.Frame(self)
        self.bot_Frame.pack(side=BOTTOM, fill=X)

        self.label_emp_id = tk.Label(self.top_Frame, text="Enter Employee ID")
        self.label_emp_id.grid(row=0, column=0)
        self.entry_emp_id = tk.Entry(self.top_Frame)
        self.entry_emp_id.grid(row=0, column=1)

        self.label_fname = tk.Label(self.top_Frame, text="Enter First Name")
        self.label_fname.grid(row=1, column=0)
        self.entry_fname = tk.Entry(self.top_Frame)
        self.entry_fname.grid(row=1, column=1)

        self.label_lname = tk.Label(self.top_Frame, text="Enter Last Name")
        self.label_lname.grid(row=2, column=0)
        self.entry_lname = tk.Entry(self.top_Frame)
        self.entry_lname.grid(row=2, column=1)

        self.label_address = tk.Label(self.top_Frame, text="Enter Address")
        self.label_address.grid(row=3, column=0)
        self.entry_address = tk.Entry(self.top_Frame)
        self.entry_address.grid(row=3, column=1)

        self.label_city = tk.Label(self.top_Frame, text="Enter City")
        self.label_city.grid(row=4, column=0)
        self.entry_city = tk.Entry(self.top_Frame)
        self.entry_city.grid(row=4, column=1)

        self.label_state = tk.Label(self.top_Frame, text="Enter State")
        self.label_state.grid(row=5, column=0)
        self.entry_state = tk.Entry(self.top_Frame)
        self.entry_state.grid(row=5, column=1)

        self.label_zip_code = tk.Label(self.top_Frame, text="Enter Zip Code")
        self.label_zip_code.grid(row=6, column=0)
        self.entry_zip_code = tk.Entry(self.top_Frame)
        self.entry_zip_code.grid(row=6, column=1)

        self.label_email = tk.Label(self.top_Frame, text="Enter Email")
        self.label_email.grid(row=7, column=0)
        self.entry_email = tk.Entry(self.top_Frame)
        self.entry_email.grid(row=7, column=1)

        self.label_password = tk.Label(self.top_Frame, text="Enter Password")
        self.label_password.grid(row=8, column=0)
        self.entry_password = tk.Entry(self.top_Frame)
        self.entry_password.grid(row=8, column=1)

        self.button_sign_up = tk.Button(self.top_Frame, text="Sign Up", command=lambda: self.insert_registration(controller))
        self.button_sign_up.grid(columnspan=3)

        self.back_button = tk.Button(self.bot_Frame, text="Main Menu", command=lambda: controller.show_frame("MenuFrame"))
        self.back_button.pack(side=LEFT)
        self.quit_button = tk.Button(self.bot_Frame, text="Quit", fg='red')
        self.quit_button.pack(side=RIGHT)

    def insert_registration(self, controller):
        self.controller = controller
        userEmp_id = self.entry_emp_id.get()
        userF_name = str(self.entry_fname.get())
        userL_name = str(self.entry_lname.get())
        userAddress = self.entry_address.get()
        userCity = self.entry_city.get()
        userState = self.entry_state.get()
        userZip_code = self.entry_zip_code.get()
        userEmail = self.entry_email.get()
        userPassword = self.entry_password.get()

        try:
            with sqlite3.connect('LeVinEmployee.db') as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Employee VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                               (userEmp_id, userF_name, userL_name, userAddress, userCity, userState, userZip_code,
                                userEmail, userPassword))
                tm.showinfo("Registration Info", "" + userF_name + " " + userL_name + "has been successfully registered")
                controller.show_frame("MenuFrame")
        except sqlite3.Error as e:
            print(e)
            tm.showerror("Registration error", "Employee was unable to be registered. Please check the information you entered.")

class AssociationFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.top_Frame = tk.Frame(self)
        self.top_Frame.pack(side=TOP)
        self.left_Frame = tk.Frame(self.top_Frame, bg="green")
        self.left_Frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.right_Frame = tk.Frame(self.top_Frame, bg="blue")
        self.right_Frame.pack(side=RIGHT, fill=BOTH, expand=True)

        self.middle_Frame = tk.Frame(self, bg="purple")
        self.middle_Frame.pack(side=TOP, fill=X)
        self.bot_Frame = tk.Frame(self)
        self.bot_Frame.pack(side=BOTTOM, fill=X)

        self.var_wine_char = tk.IntVar()
        self.var_wine_type = tk.IntVar()

        self.button_a = tk.Radiobutton(self.left_Frame, text="Volatile Acidity and Wine Quality", variable=self.var_wine_char, value=1)
        self.button_a.grid(row=0, column=1, sticky=W)

        self.button_b = tk.Radiobutton(self.left_Frame, text="Fixed Acidity and Wine Quality", variable=self.var_wine_char, value=2)
        self.button_b.grid(row=1, column=1, sticky=W)

        self.button_c = tk.Radiobutton(self.left_Frame, text="Alcohol Percentage and Wine Quality", variable=self.var_wine_char, value=3)
        self.button_c.grid(row=2, column=1, sticky=W)

        self.button_d = tk.Radiobutton(self.left_Frame, text="Residual Sugar and Wine Quality", variable=self.var_wine_char, value=4)
        self.button_d.grid(row=3, column=1, sticky=W)

        self.button_red = tk.Radiobutton(self.right_Frame, text="Red", variable=self.var_wine_type, value=8)
        self.button_red.grid(row=0, column=0, sticky=W)

        self.button_white = tk.Radiobutton(self.right_Frame, text="White", variable=self.var_wine_type, value=9)
        self.button_white.grid(row=1, column=0, sticky=W)

        self.button_enter = tk.Button(self.middle_Frame, text="Submit", command=self.association_result, fg="green")
        self.button_enter.pack(fill=X)

        self.back_button = tk.Button(self.bot_Frame, text="Main Menu", command=lambda: controller.show_frame("MenuFrame"))
        self.back_button.pack(side=LEFT)
        self.quit_button = tk.Button(self.bot_Frame, text="Quit", fg="red")
        self.quit_button.pack(side=RIGHT)

    def association_result(self):
        if self.var_wine_char.get() == 1:
            if self.var_wine_type.get() == 8:
                print(self.var_wine_char)
                print(self.var_wine_type)
                try:
                    WineCharX = "quality"
                    WineCharY = "volatile acidity"
                    allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                    red = allWines.loc[allWines['type'] == 'red', :]

                    getCorr = scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
                    correlation = str(getCorr[0])
                    pValue = str(getCorr[1])
                    print("\nFor red wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                    print("With p-value of: " + pValue)

                    seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
                    plt.xlabel(WineCharX)
                    plt.ylabel(WineCharY)
                    plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
                    plt.show()

                except (KeyError) as e:
                    print("\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")
            if self.var_wine_type.get() == 9:
                print(self.var_wine_char)
                print(self.var_wine_type)

                try:
                    WineCharX = "quality"
                    WineCharY = "volatile acidity"
                    allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                    white = allWines.loc[allWines['type'] == 'white', :]

                    getCorr = scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
                    correlation = str(getCorr[0])
                    pValue = str(getCorr[1])
                    print("\nFor white wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                    print("With p-value of: " + pValue)

                    seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
                    plt.xlabel(WineCharX)
                    plt.ylabel(WineCharY)
                    plt.title("White Wine: " + WineCharX + " X " + WineCharY)
                    plt.show()

                except (KeyError) as e:
                    print("\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")
                    # ---------------------------------------FIXED ACIDITY--------------------------------------
        if self.var_wine_char.get() == 2:
            if self.var_wine_type.get() == 8:
                print(self.var_wine_char)
                print(self.var_wine_type)

                try:
                    WineCharX = "quality"
                    WineCharY = "fixed acidity"
                    allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                    red = allWines.loc[allWines['type'] == 'red', :]

                    getCorr = scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
                    correlation = str(getCorr[0])
                    pValue = str(getCorr[1])
                    print("\nFor red wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                    print("With p-value of: " + pValue)

                    seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
                    plt.xlabel(WineCharX)
                    plt.ylabel(WineCharY)
                    plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
                    plt.show()

                except (KeyError) as e:
                    print("\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")

            if self.var_wine_type.get() == 9:
                print(self.var_wine_char)
                print(self.var_wine_type)

                try:
                    WineCharX = "quality"
                    WineCharY = "fixed acidity"
                    allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                    white = allWines.loc[allWines['type'] == 'white', :]

                    getCorr = scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
                    correlation = str(getCorr[0])
                    pValue = str(getCorr[1])
                    print("\nFor white wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                    print("With p-value of: " + pValue)

                    seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
                    plt.xlabel(WineCharX)
                    plt.ylabel(WineCharY)
                    plt.title("White Wine: " + WineCharX + " X " + WineCharY)
                    plt.show()

                except (KeyError) as e:
                    print("\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")
                    # -----------------------------------------------ALCOHOL-------------------------------------------------------------
        if self.var_wine_char.get() == 3:
            if self.var_wine_type.get() == 8:
                print(self.var_wine_char)
                print(self.var_wine_type)

                try:
                    WineCharX = "quality"
                    WineCharY = "alcohol"
                    allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                    red = allWines.loc[allWines['type'] == 'red', :]

                    getCorr = scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
                    correlation = str(getCorr[0])
                    pValue = str(getCorr[1])
                    print("\nFor red wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                    print("With p-value of: " + pValue)

                    seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
                    plt.xlabel(WineCharX)
                    plt.ylabel(WineCharY)
                    plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
                    plt.show()

                except (KeyError) as e:
                    print("\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")

            if self.var_wine_type.get() == 9:
                print(self.var_wine_char)
                print(self.var_wine_type)

                try:
                    WineCharX = "quality"
                    WineCharY = "alcohol"
                    allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                    white = allWines.loc[allWines['type'] == 'white', :]

                    getCorr = scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
                    correlation = str(getCorr[0])
                    pValue = str(getCorr[1])
                    print("\nFor white wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                    print("With p-value of: " + pValue)

                    seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
                    plt.xlabel(WineCharX)
                    plt.ylabel(WineCharY)
                    plt.title("White Wine: " + WineCharX + " X " + WineCharY)
                    plt.show()

                except (KeyError) as e:
                    print("\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")
                    # ---------------------------------------------------RESIDUAL SUGAR -----------------------------------------------
        if self.var_wine_char.get() == 4:
            if self.var_wine_type.get() == 8:
                print(self.var_wine_char)
                print(self.var_wine_type)

                try:
                    WineCharX = "quality"
                    WineCharY = "residual sugar"
                    allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                    red = allWines.loc[allWines['type'] == 'red', :]

                    getCorr = scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
                    correlation = str(getCorr[0])
                    pValue = str(getCorr[1])
                    print("\nFor red wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                    print("With p-value of: " + pValue)

                    seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
                    plt.xlabel(WineCharX)
                    plt.ylabel(WineCharY)
                    plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
                    plt.show()

                except (KeyError) as e:
                    print("\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")

            if self.var_wine_type.get() == 9:
                print(self.var_wine_char)
                print(self.var_wine_type)

                try:
                    WineCharX = "quality"
                    WineCharY = "residual sugar"
                    allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                    white = allWines.loc[allWines['type'] == 'white', :]

                    getCorr = scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
                    correlation = str(getCorr[0])
                    pValue = str(getCorr[1])
                    print("\nFor white wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                    print("With p-value of: " + pValue)

                    seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
                    plt.xlabel(WineCharX)
                    plt.ylabel(WineCharY)
                    plt.title("White Wine: " + WineCharX + " X " + WineCharY)
                    plt.show()

                except (KeyError) as e:
                    print("\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")

class FreqDistFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.top_Frame = tk.Frame(self)
        self.top_Frame.pack(side=TOP)
        self.left_Frame = tk.Frame(self.top_Frame)
        self.left_Frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.right_Frame = tk.Frame(self.top_Frame)
        self.right_Frame.pack(side=RIGHT, fill=BOTH, expand=True)

        self.middle_Frame = tk.Frame(self)
        self.middle_Frame.pack(side=TOP, fill=X)

        self.middle_bot_Frame = tk.Frame(self)
        self.middle_bot_Frame.pack(side=TOP, fill=X)

        self.bot_Frame = tk.Frame(self)
        self.bot_Frame.pack(side=BOTTOM, fill=X)

        self.fd_var_wine_char = IntVar()
        self.fd_var_wine_type = IntVar()

        self.button_a = tk.Radiobutton(self.left_Frame, text="Volatile Acidity and Wine Quality", variable=self.fd_var_wine_char, value=1)
        self.button_a.grid(row=0, column=1, sticky=W)

        self.button_b = tk.Radiobutton(self.left_Frame, text="Fixed Acidity and Wine Quality", variable=self.fd_var_wine_char, value=2)
        self.button_b.grid(row=1, column=1, sticky=W)

        self.button_c = tk.Radiobutton(self.left_Frame, text="Alcohol Percentage and Wine Quality", variable=self.fd_var_wine_char,
                               value=3)
        self.button_c.grid(row=2, column=1, sticky=W)

        self.button_d = tk.Radiobutton(self.left_Frame, text="Residual Sugar and Wine Quality", variable=self.fd_var_wine_char, value=4)
        self.button_d.grid(row=3, column=1, sticky=W)

        self.button_red = tk.Radiobutton(self.right_Frame, text="Red", variable=self.fd_var_wine_type, value=8)
        self.button_red.grid(row=0, column=0, sticky=W)

        self.button_white = tk.Radiobutton(self.right_Frame, text="White", variable=self.fd_var_wine_type, value=9)
        self.button_white.grid(row=1, column=0, sticky=W)

        self.freq_dist_value_lbl = tk.Label(self.middle_Frame, text="Please Enter a Value")
        self.freq_dist_value_lbl.pack(side=LEFT)
        self.freq_dist_value = tk.Entry(self.middle_Frame)
        self.freq_dist_value.pack(side=LEFT)

        self.button_enter = tk.Button(self.middle_bot_Frame, text="Submit", command=self.freq_dist_result,fg="green")
        self.button_enter.pack(side=BOTTOM, fill=X)

        self.back_button = tk.Button(self.bot_Frame, text="Main Menu", command=lambda: controller.show_frame("MenuFrame"))
        self.back_button.pack(side=LEFT)
        self.quit_button = tk.Button(self.bot_Frame, text="Quit", fg="red")
        self.quit_button.pack(side=RIGHT)

    def freq_dist_result(self):
        if self.fd_var_wine_char.get() == 1:
            self.wine_char = "volatile acidity"

            if self.fd_var_wine_type.get() == 8:
                print(self.fd_var_wine_type)
                print(self.fd_var_wine_char)

                wine_char_value = float(self.freq_dist_value.get())
                if wine_char_value > 1.58 or wine_char_value < 0.08 or wine_char_value == "":
                    tm.showerror("Error", "Incorrect Input. For all wines, the minimum value for volatile acidity is 0.08 and the max value is 1.58. Enter a numerical value for this characteristic within the given range (including lower and upper limits.)")
                else:
                    if wine_char_value > 0.668938:
                        tm.showinfo("ALERT", "The value you have entered is more than two standard deviations away from the mean volatile acidity for all wines.")

                    if wine_char_value > 0.14:
                        tm.showinfo("ALERT", "The value you have entered for volatile acidity is greater than the regulated amount set by the federal Tax & Trade Bureau. For red wines, the max volatile acidity allowed is 0.14. For white wines, the max volatile acidity allowed is 0.12. It is recommended that you blend an amount of volatile acidity in the wine that is no greater than the federally regulated limit.")

                    wine_char_2 = "quality"
                    all_wines = pd.read_csv('winequality-both.csv')

                    red = all_wines.loc[all_wines['type'] == 'red', :]

                    red_wine_char = red.loc[red[self.wine_char] == wine_char_value, :]

                    wine_char_value_data_set = red_wine_char.loc[:, wine_char_2]

                    seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
                    plt.title("Red Wine: " + self.wine_char + " value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
                    plt.ylabel('Number of wines')

                    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                    plt.show()


            if self.fd_var_wine_type.get() == 9:
                print(self.fd_var_wine_type)
                print(self.fd_var_wine_char)

                wine_char_value = float(self.freq_dist_value.get())
                if wine_char_value > 1.58 or wine_char_value < 0.08 or wine_char_value == "":
                    tm.showerror("Error", "Incorrect Input. For all wines, the minimum value for volatile acidity is 0.08 and the max value is 1.58. Enter a numerical value for this characteristic within the given range (including lower and upper limits.)")
                else:
                    if wine_char_value > 0.668938:
                        tm.showinfo("ALERT", "The value you have entered is more than two standard deviations away from the mean volatile acidity for all wines.")

                    if wine_char_value > 0.12:
                        tm.showinfo("ALERT", "The value you have entered for volatile acidity is greater than the regulated amount set by the federal Tax & Trade Bureau. For red wines, the max volatile acidity allowed is 0.14. For white wines, the max volatile acidity allowed is 0.12. It is recommended that you blend an amount of volatile acidity in the wine that is no greater than the federally regulated limit.")

                    wine_char_2 = "quality"
                    all_wines = pd.read_csv('winequality-both.csv')

                    white = all_wines.loc[all_wines['type'] == 'white', :]

                    white_wine_char = white.loc[white[self.wine_char] == wine_char_value, :]

                    wine_char_value_data_set = white_wine_char.loc[:, wine_char_2]

                    seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
                    plt.title("White Wine: " + self.wine_char + " value of " + str(
                            wine_char_value) + ", frequencies by " + wine_char_2)
                    plt.ylabel('Number of wines')

                    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                    plt.show()

        if self.fd_var_wine_char.get() == 2:
            wine_char = "fixed acidity"

            if self.fd_var_wine_type.get() == 8:
                print(self.fd_var_wine_type)
                print(self.fd_var_wine_char)

                wine_char_value = float(self.freq_dist_value.get())
                if wine_char_value > 15.9 or wine_char_value < 3.8 or wine_char_value == "":
                    tm.showerror("Error", "Incorrect Input. For all wines, the minimum value for fixed acidity is 3.8 and the max value is 15.9. Please enter a value within the given range (including lower and upper limits.)")
                else:
                    if wine_char_value > 12:
                        tm.showinfo("ALERT", "This high of an amount of fixed acidity can cause a wine to taste too sour. It is recommended that you blend a lower amount of fixed acidity into the wine.")

                    if wine_char_value > 9.808175:
                        tm.showinfo("ALERT", "The value you have entered is more than two standard deviations away from the mean fixed acidity for all wines.")

                    wine_char_2 = "quality"
                    all_wines = pd.read_csv('winequality-both.csv')

                    red = all_wines.loc[all_wines['type'] == 'red', :]

                    red_wine_char = red.loc[red[self.wine_char] == wine_char_value, :]

                    wine_char_value_data_set = red_wine_char.loc[:, wine_char_2]

                    seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
                    plt.title("Red Wine: " + self.wine_char + " value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
                    plt.ylabel('Number of wines')

                    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                    plt.show()

            if self.fd_var_wine_type.get() == 9:
                print(self.fd_var_wine_type)
                print(self.fd_var_wine_char)

                wine_char_value = float(self.freq_dist_value.get())
                if wine_char_value > 15.9 or wine_char_value < 3.8 or wine_char_value == "":
                    tm.showerror("Error", "Incorrect Input. For all wines, the minimum value for fixed acidity is 3.8 and the max value is 15.9. Please enter a value within the given range (including lower and upper limits.)")
                else:
                    if wine_char_value > 12:
                        tm.showinfo("ALERT", "This high of an amount of fixed acidity can cause a wine to taste too sour. It is recommended that you blend a lower amount of fixed acidity into the wine.")

                    if wine_char_value > 9.808175:
                        tm.showinfo("ALERT", "The value you have entered is more than two standard deviations away from the mean fixed acidity for all wines.")

                    wine_char_2 = "quality"
                    all_wines = pd.read_csv('winequality-both.csv')

                    white = all_wines.loc[all_wines['type'] == 'white', :]

                    white_wine_char = white.loc[white[self.wine_char] == wine_char_value, :]

                    wine_char_value_data_set = white_wine_char.loc[:, wine_char_2]

                    seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
                    plt.title("White Wine: " + self.wine_char + " value of " + str(
                            wine_char_value) + ", frequencies by " + wine_char_2)
                    plt.ylabel('Number of wines')

                    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                    plt.show()

        if self.fd_var_wine_char.get() == 3:
            wine_char = "alcohol"

            if self.fd_var_wine_type.get() == 8:
                print(self.fd_var_wine_type)
                print(self.fd_var_wine_char)

                wine_char_value = float(self.freq_dist_value.get())
                if wine_char_value > 14.9 or wine_char_value < 8 or wine_char_value == "":
                    tm.showerror("Error", "Incorrect Input. For all wines, the minimum value for alcohol percentage is 8 and the max value is 14.9. Enter a numerical value for this characteristic within the given range (including lower and upper limits.)")
                else:
                    if wine_char_value > 12.877224:
                        tm.showinfo("ALERT", "The value you have entered is more than two standard deviations away from the mean alcohol percentage for all wines.")

                    wine_char_2 = "quality"
                    all_wines = pd.read_csv('winequality-both.csv')

                    red = all_wines.loc[all_wines['type'] == 'red', :]

                    red_wine_char = red.loc[red[self.wine_char] == wine_char_value, :]

                    wine_char_value_data_set = red_wine_char.loc[:, wine_char_2]

                    seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
                    plt.title("Red Wine: " + self.wine_char + " value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
                    plt.ylabel('Number of wines')

                    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                    plt.show()

            if self.fd_var_wine_type.get() == 9:
                print(self.fd_var_wine_type)
                print(self.fd_var_wine_char)

                wine_char_value = float(self.freq_dist_value.get())
                if wine_char_value > 14.9 or wine_char_value < 8 or wine_char_value == "":
                    tm.showerror("Error", "Incorrect Input. For all wines, the minimum value for alcohol percentage is 8 and the max value is 14.9. Enter a numerical value for this characteristic within the given range (including lower and upper limits.)")
                else:
                    if wine_char_value > 12.877224:
                        tm.showinfo("ALERT", "The value you have entered is more than two standard deviations away from the mean alcohol percentage for all wines.")

                    wine_char_2 = "quality"
                    all_wines = pd.read_csv('winequality-both.csv')

                    white = all_wines.loc[all_wines['type'] == 'white', :]

                    white_wine_char = white.loc[white[self.wine_char] == wine_char_value, :]

                    wine_char_value_data_set = white_wine_char.loc[:, wine_char_2]

                    seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
                    plt.title("White Wine: " + self.wine_char + " value of " + str(
                            wine_char_value) + ", frequencies by " + wine_char_2)
                    plt.ylabel('Number of wines')

                    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                    plt.show()

        if self.fd_var_wine_char.get() == 4:
            wine_char = "residual sugar"

            if self.fd_var_wine_type.get() == 8:
                print(self.fd_var_wine_type)
                print(self.fd_var_wine_char)

                wine_char_value = float(self.freq_dist_value.get())
                if wine_char_value > 65.8 or wine_char_value < 0.6 or wine_char_value == "":
                    tm.showerror("Error", "Incorrect Input. For all wines, the minimum value for residual sugar is 0.6 and the max value is 65.8. Enter a numerical value for this characteristic within the given range (including lower and upper limits.)")
                else:
                    if wine_char_value < 4:
                        tm.showinfo("ALERT", "It is recommended you enter a value of 4 or greater for residual sugar so that your wine has some sweetness. If a wine has a low value for residual sugar, it is recommended that you DO NOT blend it with a dry wine.")
                    if wine_char_value >= 20:
                        tm.showinfo("ALERT", "Since this is a high value for residual sugar, it is recommended that you blend this wine with a dryer wine to balance out the overall taste.")
                    if wine_char_value > 14.958843:
                        tm.showinfo("ALERT", "The value you have entered is more than two standard deviations away from the mean residual sugar for all wines.")

                    wine_char_2 = "quality"
                    all_wines = pd.read_csv('winequality-both.csv')

                    red = all_wines.loc[all_wines['type'] == 'red', :]

                    red_wine_char = red.loc[red[self.wine_char] == wine_char_value, :]

                    wine_char_value_data_set = red_wine_char.loc[:, wine_char_2]

                    seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
                    plt.title("Red Wine: " + self.wine_char + " value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
                    plt.ylabel('Number of wines')

                    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                    plt.show()

            if self.fd_var_wine_type.get() == 9:
                print(self.fd_var_wine_type)
                print(self.fd_var_wine_char)

                wine_char_value = float(self.freq_dist_value.get())
                if wine_char_value > 65.8 or wine_char_value < 0.6 or wine_char_value == "":
                    tm.showerror("Error", "Incorrect Input. For all wines, the minimum value for residual sugar is 0.6 and the max value is 65.8. Enter a numerical value for this characteristic within the given range (including lower and upper limits.)")
                else:
                    if wine_char_value < 4:
                        tm.showinfo("ALERT", "It is recommended you enter a value of 4 or greater for residual sugar so that your wine has some sweetness. If a wine has a low value for residual sugar, it is recommended that you DO NOT blend it with a dry wine.")
                    if wine_char_value >= 20:
                        tm.showinfo("ALERT", "Since this is a high value for residual sugar, it is recommended that you blend this wine with a dryer wine to balance out the overall taste.")
                    if wine_char_value > 14.958843:
                        tm.showinfo("ALERT", "The value you have entered is more than two standard deviations away from the mean residual sugar for all wines.")

                    wine_char_2 = "quality"
                    all_wines = pd.read_csv('winequality-both.csv')

                    white = all_wines.loc[all_wines['type'] == 'white', :]

                    white_wine_char = white.loc[white[self.wine_char] == wine_char_value, :]

                    wine_char_value_data_set = white_wine_char.loc[:, wine_char_2]

                    seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
                    plt.title("White Wine: " + self.wine_char + " value of " + str(
                            wine_char_value) + ", frequencies by " + wine_char_2)
                    plt.ylabel('Number of wines')

                    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                    plt.show()

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("600x300+500+300")
    app.mainloop()
