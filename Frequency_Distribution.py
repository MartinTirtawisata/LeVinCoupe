import pandas as pd
import scipy.stats
import seaborn
import matplotlib.pyplot as plt

'''
Max Values:
fixed acidity = 15.9
volatile acidity = 1.58
citric acid = 1.66
residual sugar = 65.8
chlorides = 0.611
free sulfur dioxide = 289
total sulfur dioxide = 440
density = 1.03898
pH = 4.01
sulphates = 2
alcohol = 14.9
quality = 9

Volatile Acidity:   Mean = 0.339666     SD = 0.164636474        Two SDs from Mean = 0.668938
Fixed Acidity:      Mean = 7.215307065  SD = 1.296433758        Two SDs from Mean = 9.808175
Alcohol:            Mean = 10.49180083  SD = 1.192711749        Two SDs from Mean = 12.877224
Residual Sugar:     Mean = 5.443235339  SD = 4.757803743        Two SDs from Mean = 14.958843
'''


def freq_distribution():

    print("\n===============================================================================")
    print("a. Volatile Acidity")
    print("b. Fixed Acidity")
    print("c. Alcohol")
    print("d. Residual Sugar")
    print("===============================================================================")

    while True:
        wine_char = input("\nPlease select an option (enter the letter): ").lower().strip()

        if wine_char == "a":
            wine_char = "volatile acidity"
            break
        if wine_char == "b":
            wine_char = "fixed acidity"
            break
        if wine_char == "c":
            wine_char = "alcohol"
            break
        if wine_char == "d":
            wine_char = "residual sugar"
            break
        else:
            print("\nYou must select only one menu choice from above by typing the letter.")

    while True:
        wine_type = input("\nPlease enter 'red' or 'white' based on the wine distribution you wish to see: ").lower().strip()
        if wine_type == "red" or wine_type == "white":
            break
        else:
            print("\nYou must enter either 'red' or 'white' based on which wine you want to see a distribution for.")

    try:
        if wine_char == "volatile acidity":
            while True:
                wine_char_value = float(input("\nEnter a numerical value for this characteristic: "))
                if wine_char_value > 1.58 or wine_char_value == "":
                    print("\nThe max value for volatile acidity out of all wines is 1.58. Please enter a value no greater than this number.")
                elif wine_char_value > 0.668938:
                    print("\nALERT: The value you have entered is more than two standard deviations away from the mean volatile acidity for all wines.")
                elif wine_char_value == 0 or wine_char_value < 0:
                    print("\nPlease enter a value that is greater than 0.")
                else:
                    break

        if wine_char == "fixed acidity":
            while True:
                wine_char_value = float(input("\nEnter a numerical value for this characteristic: "))
                if wine_char_value > 15.9 or wine_char_value == "":
                    print("\nThe max value for fixed acidity out of all wines is 15.9. Please enter a value no greater than this number.")
                elif wine_char_value > 9.808175:
                    print("\nALERT: The value you have entered is more than two standard deviations away from the mean fixed acidity for all wines.")
                    break
                elif wine_char_value == 0 or wine_char_value < 0:
                    print("\nPlease enter a value that is greater than 0.")
                else:
                    break

        if wine_char == "alcohol":
            while True:
                wine_char_value = float(input("\nEnter a numerical value for this characteristic: "))
                if wine_char_value > 14.9 or wine_char_value == "":
                    print("\nThe max value for alcohol percentage out of all wines is 14.9. Please enter a value no greater than this number.")
                elif wine_char_value > 12.877224:
                    print("\nALERT: The value you have entered is more than two standard deviations away from the mean alcohol percentage for all wines.")
                    break
                elif wine_char_value == 0 or wine_char_value < 0:
                    print("\nPlease enter a value that is greater than 0.")
                else:
                    break

        if wine_char == "residual sugar":
            while True:
                wine_char_value = float(input("\nEnter a numerical value for this characteristic: "))
                if wine_char_value > 65.8 or wine_char_value == "":
                    print("\nThe max value for residual sugar out of all wines is 65.8. Please enter a value no greater than this number.")
                elif wine_char_value > 14.958843:
                    print("\nALERT: The value you have entered is more than two standard deviations away from the mean residual sugar for all wines.")
                    break
                elif wine_char_value == 0 or wine_char_value < 0:
                    print("\nPlease enter a value that is greater than 0.")
                else:
                    break

        wine_char_2 = "quality"
        all_wines = pd.read_csv('winequality-both.csv')

        if wine_type == "red":
            red = all_wines.loc[all_wines['type'] == 'red', :]

            red_wine_char = red.loc[red[wine_char] == wine_char_value, :]

            wine_char_value_data_set = red_wine_char.loc[:, wine_char_2]

            seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
            plt.title("Red Wine: " + wine_char + " value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
            plt.ylabel('Number of wines')

            plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
            plt.show()

        if wine_type == "white":
            white = all_wines.loc[all_wines['type'] == 'white', :]

            white_wine_char = white.loc[white[wine_char] == wine_char_value, :]

            wine_char_value_data_set = white_wine_char.loc[:, wine_char_2]

            seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
            plt.title("White Wine: "+ wine_char + " value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
            plt.ylabel('Number of wines')

            plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            plt.show()

    except (KeyError, ZeroDivisionError) as e:
        print("\n")
        print(e)

    while True:
        after = input("\nWould you like to test more frequency distributions or return to the main menu? (enter 'test' or 'main'): ").lower().strip()
        if after == "test":
            freq_distribution()
            break
        if after == "main":
            break
        else:
            print("\nYou must enter either 'test' or 'main' based on what you want to do. Please try again.")



