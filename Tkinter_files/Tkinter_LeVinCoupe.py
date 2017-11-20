import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import pandas as pd
import scipy.stats
import seaborn
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tm
import sqlite3


#import matplotlib, Matplotlib(TkAgg),

# (t) in front is to indicate that it is a tkinter function
# (check) a function that validates

def start_program():
    t_login()

def pressed_main_menu_r():
    root_register.destroy()
    return t_main_menu()

def pressed_main_menu_a():
    root_association.destroy()
    return t_main_menu()

def pressed_main_menu_fd():
    root_freq_dist.destroy()
    return t_main_menu()

def quit_button_m():
    root_menu.destroy()
def quit_button_r():
    root_register.destroy()
def quit_button_a():
    root_association.destroy()
def quit_button_fd():
    root_freq_dist.destroy()

#---------------------LOGIN---------------------
def t_login():
    global root_login
    global mainframe
    global entry_email
    global entry_password
    global var


    root_login = Tk()
    root_login.title("LeVinCoupe - Login")
    root_login.geometry('450x200+500+300')

    topFrame = Frame(root_login, bg="purple")
    topFrame.pack(side=TOP,fill=X)

    midFrame = Frame(root_login)
    midFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

    label_title = ttk.Label(topFrame, text="Welcome to LeVinCoupe")
    label_title.pack()

    label_email = ttk.Label(midFrame, text="Email")
    label_email.grid(row=0, column=2, sticky=E)
    entry_email = ttk.Entry(midFrame)
    entry_password = ttk.Entry(midFrame, show='*')

    label_password = ttk.Label(midFrame, text="Password")
    label_password.grid(row=1, column=2, sticky=E)
    entry_email.grid(row=0, column=3, columnspan=2)
    entry_password.grid(row=1, column=3, columnspan=2)

    var_check_login = IntVar()
    check = ttk.Checkbutton(midFrame, text="Keep me signed in", command=t_checkState, variable=var_check_login)
    check.grid(row=2, column=3, sticky=E)

    button_sign_in = ttk.Button(midFrame, text="Log in", command=t_check_login)
    button_sign_in.grid(row=2, column=4)

    root_login.mainloop()

