def Menu():
    print("\n===============================================================================")
    print("a. Register other employees")
    print("b. Test wine associations based on characteristic and quality")
    print("c. Create wine frequency distribution based on value of wine characteristic and wine quality")
    print("d. Ask additional questions or add features")
    print("e. Quit")
    print("===============================================================================")

    while True:
        menu_choice = input("\nPlease select an option from the following (enter the letter): ").lower().strip()
        if menu_choice == "a" or menu_choice == "b" or menu_choice == "c" or menu_choice == "d" or menu_choice == "e":
            break
        else:
            print("\nYou must select only one menu choice from above by typing the letter. Please try again.")

# Menu Options

    if menu_choice == "a":
        Registration()
    if menu_choice == "b":
        Association()
    if menu_choice == "c":
        Freq_Distribution()
    #if menu_choice == "d":
        #Additional()
    if menu_choice == "e":
        print("\nHave a great day!")

