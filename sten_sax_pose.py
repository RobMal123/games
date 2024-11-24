from random import randint

options = ["sten", "sax", "påse"]

computer = options[randint(0,2)]

player = False
player_count = 0
computer_count = 0

while True:
    computer = options[randint(0,2)]
    print(f"Spelares poäng: {player_count}")
    print(f"Dators poäng: {computer_count}")
    player = input("STEN SAX eller PÅSE : ").lower()
    if player == computer:
        print(f"Oavgjort! datorn valde också: {computer.upper()}")
    elif player == "sten":
        if computer == "sax":
            player_count += 1
            print(f"Du vann, datorn valde: {computer.upper()}")
        elif computer == "påse":
            computer_count += 1
            print(f"Du förlora, datorn valde: {computer.upper()}")
    elif player == "sax":
        if computer == "sten":
            computer_count += 1
            print(f"Du förlora, datorn valde: {computer.upper()}")
        elif computer == "påse":
            player_count += 1
            print(f"Du vann, datorn valde: {computer.upper()}")
    elif player == "påse":
        if computer == "sten":
            player_count += 1
            print(f"Du vann, datorn valde: {computer.upper()}")
        elif computer == "sax":
            computer_count += 1
            print(f"Du förlora, datorn valde: {computer.upper()}")
    else:
        print("Felaktig input")

    
        