def t_check_login():
    userEmail = str(entry_email.get())
    userPassword = str(entry_password.get())

    try:
        with sqlite3.connect('LeVinEmployee.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Employee WHERE(Email = '" + userEmail + "') AND (Password = '" + userPassword + "')")
            query_result = cursor.fetchone()
            print(query_result)
    except (KeyError) as e:
        print(e)

    if userEmail == query_result[7] and userPassword == query_result[8]:
        root_login.destroy()
        return t_main_menu()


def t_checkState():
    #this prints out the type of data
    if var_check_login.get() == 1:
        print("checkbox is checked")
        print(var_check_login)
    else:
        print("not checked")

#--------------------------------------MENU---------------------------------
def t_main_menu():
    global root_menu
    root_menu = Tk()
    root_menu.title("LeVinCoupe - Menu")
    root_menu.geometry('450x200+500+300')

    top_Frame = Frame(root_menu, bg="yellow")
    top_Frame.pack(side=TOP, fill=BOTH, expand=True)
    bot_Frame = Frame(root_menu, bg="green")
    bot_Frame.pack(side=BOTTOM, fill=X)

    button_A = Button(top_Frame, text="Register other employees", command=t_menu_register)
    button_A.pack(fill=X)

    button_B = Button(top_Frame, text="Test wine associations based on characteristic & quality", command=t_menu_association)
    button_B.pack(fill=X)

    button_C = Button(top_Frame, text="Create wine frequency distribution based on value of wine characteristic & quality", command=t_menu_freq_distribution)
    button_C.pack(fill=X)

    button_D = Button(top_Frame, text="Test wine associations based on user inputted characteristics")
    button_D.pack(fill=X)

    back_button = ttk.Button(bot_Frame, text="Back", command=t_login)
    back_button.pack(side=LEFT)
    quit_button = Button(bot_Frame, text="Quit", fg="red", command=quit_button_m)
    quit_button.pack(side=RIGHT)

    root_menu.mainloop()

#------------------------------------------------REGISTER---------------------------------------
def t_menu_register():
    root_menu.destroy()
    return t_register()

def t_register():
    global entry_emp_id
    global entry_fname
    global entry_lname
    global entry_address
    global entry_city
    global entry_state
    global entry_zip_code
    global entry_email
    global entry_password
    global root_register
    #Need Employee ID, First Name, Last Name,  Address, City, State, Zip Code, Email, Password
    root_register = Tk()
    root_register.title("LeVinCoupe - Employee Registration")
    root_register.geometry('400x300+500+300')

    top_Frame = Frame(root_register)
    top_Frame.pack(side=TOP)
    bot_Frame = Frame(root_register)
    bot_Frame.pack(side=BOTTOM, fill=X)

    label_emp_id = Label(top_Frame, text="Enter Employee ID")
    label_emp_id.grid(row=0, column=0)
    entry_emp_id = Entry(top_Frame)
    entry_emp_id.grid(row=0, column=1)

    label_fname = Label(top_Frame, text="Enter First Name")
    label_fname.grid(row=1, column=0)
    entry_fname = Entry(top_Frame)
    entry_fname.grid(row=1, column=1)

    label_lname = Label(top_Frame, text="Enter Last Name")
    label_lname.grid(row=2, column=0)
    entry_lname = Entry(top_Frame)
    entry_lname.grid(row=2, column=1)

    label_address = Label(top_Frame, text="Enter Address")
    label_address.grid(row=3, column=0)
    entry_address = Entry(top_Frame)
    entry_address.grid(row=3, column=1)

    label_city = Label(top_Frame, text="Enter City")
    label_city.grid(row=4, column=0)
    entry_city = Entry(top_Frame)
    entry_city.grid(row=4, column=1)

    label_state = Label(top_Frame, text="Enter State")
    label_state.grid(row=5, column=0)
    entry_state = Entry(top_Frame)
    entry_state.grid(row=5, column=1)

    label_zip_code = Label(top_Frame, text="Enter Zip Code")
    label_zip_code.grid(row=6, column=0)
    entry_zip_code = Entry(top_Frame)
    entry_zip_code.grid(row=6, column=1)

    label_email = Label(top_Frame, text="Enter Email")
    label_email.grid(row=7, column=0)
    entry_email = Entry(top_Frame)
    entry_email.grid(row=7, column=1)

    label_password = Label(top_Frame, text="Enter Password")
    label_password.grid(row=8, column=0)
    entry_password = Entry(top_Frame)
    entry_password.grid(row=8, column=1)

    button_sign_up = Button(top_Frame, text="Sign Up", command=t_insert_registration)
    button_sign_up.grid(columnspan=3)

    back_button = Button(bot_Frame, text="Main Menu", command=pressed_main_menu_r)
    back_button.pack(side=LEFT)
    quit_button = Button(bot_Frame, text="Quit", fg='red', command=quit_button_r)
    quit_button.pack(side=RIGHT)

    root_register.mainloop()

def t_insert_registration():

    userEmp_id = entry_emp_id.get()
    userF_name = str(entry_fname.get())
    userL_name = str(entry_lname.get())
    userAddress = str(entry_address.get())
    userCity = str(entry_city.get())
    userState = str(entry_state.get())
    userZip_code = str(entry_zip_code.get())
    userEmail = str(entry_email.get())
    userPassword = str(entry_password.get())

    try:
        with sqlite3.connect('LeVinEmployee.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Employee VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (userEmp_id, userF_name, userL_name, userAddress, userCity, userState, userZip_code, userEmail, userPassword))
            query_result = cursor.fetchall()
            print(query_result)
    except sqlite3.Error as e:
        print(e)


#------------------------------------ASSOCIATION--------------------------------------------------------

def t_menu_association():
    root_menu.destroy()
    return t_association()

def t_association():
    global root_association
    global var_wine_char
    global var_wine_type

    root_association = Tk()
    root_association.title("LeVinCoupe - Association")
    root_association.geometry('450x200+500+300')

    top_Frame = Frame(root_association)
    top_Frame.pack(side=TOP)
    left_Frame = Frame(top_Frame, bg="green")
    left_Frame.pack(side=LEFT, fill=BOTH, expand=True)
    right_Frame = Frame(top_Frame, bg="blue")
    right_Frame.pack(side=RIGHT, fill=BOTH, expand=True)

    middle_Frame = Frame(root_association, bg="purple")
    middle_Frame.pack(side=TOP, fill=X)
    bot_Frame = Frame(root_association)
    bot_Frame.pack(side=BOTTOM, fill=X)

    var_wine_char = IntVar()
    var_wine_type = IntVar()


    button_a = Radiobutton(left_Frame, text="Volatile Acidity and Wine Quality", variable=var_wine_char, value=1)
    button_a.grid(row=0, column=1, sticky=W)

    button_b = Radiobutton(left_Frame, text="Fixed Acidity and Wine Quality", variable=var_wine_char, value=2)
    button_b.grid(row=1, column=1, sticky=W)

    button_c = Radiobutton(left_Frame, text="Alcohol Percentage and Wine Quality", variable=var_wine_char, value=3)
    button_c.grid(row=2, column=1, sticky=W)

    button_d = Radiobutton(left_Frame, text="Residual Sugar and Wine Quality", variable=var_wine_char, value=4)
    button_d.grid(row=3, column=1, sticky=W)

    button_red = Radiobutton(right_Frame, text="Red", variable=var_wine_type, value=8)
    button_red.grid(row=0, column=0, sticky=W)

    button_white = Radiobutton(right_Frame, text="White", variable=var_wine_type, value=9)
    button_white.grid(row=1, column=0, sticky=W)

    button_enter = Button(middle_Frame, text="Submit", command=t_association_result, fg="green")
    button_enter.pack(fill=X)

    back_button = ttk.Button(bot_Frame, text="Main Menu", command=pressed_main_menu_a)
    back_button.pack(side=LEFT)
    quit_button = Button(bot_Frame, text="Quit", fg="red", command=quit_button_a)
    quit_button.pack(side=RIGHT)



    root_association.mainloop()

def t_association_result():
    if var_wine_char.get() == 1:
        if var_wine_type.get() == 8:
            print(var_wine_char)
            print(var_wine_type)

            try:
                WineCharX = "quality"
                WineCharY = "volatile acidity"
                allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                red = allWines.loc[allWines['type'] == 'red', :]

                getCorr = scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
                correlation = str(getCorr[0])
                pValue = str(getCorr[1])
                print(
                "\nFor red wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                print("With p-value of: " + pValue)

                seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
                plt.xlabel(WineCharX)
                plt.ylabel(WineCharY)
                plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
                plt.show()

            except (KeyError) as e:
                print(
                "\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")

        if var_wine_type.get() == 9:
            print(var_wine_char)
            print(var_wine_type)

            try:
                WineCharX = "quality"
                WineCharY = "volatile acidity"
                allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                white = allWines.loc[allWines['type'] == 'white', :]

                getCorr = scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
                correlation = str(getCorr[0])
                pValue = str(getCorr[1])
                print(
                    "\nFor white wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                print("With p-value of: " + pValue)

                seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
                plt.xlabel(WineCharX)
                plt.ylabel(WineCharY)
                plt.title("White Wine: " + WineCharX + " X " + WineCharY)
                plt.show()

            except (KeyError) as e:
                print(
                    "\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")
#---------------------------------------FIXED ACIDITY--------------------------------------
    if var_wine_char.get() == 2:
        if var_wine_type.get() == 8:
            print(var_wine_char)
            print(var_wine_type)

            try:
                WineCharX = "quality"
                WineCharY = "fixed acidity"
                allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                red = allWines.loc[allWines['type'] == 'red', :]

                getCorr = scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
                correlation = str(getCorr[0])
                pValue = str(getCorr[1])
                print(
                    "\nFor red wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                print("With p-value of: " + pValue)

                seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
                plt.xlabel(WineCharX)
                plt.ylabel(WineCharY)
                plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
                plt.show()

            except (KeyError) as e:
                print(
                    "\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")

        if var_wine_type.get() == 9:
            print(var_wine_char)
            print(var_wine_type)

            try:
                WineCharX = "quality"
                WineCharY = "fixed acidity"
                allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                white = allWines.loc[allWines['type'] == 'white', :]

                getCorr = scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
                correlation = str(getCorr[0])
                pValue = str(getCorr[1])
                print(
                    "\nFor white wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                print("With p-value of: " + pValue)

                seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
                plt.xlabel(WineCharX)
                plt.ylabel(WineCharY)
                plt.title("White Wine: " + WineCharX + " X " + WineCharY)
                plt.show()

            except (KeyError) as e:
                print(
                    "\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")
#-----------------------------------------------ALCOHOL-------------------------------------------------------------
    if var_wine_char.get() == 3:
        if var_wine_type.get() == 8:
            print(var_wine_char)
            print(var_wine_type)

            try:
                WineCharX = "quality"
                WineCharY = "alcohol"
                allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                red = allWines.loc[allWines['type'] == 'red', :]

                getCorr = scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
                correlation = str(getCorr[0])
                pValue = str(getCorr[1])
                print(
                    "\nFor red wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                print("With p-value of: " + pValue)

                seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
                plt.xlabel(WineCharX)
                plt.ylabel(WineCharY)
                plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
                plt.show()

            except (KeyError) as e:
                print(
                    "\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")

        if var_wine_type.get() == 9:
            print(var_wine_char)
            print(var_wine_type)

            try:
                WineCharX = "quality"
                WineCharY = "alcohol"
                allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                white = allWines.loc[allWines['type'] == 'white', :]

                getCorr = scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
                correlation = str(getCorr[0])
                pValue = str(getCorr[1])
                print(
                    "\nFor white wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                print("With p-value of: " + pValue)

                seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
                plt.xlabel(WineCharX)
                plt.ylabel(WineCharY)
                plt.title("White Wine: " + WineCharX + " X " + WineCharY)
                plt.show()

            except (KeyError) as e:
                print(
                    "\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")
#---------------------------------------------------RESIDUAL SUGAR -----------------------------------------------
    if var_wine_char.get() == 4:
        if var_wine_type.get() == 8:
            print(var_wine_char)
            print(var_wine_type)

            try:
                WineCharX = "quality"
                WineCharY = "residual sugar"
                allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                red = allWines.loc[allWines['type'] == 'red', :]

                getCorr = scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
                correlation = str(getCorr[0])
                pValue = str(getCorr[1])
                print(
                    "\nFor red wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                print("With p-value of: " + pValue)

                seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
                plt.xlabel(WineCharX)
                plt.ylabel(WineCharY)
                plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
                plt.show()

            except (KeyError) as e:
                print(
                    "\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")

        if var_wine_type.get() == 9:
            print(var_wine_char)
            print(var_wine_type)

            try:
                WineCharX = "quality"
                WineCharY = "residual sugar"
                allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                white = allWines.loc[allWines['type'] == 'white', :]

                getCorr = scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
                correlation = str(getCorr[0])
                pValue = str(getCorr[1])
                print(
                    "\nFor white wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                print("With p-value of: " + pValue)

                seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
                plt.xlabel(WineCharX)
                plt.ylabel(WineCharY)
                plt.title("White Wine: " + WineCharX + " X " + WineCharY)
                plt.show()

            except (KeyError) as e:
                print(
                    "\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")


            # f = Figure(figsize=(5, 5), dpi=100)
# a = f.add_subplot(111)
# a.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 6, 1, 3, 8, 9, 3, 5, 8, 8])
# # this is the X axis                       this is the graph
#
# canvas = FigureCanvasTkAgg(f, master=root_association)
# canvas.show()
# canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#------------------------------------------------FREQUENCY DISTRIBUTOIN-----------------------

def t_menu_freq_distribution():
    root_menu.destroy()
    return t_freq_distribution()

def t_freq_distribution():
    global freq_dist_value
    global fd_var_wine_char
    global fd_var_wine_type
    global root_freq_dist


    root_freq_dist = Tk()
    root_freq_dist.title("LeVinCoupe - Frequency Distribution")
    root_freq_dist.geometry('450x200+500+300')

    top_Frame = Frame(root_freq_dist)
    top_Frame.pack(side=TOP)
    left_Frame = Frame(top_Frame)
    left_Frame.pack(side=LEFT, fill=BOTH, expand=True)
    right_Frame = Frame(top_Frame)
    right_Frame.pack(side=RIGHT, fill=BOTH, expand=True)

    middle_Frame = Frame(root_freq_dist)
    middle_Frame.pack(side=TOP, fill=X)

    middle_bot_Frame = Frame(root_freq_dist)
    middle_bot_Frame.pack(side=TOP, fill=X)

    bot_Frame = Frame(root_freq_dist)
    bot_Frame.pack(side=BOTTOM, fill=X)


    fd_var_wine_char = IntVar()
    fd_var_wine_type = IntVar()

    button_a = Radiobutton(left_Frame, text="Volatile Acidity and Wine Quality", variable=fd_var_wine_char, value=1)
    button_a.grid(row=0, column=1, sticky=W)

    button_b = Radiobutton(left_Frame, text="Fixed Acidity and Wine Quality", variable=fd_var_wine_char, value=2)
    button_b.grid(row=1, column=1, sticky=W)

    button_c = Radiobutton(left_Frame, text="Alcohol Percentage and Wine Quality", variable=fd_var_wine_char,
                           value=3)
    button_c.grid(row=2, column=1, sticky=W)

    button_d = Radiobutton(left_Frame, text="Residual Sugar and Wine Quality", variable=fd_var_wine_char, value=4)
    button_d.grid(row=3, column=1, sticky=W)

    button_red = Radiobutton(right_Frame, text="Red", variable=fd_var_wine_type, value=8)
    button_red.grid(row=0, column=0, sticky=W)

    button_white = Radiobutton(right_Frame, text="White", variable=fd_var_wine_type, value=9)
    button_white.grid(row=1, column=0, sticky=W)

    freq_dist_value_lbl = Label(middle_Frame, text="Please Enter a Value")
    freq_dist_value_lbl.pack(side=LEFT)
    freq_dist_value = Entry(middle_Frame)
    freq_dist_value.pack(side=LEFT)

    button_enter = Button(middle_bot_Frame, text="Submit", command=t_freq_dist_result, fg="green")
    button_enter.pack(side=BOTTOM, fill=X)

    back_button = ttk.Button(bot_Frame, text="Main Menu", command=pressed_main_menu_fd)
    back_button.pack(side=LEFT)
    quit_button = Button(bot_Frame, text="Quit", fg="red", command=quit_button_fd)
    quit_button.pack(side=RIGHT)

    root_freq_dist.mainloop()

def t_freq_dist_result():
    if fd_var_wine_char.get() == 1:
        wine_char = "volatile acidity"

        if fd_var_wine_type.get() == 8:
            print(fd_var_wine_type)
            print(fd_var_wine_char)

            wine_char_value = int(freq_dist_value.get())
            wine_char_2 = "quality"
            all_wines = pd.read_csv('winequality-both.csv')

            red = all_wines.loc[all_wines['type'] == 'red', :]

            red_wine_char = red.loc[red[wine_char] == wine_char_value, :]

            wine_char_value_data_set = red_wine_char.loc[:, wine_char_2]

            seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
            plt.title(
                "Red Wine: " + wine_char + " value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
            plt.ylabel('Number of wines')

            plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            plt.show()

        if fd_var_wine_type.get() == 9:
            print(fd_var_wine_type)
            print(fd_var_wine_char)

            wine_char_value = int(freq_dist_value.get())
            wine_char_2 = "quality"
            all_wines = pd.read_csv('winequality-both.csv')

            white = all_wines.loc[all_wines['type'] == 'white', :]

            white_wine_char = white.loc[white[wine_char] == wine_char_value, :]

            wine_char_value_data_set = white_wine_char.loc[:, wine_char_2]

            seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
            plt.title(
                "White Wine: " + wine_char + " value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
            plt.ylabel('Number of wines')

            plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            plt.show()

    if fd_var_wine_char.get() == 2:
        wine_char = "fixed acidity"

        if fd_var_wine_type.get() == 8:
            print(fd_var_wine_type)
            print(fd_var_wine_char)

            wine_char_value = int(freq_dist_value.get())
            wine_char_2 = "quality"
            all_wines = pd.read_csv('winequality-both.csv')

            red = all_wines.loc[all_wines['type'] == 'red', :]

            red_wine_char = red.loc[red[wine_char] == wine_char_value, :]

            wine_char_value_data_set = red_wine_char.loc[:, wine_char_2]

            seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
            plt.title(
                "Red Wine: " + wine_char + " value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
            plt.ylabel('Number of wines')

            plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            plt.show()

        if fd_var_wine_type.get() == 9:
            print(fd_var_wine_type)
            print(fd_var_wine_char)

            wine_char_value = int(freq_dist_value.get())
            wine_char_2 = "quality"
            all_wines = pd.read_csv('winequality-both.csv')

            white = all_wines.loc[all_wines['type'] == 'white', :]

            white_wine_char = white.loc[white[wine_char] == wine_char_value, :]

            wine_char_value_data_set = white_wine_char.loc[:, wine_char_2]

            seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
            plt.title(
                "White Wine: " + wine_char + " value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
            plt.ylabel('Number of wines')

            plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            plt.show()

    if fd_var_wine_char.get() == 3:
        wine_char = "alcohol"

        if fd_var_wine_type.get() == 8:
            print(fd_var_wine_type)
            print(fd_var_wine_char)

            wine_char_value = int(freq_dist_value.get())
            wine_char_2 = "quality"
            all_wines = pd.read_csv('winequality-both.csv')

            red = all_wines.loc[all_wines['type'] == 'red', :]

            red_wine_char = red.loc[red[wine_char] == wine_char_value, :]

            wine_char_value_data_set = red_wine_char.loc[:, wine_char_2]

            seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
            plt.title(
                "Red Wine: " + wine_char + " value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
            plt.ylabel('Number of wines')

            plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            plt.show()

        if fd_var_wine_type.get() == 9:
            print(fd_var_wine_type)
            print(fd_var_wine_char)

            wine_char_value = int(freq_dist_value.get())
            wine_char_2 = "quality"
            all_wines = pd.read_csv('winequality-both.csv')

            white = all_wines.loc[all_wines['type'] == 'white', :]

            white_wine_char = white.loc[white[wine_char] == wine_char_value, :]

            wine_char_value_data_set = white_wine_char.loc[:, wine_char_2]

            seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
            plt.title(
                "White Wine: " + wine_char + " value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
            plt.ylabel('Number of wines')

            plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            plt.show()

    if fd_var_wine_char.get() == 4:
        wine_char = "residual sugar"

        if fd_var_wine_type.get() == 8:
            print(fd_var_wine_type)
            print(fd_var_wine_char)

            wine_char_value = int(freq_dist_value.get())
            wine_char_2 = "quality"
            all_wines = pd.read_csv('winequality-both.csv')

            red = all_wines.loc[all_wines['type'] == 'red', :]

            red_wine_char = red.loc[red[wine_char] == wine_char_value, :]

            wine_char_value_data_set = red_wine_char.loc[:, wine_char_2]

            seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
            plt.title(
                "Red Wine: " + wine_char + " value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
            plt.ylabel('Number of wines')

            plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            plt.show()

        if fd_var_wine_type.get() == 9:
            print(fd_var_wine_type)
            print(fd_var_wine_char)

            wine_char_value = int(freq_dist_value.get())
            wine_char_2 = "quality"
            all_wines = pd.read_csv('winequality-both.csv')

            white = all_wines.loc[all_wines['type'] == 'white', :]

            white_wine_char = white.loc[white[wine_char] == wine_char_value, :]

            wine_char_value_data_set = white_wine_char.loc[:, wine_char_2]

            seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
            plt.title(
                "White Wine: " + wine_char + " value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
            plt.ylabel('Number of wines')

            plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            plt.show()



#------------------------Main System-----------------

start_program()
