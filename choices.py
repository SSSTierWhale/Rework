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

def display_archive_units():
    with open('archive_units.json', 'r') as f:
        units = json.load(f)
    for unit in units:
        print(f"Nom: {unit['name']}")
        print(f"Type: {unit['type']}")
        print(f"Stats: Hp: {unit['stats']['Hp']}, ATK: {unit['stats']['ATK']}, DEF: {unit['stats']['DEF']}")
        print(f"Range: {unit['Range']}")
        print(f"Type d'unité: {unit['unit_type']}")
        if unit['DPS'] == 'yes':
            print("DPS: Yes")
        if unit['SPT'] == 'yes':
            print("SPT: Yes")
        if unit['Medic'] == 'yes':
            print("Medic: Yes")
        if unit['DEF'] == 'yes':
            print("DEF: Yes")
        print(f"F. Jutsu: {unit['f_jutsu']}")
        for skill in unit['skills']:
            if 'chakra' in skill:
                print(f"Chakra: {skill['chakra']}")
                print(f"Description: {skill['description']}")
            elif 'Passive' in skill:
                print(f"Passive: {skill['Passive']}")
            elif 'Talent' in skill:
                print(f"Talent: {skill['Talent']}")
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
