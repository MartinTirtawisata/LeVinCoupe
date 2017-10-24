import sqlite3

conn = sqlite3.connect('LeVinEmployee.db')

with conn:
        cur = conn.cursor()

        #Requirement 1

        userEmail = input("Please enter the email of the employee you want to find: ")

        try:
            cur.execute("SELECT * FROM Employee WHERE(Email = '" + userEmail +"')")

            results = cur.fetchall()
            rowCounter = 0

            print("Password: " + results[0][8])

        except:
            print("Connection Failed")

        #Requirement 2

        while True:

            userEmail = input("\nPlease enter your email: ").strip()
            userPassword = input("Please enter your password: ").strip()

            try:
                cur.execute("SELECT * FROM Employee WHERE(Email = '" + userEmail +"') AND (Password = '" + userPassword + "')")

                if userEmail == results[0][7] and userPassword == results[0][8]:
                    print("\nLogin successful")
                    break
                if userEmail == "":
                    print("You did not enter an email")
                if userPassword == "":
                    print("You did not enter a password")
                else:
                    print("\nLogin failed, email or password is incorrect. Please try again")

            except:
                print("Connection Failed")