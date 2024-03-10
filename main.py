## ----------------------------------------------------------------------------------- ##
##                                                                                     ##
## EPITECH PROJECT - Mon, Mar, 2024                                                    ##
## Title           - Rework                                                            ##
## Description     -                                                                   ##
##     main                                                                            ##
##                                                                                     ##
## ----------------------------------------------------------------------------------- ##
##                                                                                     ##
##       ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▀▄    ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▄▄▄▄   ▄▀▀▄ ▄▄            ##
##      ▐  ▄▀   ▐ █   █   █ █   █  █  █    █  ▐ ▐  ▄▀   ▐ █ █    ▌ █  █   ▄▀           ##
##        █▄▄▄▄▄  ▐  █▀▀▀▀  ▐   █  ▐  ▐   █       █▄▄▄▄▄  ▐ █      ▐  █▄▄▄█            ##
##        █    ▌     █          █        █        █    ▌    █         █   █            ##
##       ▄▀▄▄▄▄    ▄▀        ▄▀▀▀▀▀▄   ▄▀        ▄▀▄▄▄▄    ▄▀▄▄▄▄▀   ▄▀  ▄▀            ##
##       █    ▐   █         █       █ █          █    ▐   █     ▐   █   █              ##
##       ▐        ▐         ▐       ▐ ▐          ▐        ▐         ▐   ▐              ##
##                                                                                     ##
## ----------------------------------------------------------------------------------- ##
from choices import get_choice, get_more_choices
from colorama import Fore, Style

class Choice:
    def main(self):
        while True:
            choice = get_choice()
            if choice == 1:
                more_choice = get_more_choices()
            elif choice == 2:
                print(f"{Fore.LIGHTGREEN_EX}Succession{Style.RESET_ALL}")
            elif choice == 3:
                print(f"{Fore.LIGHTGREEN_EX}Academy{Style.RESET_ALL}")
            elif choice == 4:
                print(f"{Fore.LIGHTGREEN_EX}Hire{Style.RESET_ALL}")
            elif choice == 5:
                print(f"{Fore.LIGHTGREEN_EX}F. Jutsu{Style.RESET_ALL}")
            elif choice == 6:
                print(f"{Fore.LIGHTGREEN_EX}Beasts{Style.RESET_ALL}")
            elif choice == 7:
                print(f"{Fore.LIGHTGREEN_EX}Six Path Tools{Style.RESET_ALL}")
            elif choice == 8:
                print(f"{Fore.LIGHTGREEN_EX}Other Events{Style.RESET_ALL}")
            elif choice == 9:
                print(f"{Fore.LIGHTGREEN_EX}Goodbye!{Style.RESET_ALL}")
                break
            
if __name__ == "__main__":
    choice = Choice()
    choice.main()
