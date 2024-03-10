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
from colorama import Fore, Style

def get_choice():
    while True:
        print(f"{Fore.LIGHTBLUE_EX}1. Clan{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}2. Succession{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}3. Academy{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}4. Lab{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}5. Ally{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}6. Ninja Bond{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}7. Ranking{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}8. Shop{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}9. Archive{Style.RESET_ALL}")
        
        choice = input(f"{Fore.CYAN}Enter your choice: {Style.RESET_ALL}")
        if choice.isdigit() and 1 <= int(choice) <= 9:
            return int(choice)
        else:
            print(f"{Fore.RED}Invalid choice, try again.{Style.RESET_ALL}")

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
