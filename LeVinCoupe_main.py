import pandas as pd
import scipy.stats
import seaborn
import matplotlib.pyplot as plt
import sqlite3
from Association import association
from Frequency_Distribution import freq_distribution
from Login import login
from Registration import registration
from Menu import menu
conn = sqlite3.connect('LeVinEmployee.db')


#-------------------------------------------Beginning of Code---------------------------------------------
print("\n===============================================================================")
print("                          WELCOME TO LE VIN COUPE")
print("                Where wine and quality engineering collide!")
print("===============================================================================")

print("1) log in")
print("0 exit ")
option = int(input("Please choose an option: "))

if option == 0:
    print(" Have a nice day! ")

if option == 1:
    login()

    active = True
    while active:
        menu()
        while True:
            menu_choice = input("\nPlease select an option from the following (enter the letter): ").lower().strip()
            if menu_choice == "a" or menu_choice == "b" or menu_choice == "c" or menu_choice == "d" or menu_choice == "e":
                break
            else:
                print("\nYou must select only one menu choice from above by typing the letter. Please try again.")

        if menu_choice == "a":
            registration()
            continue

        if menu_choice == "b":
            association()

        if menu_choice == "c":
            freq_distribution()

        #if menu_choice == "d":
            #Additional()

        if menu_choice == "e":
            active = False
            print("\nHave a great day!")
            break

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
