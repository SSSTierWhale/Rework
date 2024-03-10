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
import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from colorama import Fore, Style

def display_archive_units():
    with open('archive.json', 'r') as f:
        units = json.load(f)
    for unit in units:
        print(f"{Fore.LIGHTYELLOW_EX}Name: {unit['name']}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTYELLOW_EX}Type: {unit['type']}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTYELLOW_EX}Stats: Hp: {unit['stats']['Hp']}, ATK: {unit['stats']['ATK']}, DEF: {unit['stats']['DEF']}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTYELLOW_EX}Range: {unit['Range']}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTYELLOW_EX}Unit type: {unit['unit_type']}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTYELLOW_EX}F. Jutsu: {unit['f_jutsu']}{Style.RESET_ALL}")
        for skill in unit['skills']:
            if 'chakra' in skill:
                print(f"{Fore.LIGHTYELLOW_EX}Chakra: {skill['chakra']}{Style.RESET_ALL}")
                print(f"{Fore.LIGHTYELLOW_EX}Description: {skill['description']}{Style.RESET_ALL}")
            elif 'Passive' in skill:
                print(f"{Fore.LIGHTYELLOW_EX}Passive Name: {skill['Passive_name']}{Style.RESET_ALL}")
                print(f"{Fore.LIGHTYELLOW_EX}Passive: {skill['Passive']}{Style.RESET_ALL}")
            elif 'Talent' in skill:
                print(f"{Fore.LIGHTYELLOW_EX}Talent Name: {skill['Talent_name']}{Style.RESET_ALL}")
                print(f"{Fore.LIGHTYELLOW_EX}Talent: {skill['Talent']}{Style.RESET_ALL}")
        print()

def get_choice():
    while True:
        print(f"{Fore.LIGHTBLUE_EX}1. More{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}2. Challenge{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}3. Ninja{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}4. Hire{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}5. F. Jutsu{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}6. Beasts{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}7. Six Path Tools{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}8. Other Events{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}9. Exit{Style.RESET_ALL}")
        
        choice = input(f"{Fore.CYAN}Enter your choice: {Style.RESET_ALL}")
        if choice.isdigit() and 1 <= int(choice) <= 9:
            return int(choice)
        else:
            print(f"{Fore.RED}Invalid choice, try again.{Style.RESET_ALL}")

def get_more_choices():
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
        print(f"{Fore.LIGHTBLUE_EX}10. Back{Style.RESET_ALL}")

        choice = input(f"{Fore.CYAN}Enter your choice: {Style.RESET_ALL}")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 8:
                return choice
            elif choice == 9:
                display_archive_units()
            elif choice == 10:
                return choice
        else:
            print("Invalid choice, try again.")
