## ----------------------------------------------------------------------------------- ##
##                                                                                     ##
## EPITECH PROJECT - Mon, Mar, 2024                                                    ##
## Title           - Rework                                                            ##
## Description     -                                                                   ##
##     choices                                                                         ##
##                                                                                     ##
## ----------------------------------------------------------------------------------- ##
##                                                                                     ##
##         ░        ░       ░░        ░        ░        ░░      ░░  ░░░░  ░            ##
##         ▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒  ▒▒▒▒  ▒            ##
##         ▓      ▓▓▓       ▓▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓      ▓▓▓  ▓▓▓▓▓▓▓        ▓            ##
##         █  ███████  ██████████  ███████  ████  ███████  ████  █  ████  █            ##
##         █        █  ███████        ████  ████        ██      ██  ████  █            ##
##                                                                                     ##
## ----------------------------------------------------------------------------------- ##
def get_choice():
    while True:
        print("1. More")
        print("2. Challenge")
        print("3. Ninja")
        print("4. Hire")
        print("5. F. Jutsu")
        print("6. Beasts")
        print("7. Six Path Tools")
        print("8. Other Events")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= 9:
            return int(choice)
        else:
            print("Invalid choice, try again.")

def get_more_choices():
    while True:
        print("1. Clan")
        print("2. Succession")
        print("3. Academy")
        print("4. Lab")
        print("5. Ally")
        print("6. Ninja Bond")
        print("7. Ranking")
        print("8. Shop")
        print("9. Archive")
        print("10. Back")

        choice = input("Enter your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= 10:
            return int(choice)
        else:
            print("Invalid choice, try again.")
