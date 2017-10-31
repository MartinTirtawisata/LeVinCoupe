import pandas as pd
import scipy.stats
import seaborn
import matplotlib.pyplot as plt

def freq_distribution():
    try:
        while True:
            wine_type = input("please choose 'red' or 'white' wine: ").lower().strip()
            if wine_type == "red" or wine_type == "white":
                break
            else:
                print("Input invalid. Please choose red or white")

        while True:
            wine_char = input("what wine characteristic would you like to choose?\
        \n(residual sugar, alcohol present, fixed acidity, volatile acidity: ").lower().strip()
            if wine_char == "residual sugar" or wine_char == "alcohol present" or wine_char == "fixed acidity" or wine_char == "volatile acidity":
                break
            else:
                print("Input invalid: Please enter from the available wine characters")

        while True:
            wine_char_value = int(input("Please enter a value: "))
            # need to figure out what are the min - max values
            if wine_char_value > 5 or wine_char_value == "":
                print("Input invalid. Please enter a value between 1 - 5")
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



