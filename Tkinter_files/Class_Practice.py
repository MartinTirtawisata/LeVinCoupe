from tkinter import *
import tkinter.messagebox as tm


class LoginFrame(Frame):
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
        self.userEmail = self.str(entry_email.get())
        self.userPassword = self.str(entry_password.get())

        try:
            with sqlite3.connect('LeVinEmployee.db') as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM Employee WHERE(Email = '" + self.userEmail + "') AND (Password = '" + self.userPassword + "')")
                query_result = cursor.fetchone()
                print(query_result)
        except (KeyError) as e:
            print(e)

        if self.userEmail == self.query_result[7] and self.userPassword == self.query_result[8]:
            tm.showinfo("Login info", "Welcome John")

class MenuFrame(Frame):
    def __init__(self, master):




if __name__ == "__main__":
    root = Tk()
    main = LoginFrame(root)
    root.geometry("400x400+500+300")
    root.mainloop()