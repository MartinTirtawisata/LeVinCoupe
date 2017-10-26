import pandas as pd
import scipy.stats
import seaborn
import matplotlib.pyplot as plt

def association():

    print("\n===============================================================================")
    print("a. Volatile Acidity and Wine Quality")
    print("b. Fixed Acidity and Wine Quality")
    print("c. Alcohol and Wine Quality")
    print("d. Residual Sugar and Wine Quality")
    print("===============================================================================")

    while True:
        association_choice = input("\nPlease select an option of which associations you would like to check (enter the letter): ").strip().lower()
        if association_choice == "a" or association_choice == "b" or association_choice == "c" or association_choice == "d":
            break
        else:
            print("\nYou must select only one menu choice from above by typing the letter. Please try again.")

    if association_choice == "a":

        while True:
            wine_choice = input("\nWould like to test for red or white wine? (enter 'red' or 'white'): ").strip().lower()

            if wine_choice == "red":
                try:
                    WineCharX = "quality"
                    WineCharY = "volatile acidity"
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
                    WineCharX = "quality"
                    WineCharY = "volatile acidity"
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
            after = input("\nWould you like to test more associations or return to the main menu? Enter 'test' or 'main': ").lower().strip()
            if after == "test":
                Association()
                break
            if after == "main":
                Menu()
                break
            else:
                print("\nYou must enter either 'test' or 'main' based on what you want to do. Please try again.")

    if association_choice == "b":


        while True:
            wine_choice = input("\nWould like to test for red or white wine? (enter 'red' or 'white'): ").strip().lower()

            if wine_choice == "red":
                try:
                    WineCharX = "quality"
                    WineCharY = "fixed acidity"
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
                    WineCharX = "quality"
                    WineCharY = "fixed acidity"
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
            after = input("\nWould you like to test more associations or return to the main menu? Enter 'test' or 'main': ").lower().strip()
            if after == "test":
                Association()
                break
            if after == "main":
                Menu()
                break
            else:
                print("\nYou must enter either 'test' or 'main' based on what you want to do. Please try again.")

    if association_choice == "c":

        while True:
            wine_choice = input("\nWould like to test for red or white wine? (enter 'red' or 'white'): ").strip().lower()

            if wine_choice == "red":
                try:
                    WineCharX = "quality"
                    WineCharY = "alcohol"
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
                    WineCharX = "quality"
                    WineCharY = "alcohol"
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
            after = input("\nWould you like to test more associations or return to the main menu? Enter 'test' or 'main': ").lower().strip()
            if after == "test":
                Association()
                break
            if after == "main":
                Menu()
                break
            else:
                print("\nYou must enter either 'test' or 'main' based on what you want to do. Please try again.")

    if association_choice == "d":

        while True:
            wine_choice = input("\nWould like to test for red or white wine? (enter 'red' or 'white'): ").strip().lower()

            if wine_choice == "red":
                try:
                    WineCharX = "quality"
                    WineCharY = "residual sugar"
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
                    WineCharX = "quality"
                    WineCharY = "residual sugar"
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
            after = input("\nWould you like to test more associations or return to the main menu? Enter 'test' or 'main': ").lower().strip()
            if after == "test":
                Association()
                break
            if after == "main":
                menu()
                break
            else:
                print("\nYou must enter either 'test' or 'main' based on what you want to do. Please try again.")
