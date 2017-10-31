import pandas as pd
import scipy.stats
import seaborn
import matplotlib.pyplot as plt

def freq_distribution():
    try:
        while True:
            wine_type = input("\nPlease enter 'red' or 'white' based on the distribution on the wine distribution you wish to see: ").lower().strip()
            if wine_type == "red" or wine_type == "white":
                break
            else:
                print("\nYou must enter either 'red' or 'white' based on which wine you want to see a distribution for. Please try again.")

        while True:
            print("\n===============================================================================")
            print("a. Residual Sugar")
            print("b. Alcohol Percentage")
            print("c. Fixed Acidity")
            print("d. Volatile Acidity")
            print("===============================================================================")

            wine_char = input("\nPlease select an option of which wine characteristic you would like to see a distribution for (enter the letter):").lower().strip()
            if wine_char == "a" or wine_char == "b" or wine_char == "c" or wine_char == "d":
                break
            else:
                print("\nYou must select only one menu choice from above by typing the letter. Please try again.")

        while True:
            wine_char_value = int(input("\nPlease enter a value for this characteristic: "))
            # need to figure out what are the min - max values
            if wine_char_value > 5 or wine_char_value == "":
                print("\nInput invalid. Please enter a value between 1 - 5")
            else:
                break

        wine_char_2 = "quality"
        all_wines = pd.read_csv('winequality-both.csv')

        if wine_type == "red":
            red = all_wines.loc[all_wines['type']=='red', :]

            red_residual_sugar = red.loc[red[wine_char] == wine_char_value, :]

            wine_char_value_data_set = red_residual_sugar.loc[:, wine_char_2]

            seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
            plt.title(wine_char + " value " + str(wine_char_value) + " frequencies by " + wine_char_2)
            plt.ylabel('Number of wines')

            plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
            plt.show()

        if wine_type == "white":
            white = all_wines.loc[all_wines['type'] == 'white', :]

            white_residual_sugar = white.loc[white[wine_char] == wine_char_value, :]

            wine_char_value_data_set = white_residual_sugar.loc[:, wine_char_2]

            seaborn.distplot(wine_char_value_data_set, bins=10, kde=False)
            plt.title(wine_char + " value " + str(wine_char_value) + " frequencies by " + wine_char_2)
            plt.ylabel('Number of wines')

            plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            plt.show()

    except (KeyError, ZeroDivisionError) as e:
        print(e)


