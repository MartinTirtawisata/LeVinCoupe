import sqlite3
conn = sqlite3.connect('LeVinEmployee.db')

# Login

def Login():

    print("\n===============================================================================")
    print("                          WELCOME TO LE VIN COUPE")
    print("                Where wine and quality engineering collide!")
    print("===============================================================================")


    with conn:
        cur = conn.cursor()

        while True:
            print("\nEnter your credentials below to login to the system.")
            userEmail = input("\nPlease enter your email: ").strip()
            userPassword = input("Please enter your password: ").strip()

            if userEmail == "" or userPassword == "":
                print("\nYou did not enter an email or password. Please try again.")
            else:

                try:
                    cur.execute("SELECT * FROM Employee WHERE(Email = '" + userEmail + "') AND (Password = '" + userPassword + "')")

                    results = cur.fetchall()

                    if userEmail == results[0][7] and userPassword == results[0][8]:
                        print("\nLogin successful")
                        break
                except:
                    print("\nConnection Failed. You entered a wrong email or password. Please try again.")


# Menu

def Menu():
    print("\n===============================================================================")
    print("a. Register other employees")
    print("b. Test wine associations based on characteristic and quality")
    print("c. Create wine frequency distribution based on value of wine characteristic and wine quality")
    print("d. Ask additional questions or add features")
    print("e. Quit")
    print("===============================================================================")

    while True:
        menu_choice = input("\nPlease select an option from the following (enter the letter): ").lower().strip()
        if menu_choice == "a" or menu_choice == "b" or menu_choice == "c" or menu_choice == "d" or menu_choice == "e":
            break
        else:
            print("\nYou must select only one menu choice from above by typing the letter. Please try again.")

# Menu Options

    if menu_choice == "a":
        Registration()
    if menu_choice == "b":
        Association()
    #if menu_choice == "c":
        #Distribution()
    #if menu_choice == "d":
        #Additional()
    if menu_choice == "e":
        print("\nHave a great day!")


# Registration

def Registration():
    print("\nYou selected the option to register a new employee.")
    while True:
        empID = input("\nTo register a new employee, please enter a new 4 digit employee ID: ").strip()
        if empID and empID.isdigit() and len(empID) == 4:
            break
        else:
            print("\nThe employee ID cannot be left blank and must only contain a 4 digit number. Please try again.")

    with conn:
        cur = conn.cursor()

        try:
            cur.execute("SELECT COUNT (*) FROM Employee WHERE (EmployeeID = '" + empID + "')")
            results = cur.fetchone()

            while results[0] == 1:
                while True:
                    empID = input("\nThat employee ID is already in use. Please try entering a different one: ").strip()
                    if empID and empID.isdigit() and len(empID) == 4:
                        break
                    else:
                        print("\nThe employee ID cannot be left blank and must only contain a 4 digit number. Please try again.")

                cur.execute("SELECT COUNT (*) FROM Employee WHERE (EmployeeID = '" + empID + "')")
                results = cur.fetchone()
            print("\nThe employee ID " + empID + " is accepted.")
            # Add 'return empID' here when you convert registration into function - I don't think we need this but she had it in her example.
        except sqlite3.Error as e:
            print("\n")
            print(e)
    # empID = idCheck() - I don't think we need this but she had it in her example. Leaving it just in case.

    while True:
        firstName = input("\nNext, enter the employee's first name: ").strip().title()
        if firstName:
            break
        else:
            print("\nThe employee's first name cannot be left blank and can only contain letters. Please try again.")

    while True:
        lastName = input("\nEnter the employee's last name: ").strip().title()
        if lastName:
            break
        else:
            print("\nThe employee's last name cannot be left blank and can only contain letters. Please try again.")

    while True:
        address = input("\nEnter the employee's street address: ").strip()
        if address:
            break
        else:
            print("\nThe employee's address cannot be left blank. Please try again.")

    while True:
        city = input("\nEnter the employees's city: ").strip().title()
        if city:
            break
        else:
            print("\nThe employee's city cannot be left blank and can only contain letters. Please try again.")

    while True:
        state = input("\nEnter the employee's state (enter the two letter abbreviation for the state): ").strip().upper()
        if state and state.isalpha() and len(state) == 2:
            break
        else:
            print("\nThe employee's state cannot be left blank and can only contain letters. Please try again.")

    while True:
        zipCode = input("\nEnter the employee's zip code: ").strip()
        if zipCode and zipCode.isdigit() and len(zipCode) == 5:
            break
        else:
            print("\nThe employee's zip code cannot be left blank and can only contain a 5 digit number. Please try again.")

    # def emailCheck(): - I don't think we need this but she had it in her example. Leaving it just in case.
    while True:
        email = input("\nEnter the employee's email: ").strip()
        if email:
            break
        else:
            print("\nThe employee's email cannot be left blank. Please try again.")

    with conn:
        cur = conn.cursor()

        try:
            cur.execute("SELECT COUNT (*) FROM Employee WHERE (Email = '" + email + "')")
            results = cur.fetchone()

            while results[0] == 1:
                while True:
                    email = input("\nThat employee email is already in use. Please try entering a different one: ").strip()
                    if email:
                        break
                    else:
                        print("\nThe employee's email cannot be left blank. Please try again.")

                cur.execute("SELECT COUNT (*) FROM Employee WHERE (Email = '" + email + "')")
                results = cur.fetchone()
            print("\nThe employee email " + email + " is accepted.")
            # Add 'return email' here when you convert registration into function - I don't think we need this but she had it in her example.
        except sqlite3.Error as e:
            print("\n")
            print(e)
    # email = emailCheck() - I don't think we need this but she had it in her example. Leaving it just in case.

    while True:
        password = input("\nEnter a password for the employee account: ")
        if password:
            break
        else:
            print("\nThe employee's password cannot be left blank. Please try again.")

    with conn:
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO Employee VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (empID, firstName, lastName, address, city, state, zipCode, email, password))
        except sqlite3.Error as e:
            print("\n")
            print(e)

    print("\nEmployee successfully registered!")

    while True:
        after = input("\nWould you like to return to the main menu or quit? Type 'main' or 'quit': ").lower().strip()
        if after == "main":
            Menu()
            break
        if after == "quit":
            print("\nHave a great day!")
            break
        if after != "main" or after != "quit":
                print("\nYou must type either 'main' or 'quit' based on what you want to do. Please try again.")

