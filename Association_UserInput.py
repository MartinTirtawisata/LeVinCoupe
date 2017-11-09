import pandas as pd
import scipy.stats
import seaborn
import matplotlib.pyplot as plt
from Menu import menu

def association_userInput():

    print("\n===============================================================================")
    print("a. Fixed Acidity")
    print("b. Volatile Acidity")
    print("c. Citric Acid")
    print("d. Residual Sugar")
    print("e. Chlorides")
    print("f. Free Sulfur")
    print("g. Dioxide")
    print("h. Total Sulfur Dioxide")
    print("i. Density")
    print("j. pH")
    print("k. Sulphates")
    print("l. Alcohol")
    print("m. Quality")
    print("===============================================================================")

    print("\nPlease select two characteristics from above to test an association for (enter the letter)")
    print("Note: If one of the characteristics you want to test for is quality, it is recommended you choose this characteristic for characteristic 1.")

    while True:
        choice1 = input("\nCharacteristic 1: ").lower().strip()
        if choice1 == "a":
            choice1 = "fixed acidity"
            break
        if choice1 == "b":
            choice1 = "volatile acidity"
            break
        if choice1 == "c":
            choice1 = "citric acid"
            break
        if choice1 == "d":
            choice1 = "residual sugar"
            break
        if choice1 == "e":
            choice1 = "chlorides"
            break
        if choice1 == "f":
            choice1 = "free sulfur"
            break
        if choice1 == "g":
            choice1 = "dioxide"
            break
        if choice1 == "h":
            choice1 = "total sulfur dioxide"
            break
        if choice1 == "i":
            choice1 = "density"
            break
        if choice1 == "j":
            choice1 = "pH"
            break
        if choice1 == "k":
            choice1 = "sulphates"
            break
        if choice1 == "l":
            choice1 = "alcohol"
            break
        if choice1 == "m":
            choice1 = "quality"
            break
        else:
            print("\nYou must select only one menu choice from above by typing the letter. Please try again.")

    while True:
        choice2 = input("\nCharacteristic 2: ").lower().strip()
        if choice2 == "a":
            choice2 = "fixed acidity"
            break
        if choice2 == "b":
            choice2 = "volatile acidity"
            break
        if choice2 == "c":
            choice2 = "citric acid"
            break
        if choice2 == "d":
            choice2 = "residual sugar"
            break
        if choice2 == "e":
            choice2 = "chlorides"
            break
        if choice2 == "f":
            choice2 = "free sulfur"
            break
        if choice2 == "g":
            choice2 = "dioxide"
            break
        if choice2 == "h":
            choice2 = "total sulfur dioxide"
            break
        if choice2 == "i":
            choice2 = "density"
            break
        if choice2 == "j":
            choice2 = "pH"
            break
        if choice2 == "k":
            choice2 = "sulphates"
            break
        if choice2 == "l":
            choice2 = "alcohol"
            break
        if choice2 == "m":
            choice2 = "quality"
            break
        else:
            print("\nYou must select only one menu choice from above by typing the letter. Please try again.")


    while True:
        wine_choice = input("\nWould like to test for red or white wine? (enter 'red' or 'white'): ").strip().lower()

        if wine_choice == "red":
            try:
                WineCharX = choice1
                WineCharY = choice2
                allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                red = allWines.loc[allWines['type'] == 'red', :]

                getCorr = scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
                correlation = str(getCorr[0])
                pValue = str(getCorr[1])
                print("\nFor red wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                print("With p-value of: " + pValue)

                seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
                plt.xlabel(WineCharX)
                plt.ylabel(WineCharY)
                plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
                plt.show()

            except (KeyError) as e:
                print("\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")
            break

        if wine_choice == "white":
            try:
                WineCharX = choice1
                WineCharY = choice2
                allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
                white = allWines.loc[allWines['type'] == 'white', :]

                getCorr = scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
                correlation = str(getCorr[0])
                pValue = str(getCorr[1])
                print("\nFor white wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
                print("With p-value of: " + pValue)

                seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
                plt.xlabel(WineCharX)
                plt.ylabel(WineCharY)
                plt.title("White Wine: " + WineCharX + " X " + WineCharY)
                plt.show()

            except (KeyError) as e:
                print("\nError. Please check that your spelling is correct of the wine characteristic you wish to test.")
            break

        if wine_choice != "red" or wine_choice != "white":
            print("\nYou must enter either 'red' or 'white' based on which wine you want to test associations for. Please try again.")

    while True:
        after = input("\nWould you like to test more associations or return to the main menu? (enter 'test' or 'main'): ").lower().strip()
        if after == "test":
            association_userInput()
            break
        if after == "main":
            break
        else:
            print("\nYou must enter either 'test' or 'main' based on what you want to do. Please try again.")



