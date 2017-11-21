import sqlite3
conn = sqlite3.connect('LeVinEmployee.db')

def registration():
    with conn:
        cur = conn.cursor()

        print("\nYou selected the option to register a new employee.")
        while True:
            empID = input("\nTo register a new employee, please enter a new 4 digit employee ID: ").strip()
            if empID and empID.isdigit() and len(empID) == 4:
                break
            else:
                print("\nThe employee ID cannot be left blank and must only contain a 4 digit number. Please try again.")

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
        except sqlite3.Error as e:
            print("\n")
            print(e)

    while True:
        firstName = input("\nNext, enter the employee's first name: ").strip().title()
        if firstName.isalpha():
            break
        else:
            print("\nThe employee's first name cannot be left blank and can only contain letters. Please try again.")

    while True:
        lastName = input("\nEnter the employee's last name: ").strip().title()
        if lastName.isalpha():
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

    while True:
        email = input("\nEnter the employee's email: ").strip()
        if email:
            break
        else:
            print("\nThe employee's email cannot be left blank. Please try again.")

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
    except sqlite3.Error as e:
        print("\n")
        print(e)

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
        after = input("\nWould you like to return to the main menu or register more employees? (enter 'main' or 'register'): ").lower().strip()
        if after == "main":
            break
        if after == "register":
            registration()

        if after != "main" or after != "quit":
            print("\nYou must type either 'main' or 'quit' based on what you want to do. Please try again.")