def Association():
    import pandas as pd
    import scipy.stats
    import seaborn
    import matplotlib.pyplot as plt

    print("\n===============================================================================")
    print("a. Volatile Acidity and Wine Quality")
    print("b. Fixed Acidity and Wine Quality")
    print("c. Alcohol and Wine Quality")
    print("d. Residual Sugar and Wine Quality")
    print("===============================================================================")

    while True:
        association_choice = input("\nPlease select an option of which associations you would like to check (enter the letter): ").strip().lower()
        if association_choice == "a" or association_choice == "b" or association_choice == "c" or association_choice == "d":
            break
        else:
            print("\nYou must select only one menu choice from above by typing the letter. Please try again.")

    if association_choice == "a":

        while True:
            wine_choice = input("\nWould like to test for red or white wine? (enter 'red' or 'white'): ").strip().lower()

            if wine_choice == "red":
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
                break

            if wine_choice == "white":
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
                break

            if wine_choice != "red" or wine_choice != "white":
                print("\nYou must enter either 'red' or 'white' based on which wine you want to test associations for. Please try again.")

        while True:
            after = input("\nWould you like to test more associations or return to the main menu? Enter 'test' or 'main': ").lower().strip()
            if after == "test":
                Association()
                break
            if after == "main":
                Menu()
                break
            else:
                print("\nYou must enter either 'test' or 'main' based on what you want to do. Please try again.")

    if association_choice == "b":


        while True:
            wine_choice = input("\nWould like to test for red or white wine? (enter 'red' or 'white'): ").strip().lower()

            if wine_choice == "red":
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
                break

            if wine_choice == "white":
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
                break

            if wine_choice != "red" or wine_choice != "white":
                print("\nYou must enter either 'red' or 'white' based on which wine you want to test associations for. Please try again.")

        while True:
            after = input("\nWould you like to test more associations or return to the main menu? Enter 'test' or 'main': ").lower().strip()
            if after == "test":
                Association()
                break
            if after == "main":
                Menu()
                break
            else:
                print("\nYou must enter either 'test' or 'main' based on what you want to do. Please try again.")

    if association_choice == "c":

        while True:
            wine_choice = input("\nWould like to test for red or white wine? (enter 'red' or 'white'): ").strip().lower()

            if wine_choice == "red":
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
                break

            if wine_choice == "white":
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
                break

            if wine_choice != "red" or wine_choice != "white":
                print("\nYou must enter either 'red' or 'white' based on which wine you want to test associations for. Please try again.")

        while True:
            after = input("\nWould you like to test more associations or return to the main menu? Enter 'test' or 'main': ").lower().strip()
            if after == "test":
                Association()
                break
            if after == "main":
                Menu()
                break
            else:
                print("\nYou must enter either 'test' or 'main' based on what you want to do. Please try again.")

    if association_choice == "d":

        while True:
            wine_choice = input("\nWould like to test for red or white wine? (enter 'red' or 'white'): ").strip().lower()

            if wine_choice == "red":
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
                break

            if wine_choice == "white":
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
                break

            if wine_choice != "red" or wine_choice != "white":
                print("\nYou must enter either 'red' or 'white' based on which wine you want to test associations for. Please try again.")

        while True:
            after = input("\nWould you like to test more associations or return to the main menu? Enter 'test' or 'main': ").lower().strip()
            if after == "test":
                Association()
                break
            if after == "main":
                Menu()
                break
            else:
                print("\nYou must enter either 'test' or 'main' based on what you want to do. Please try again.")


# Function calls:
Login()
Menu()
# Menu option functions are called within the definition of the menu function.


"""
Include this code after every menu option:
    while True:
        after = input("\nWould you like to return to the main menu or quit? Enter 'main' or 'quit': ").lower().strip()
        if after == "main":
            Menu()
        if after == "quit":
            print("\nHave a great day!")
            break
        if after != "main" or after != "quit":
                print("\nYou must type either 'main' or 'quit' based on what you want to do. Please try again.")
"""
