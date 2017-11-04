import pandas as pd
import scipy.stats
import seaborn
import matplotlib.pyplot as plt

'''
Questions to ask:
Are the frequency requirements different for every wine characteristic?
It works for residual sugar for the values of 

Problem #1: Floats; the alcohol, fixed, volatile are in the forms of floats which means values are inconsistent with integer etc

Problem #2: Need to create a range for requirement 4

'''
def freq_distribution():

    while True:
        print("\n===============================================================================")
        print("a. Residual Sugar")
        print("b. Alcohol Percentage")
        print("c. Fixed Acidity")
        print("d. Volatile Acidity")
        print("===============================================================================")

        wine_char = input("\nPlease select an option (enter the letter): ").lower().strip()

        if wine_char == "a":
            wine_char = "residual sugar"
            break
        if wine_char == "b":
            wine_char = "alcohol"
            break
        if wine_char == "c":
            wine_char = "fixed acidity"
            break
        if wine_char == "d":
            wine_char = "volatile acidity"
            break
        else:
            print("\nYou must select only one menu choice from above by typing the letter. Please try again.")

    while True:
        wine_type = input("\nPlease enter 'red' or 'white' based on the distribution on the wine distribution you wish to see: ").lower().strip()
        if wine_type == "red" or wine_type == "white":
            break
        else:
            print("\nYou must enter either 'red' or 'white' based on which wine you want to see a distribution for. Please try again.")

    # try:
    #     while True:
    #         wine_char_value = int(input("\nPlease enter a value (lower bound): "))
    #         wine_char_value_2 = int(input("\nPlease enter a value higher than the previous(upper bound): "))

    try:
        if wine_char == "residual sugar":
            while True:
                wine_char_value = int(input("\nPlease enter a value for this characteristic: "))
                #apparantly the value of 5 is too much for residual sugar for red
                # need to figure out what are the min - max values
                if wine_char_value > 4 or wine_char_value == "":
                    print("\nInput invalid. Please enter a value between 1 - 5")
                else:
                    break

        if wine_char == "alcohol" or wine_char == "fixed acidity" or wine_char == "volatile acidity":
            while True:
                wine_char_value = float(input("\nPlease enter a value for this characteristic: "))
                print(wine_char_value)
                # need to figure out what are the min - max values
                if wine_char_value > 10 or wine_char_value == "":
                    print("\nInput invalid. Please enter a value between 1 - 5")
                else:
                    break

        wine_char_2 = "quality"
        all_wines = pd.read_csv('winequality-both.csv')

        if wine_type == "red":
            red = all_wines.loc[all_wines['type'] == 'red', :]

            red_wine_char = red.loc[red[wine_char] == wine_char_value, :]
            print(red_wine_char)

            wine_char_value_data_set = red_wine_char.loc[:, wine_char_2]

            seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
            plt.title("Red Wine: " + wine_char + " has the value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
            plt.ylabel('Number of wines')

            plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
            plt.show()

        if wine_type == "white":
            white = all_wines.loc[all_wines['type'] == 'white', :]

            white_wine_char = white.loc[white[wine_char] == wine_char_value, :]

            wine_char_value_data_set = white_wine_char.loc[:, wine_char_2]

            seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
            plt.title("White Wine: "+ wine_char + " has the value of " + str(wine_char_value) + ", frequencies by " + wine_char_2)
            plt.ylabel('Number of wines')

            plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            plt.show()

    except (KeyError, ZeroDivisionError) as e:
        print("\n")
        print(e)

    while True:
        after = input("\nWould you like to test more frequency distribution or return to the main menu? Enter 'test' or 'main': ").lower().strip()
        if after == "test":
            freq_distribution()
            break
        if after == "main":
            break
        else:
            print("\nYou must enter either 'test' or 'main' based on what you want to do. Please try again.")



