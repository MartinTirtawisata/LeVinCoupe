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
Additional Features:
1. Association test with ability for user to input the two desired characteristics (option d in our menu).
2. Printed min and max value for user chosen characteristic in frequency distribution and prompted a user to enter a value within the range (including the lower and upper limits).
3. Alerting users to inputted values that are more than 2 SDs from the mean for their chosen characteristic for frequency distribution.
                        -Note that the graph will still be displayed if user enters a value more than 2 SDs away from the mean for their chosen characteristic.
                        -Min/Max and Mean/SD values for all wine characteristics are listed at the top of the Frequency_Distribution file.
4. Blending recommendations for the frequency distribution results:
                            -Issued a blending recommendation if user enters a value for volatile acidity above the regulated amount by the federal Tax and Trade Bureau for red and white wines. Note that the distribution will still be displayed.
                            -Issued a blending recommendation if user enters a value for residual sugar greater than or equal to 20.
                            -Issued a blending recommendation if user enters a value for residual sugar below 4.
                            -Issued a blending recommendation if user enters a value for fixed acidity greater than or equal to 12.
5. GUI
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

