class Dog:
    def __init__(self):
        self.name = "Buddy"



print(Dog().name)







# import tkinter as tk
#
# class Page(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#     def show(self):
#         self.lift()
#
# class Page1(Page):
#    def __init__(self, *args, **kwargs):
#        Page.__init__(self, *args, **kwargs)
#        label = tk.Label(self, text="This is page 1")
#        label.pack(side="top", fill="both", expand=True)
#
# class Page2(Page):
#    def __init__(self, *args, **kwargs):
#        Page.__init__(self, *args, **kwargs)
#        label = tk.Label(self, text="This is page 2")
#        label.pack(side="top", fill="both", expand=True)
#
# class Page3(Page):
#    def __init__(self, *args, **kwargs):
#        Page.__init__(self, *args, **kwargs)
#        label = tk.Label(self, text="This is page 3")
#        label.pack(side="top", fill="both", expand=True)
#
# class MainView(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#         p1 = Page1(self)
#         p2 = Page2(self)
#         p3 = Page3(self)
#
#         buttonframe = tk.Frame(self)
#         container = tk.Frame(self)
#         buttonframe.pack(side="top", fill="x", expand=False)
#         container.pack(side="top", fill="both", expand=True)
#
#         p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#         p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#         p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#
#         b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
#         b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
#         b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)
#
#         b1.pack(side="left")
#         b2.pack(side="left")
#         b3.pack(side="left")
#
#         p1.show()
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     main = MainView(root)
#     main.pack(side="top", fill="both", expand=True)
#     root.wm_geometry("400x400")
#     root.mainloop()


# from tkinter import *
# from tkinter import ttk
#
#
# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
#     except ValueError:
#         pass
#
#
# root = Tk()
# root.title("Feet to Meters")
#
# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# mainframe.columnconfigure(0, weight=1)
# mainframe.rowconfigure(0, weight=1)
#
# feet = StringVar()
# meters = StringVar()
#
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))
#
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
#
# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
#
# for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
#
# feet_entry.focus()
# root.bind('<Return>', calculate)
#
# root.mainloop()
#
