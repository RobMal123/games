from random import randint

options = ["sten", "sax", "påse"]

computer = options[randint(0, 2)]

player = False
player_count = 0
computer_count = 0

# ANSI-färger
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"

while True:
    if player_count == 5:
        print(f"{GREEN}Du vann grattis! den här spelomgången e nu slut. {RESET}")
        break
    elif computer_count == 5:
        print(f"{RED}Du förlorade försök igen, den här spelomgången e nu slut{RESET}")
        break
    computer = options[randint(0, 2)]
    print(f"{CYAN}Spelares poäng: {player_count}{RESET}")
    print(f"{CYAN}Dators poäng: {computer_count}{RESET}")
    player = input(f"{YELLOW}STEN SAX eller PÅSE: {RESET}").lower()
    if player == computer:
        print(f"{BLUE}Oavgjort! datorn valde också: {computer.upper()}{RESET}")
    elif player == "sten":
        if computer == "sax":
            player_count += 1
            print(f"{GREEN}Du vann, datorn valde: {computer.upper()}{RESET}")
        elif computer == "påse":
            computer_count += 1
            print(f"{RED}Du förlora, datorn valde: {computer.upper()}{RESET}")
    elif player == "sax":
        if computer == "sten":
            computer_count += 1
            print(f"{RED}Du förlora, datorn valde: {computer.upper()}{RESET}")
        elif computer == "påse":
            player_count += 1
            print(f"{GREEN}Du vann, datorn valde: {computer.upper()}{RESET}")
    elif player == "påse":
        if computer == "sten":
            player_count += 1
            print(f"{GREEN}Du vann, datorn valde: {computer.upper()}{RESET}")
        elif computer == "sax":
            computer_count += 1
            print(f"{RED}Du förlora, datorn valde: {computer.upper()}{RESET}")
    else:
        print(f"{RED}Felaktig input{RESET}")
