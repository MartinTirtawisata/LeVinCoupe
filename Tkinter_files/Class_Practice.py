from tkinter import *
import tkinter.messagebox as tm
import sqlite3



class LoginFrame(Frame):

    with sqlite3.connect('LeVinEmployee.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employee")
        query_result = cursor.fetchall()

    def __init__(self, master):
        super().__init__(master)

        self.label_email = Label(self, text="Email")
        self.label_password = Label(self, text="Password")

        self.entry_email = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_email.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_email.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command = self.check_login)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def check_login(self):
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

        if userEmail == query_result[7] and userPassword == query_result[8]:
            tm.showinfo("Login info", "Welcome " + query_result[1] + " " + query_result[2])
        else:
            if userEmail != query_result[7]:
                tm.showerror("Login error", "Incorrect Email")
            if userEmail != query_result[8]:
                tm.showerror("Login error", "Incorrect Password")
            if userEmail != query_result[7] and userPassword != query_result[8]:
                tm.showerror("Login error", "Incorrect Email or Password")
#
# class MenuFrame(Frame):
#     def __init__(self, master):




if __name__ == "__main__":
    root = Tk()
    main = LoginFrame(root)
    root.geometry("400x400+500+300")
    root.mainloop()