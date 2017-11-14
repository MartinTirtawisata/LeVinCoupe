from tkinter import *
import tkinter.messagebox as tm
import sqlite3

class Login(Frame):

    db_name = 'LeVinEmployee.db'

    def __init__(self, master):
        super().__init__(master)

        self.ue_label = Label(self, text="Username")
        self.pw_label = Label(self, text="Password")

        self.userEmail = Entry(self)
        self.userPassword = Entry(self, show="*")

        self.ue_label.grid(row=0, sticky=E)
        self.pw_label.grid(row=1, sticky=E)
        self.userEmail.grid(row=0, column=1)
        self.userPassword.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked())
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()

            query = "SELECT * FROM Employee WHERE(Email = '" + str(self.userEmail) + "') AND (Password = '" + str(self.userPassword) + "')"
            cursor.execute(query, parameters)
            query_result = cursor.fetchall()

        return


        # print("Clicked")
        userEmail = self.userEmail.get()
        userPassword = self.userPassword.get()

        # print(username, password)

        if userEmail == self.query_result[0][7] and userPassword == self.query_result[0][8]:
            tm.showinfo("Login info", "Welcome" + userEmail)
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
