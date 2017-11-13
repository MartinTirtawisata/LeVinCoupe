import pandas as pd
import scipy.stats
import seaborn
import matplotlib.pyplot as plt
import sqlite3
from Association import association
from Frequency_Distribution import freq_distribution
from Login import login
from Association_UserInput import association_userInput

from Registration import registration
from Menu import menu
conn = sqlite3.connect('LeVinEmployee.db')

'''
Additional Features (include this in dropbox as a separate file):
-Association with ability for user inputted characteristics (option d in our menu)
-Printed min and max value for user chosen characteristic in frequency distribution and prompted a user to enter a value within the range
-Alerting users to values that are more than 2 SDs from the mean for their chosen characteristic and inputted value for frequency distribution
                        -Min/Max and Mean/SD values for all characteristics are listed at the top of the Frequency_Distribution file
-Blending recommendations for the frequency distribution if user inputted outlier values for their chosen characteristic (clarify what checks there are and where at in the code)
                            -Blending recommendation if user enters a min or max value for a characteristic
                            -Blending recommendation for GOV STANDARD OF VOLATILE ACIDITY
-GUI
'''

#-------------------------------------------Beginning of Code---------------------------------------------
print("\n===============================================================================")
print("                          WELCOME TO LE VIN COUPE")
print("                Where wine and quality engineering collide!")
print("===============================================================================")

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

    if menu_choice == "b":
        association()

    if menu_choice == "c":
        freq_distribution()

    if menu_choice == "d":
        association_userInput()

    if menu_choice == "e":
        active = False
        print("\nHave a great day!")

