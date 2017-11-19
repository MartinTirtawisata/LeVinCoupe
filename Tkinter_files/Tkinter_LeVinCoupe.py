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

#---------------------LOGIN---------------------
def t_login():
    global root_login
    global mainframe
    global entry_email
    global entry_password
    global var

    root_login = Tk()
    root_login.title("LeVinCoupe - Login")
    root_login.geometry('400x300+500+300')

    label_title = ttk.Label(root_login, text="Welcome to LeVinCoupe")
    label_title.grid(row=0, columnspan=3)

    label_email = ttk.Label(root_login, text="Email")
    label_password = ttk.Label(root_login, text="Password")
    button_sign_in = ttk.Button(root_login, text="Log in", command=t_check_login)
    label_email.grid(row=2, column=0, sticky=E)
    label_password.grid(row=3, column=0, sticky=E)
    button_sign_in.grid(row=4, column=2, sticky=E)

    entry_email = ttk.Entry(root_login)
    entry_password = ttk.Entry(root_login, show='*')
    entry_email.grid(row=2, column=1)
    entry_password.grid(row=3, column=1)

    var_check_login = IntVar()
    # this is a tkinter variable...??
    check = ttk.Checkbutton(root_login, text="Keep me signed in", command=t_checkState, variable=var_check_login)  # Remove bracket for function argument
    # command -- is one of the methods
    check.grid(row=4, column=0, columnspan=2)
    # column span to take two column
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
    root_menu.title("LeVinCoupe Title")

    top_Frame = Frame(root_menu)
    top_Frame.pack(side=TOP)

    back_button = ttk.Button(top_Frame, text="Back", command=t_login)
    back_button.pack(side=LEFT)

    button_A = Button(root_menu, text="Register an Employee", command=t_menu_register)
    button_A.pack()

    button_B = Button(root_menu, text="Associate Wine's Characteristic and Quality", command=t_menu_association)
    button_B.pack()

    button_C = Button(root_menu, text="Test Wine Characteristic Frequency Distribution based on Quality", command=t_menu_freq_distribution)
    button_C.pack()

    button_D = Button(root_menu, text="Ask Additional Questions or Add Additional Features")
    button_D.pack()

    button_E = Button(root_menu, text="Quit", fg="red")
    button_E.pack()

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
    #Need Employee ID, First Name, Last Name,  Address, City, State, Zip Code, Email, Password
    root_register = Tk()
    root_register.title("LeVinCoupe Employee Register")

    label_emp_id = Label(root_register, text="Enter Employee ID")
    label_emp_id.grid(row=0, column=0)
    entry_emp_id = Entry(root_register)
    entry_emp_id.grid(row=0, column=1)

    label_fname = Label(root_register, text="Enter First Name")
    label_fname.grid(row=1, column=0)
    entry_fname = Entry(root_register)
    entry_fname.grid(row=1, column=1)

    label_lname = Label(root_register, text="Enter Last Name")
    label_lname.grid(row=2, column=0)
    entry_lname = Entry(root_register)
    entry_lname.grid(row=2, column=1)

    label_address = Label(root_register, text="Enter Address")
    label_address.grid(row=3, column=0)
    entry_address = Entry(root_register)
    entry_address.grid(row=3, column=1)

    label_city = Label(root_register, text="Enter City")
    label_city.grid(row=4, column=0)
    entry_city = Entry(root_register)
    entry_city.grid(row=4, column=1)

    label_state = Label(root_register, text="Enter State")
    label_state.grid(row=5, column=0)
    entry_state = Entry(root_register)
    entry_state.grid(row=5, column=1)

    label_zip_code = Label(root_register, text="Enter Zip Code")
    label_zip_code.grid(row=6, column=0)
    entry_zip_code = Entry(root_register)
    entry_zip_code.grid(row=6, column=1)

    label_email = Label(root_register, text="Enter Email")
    label_email.grid(row=7, column=0)
    entry_email = Entry(root_register)
    entry_email.grid(row=7, column=1)

    label_password = Label(root_register, text="Enter Password")
    label_password.grid(row=8, column=0)
    entry_password = Entry(root_register)
    entry_password.grid(row=8, column=1)

    button_sign_up = Button(root_register, text="Sign Up", command=t_insert_registration)
    button_sign_up.grid(columnspan=3)
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
    root_association.title("LeVinCoupe Association")

    var_wine_char = IntVar()
    var_wine_type = IntVar()


    button_a = Radiobutton(root_association, text="Volatile Acidity and Wine Quality", variable=var_wine_char, value=1)
    button_a.pack()

    button_b = Radiobutton(root_association, text="Fixed Acidity and Wine Quality", variable=var_wine_char, value=2)
    button_b.pack()

    button_c = Radiobutton(root_association, text="Alcohol Percentage and Wine Quality", variable=var_wine_char, value=3)
    button_c.pack()

    button_d = Radiobutton(root_association, text="Residual Sugar and Wine Quality", variable=var_wine_char, value=4)
    button_d.pack()

    button_red = Radiobutton(root_association, text="Red", variable=var_wine_type, value=8)
    button_red.pack()

    button_white = Radiobutton(root_association, text="White", variable=var_wine_type, value=9)
    button_white.pack()

    button_enter = Button(root_association, text="Submit", command=t_association_result)
    button_enter.pack()

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


    root_freq_dist = Tk()
    root_freq_dist.title("LeVinCoupe Frequency Distribution")

    #users will choose wine characteristics
    #users will choose wine type
    #users will enter a value

    fd_var_wine_char = IntVar()
    fd_var_wine_type = IntVar()

    button_a = Radiobutton(root_freq_dist, text="Volatile Acidity and Wine Quality", variable=fd_var_wine_char, value=1)
    button_a.pack()

    button_b = Radiobutton(root_freq_dist, text="Fixed Acidity and Wine Quality", variable=fd_var_wine_char, value=2)
    button_b.pack()

    button_c = Radiobutton(root_freq_dist, text="Alcohol Percentage and Wine Quality", variable=fd_var_wine_char,
                           value=3)
    button_c.pack()

    button_d = Radiobutton(root_freq_dist, text="Residual Sugar and Wine Quality", variable=fd_var_wine_char, value=4)
    button_d.pack()

    button_red = Radiobutton(root_freq_dist, text="Red", variable=fd_var_wine_type, value=8)
    button_red.pack()

    button_white = Radiobutton(root_freq_dist, text="White", variable=fd_var_wine_type, value=9)
    button_white.pack()

    freq_dist_value = Entry(root_freq_dist)
    freq_dist_value.pack()

    button_enter = Button(root_freq_dist, text="Submit", command=t_freq_dist_result)
    button_enter.pack()


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
