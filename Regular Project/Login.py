import sqlite3
conn = sqlite3.connect('LeVinEmployee.db')

def login():
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
                        print("\nLogin successful!")
                        break
                except:
                    print("\nConnection Failed. You entered a wrong email or password. Please try again.")
