print(''' ,     ,
    (\____/)
     (_oo_)
       (O)
     __||__    \)
  []/______\[] /
  / \______/ \/
 /    /__\ 
(\   /____\ ''')
print("Welcome to Robo Quest.")
print("Your mission is to find the ultimate robot core.")

choice1 = input("You're at a robotic junction. Where do you want to go? "
                'Type "left" or "right": ').lower()

if choice1 == "left":
    choice2 = input("You reach a cyber-lake. "
                    "There is a floating mech-island. "
                    'Type "wait" to summon a hover-boat, '
                    'or "swim" to power through the lake: ').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island safely. "
                        "There is a facility with 3 doors: red, yellow, and blue. "
                        "Which door will you choose? ").lower()
        if choice3 == "red":
            print("The room is filled with molten circuits. System meltdown! Game over.")
        elif choice3 == "yellow":
            print("You found the ultimate robot core! You win!")
        elif choice3 == "blue":
            print("The room is full of rogue bots. Game over.")
        else:
            print("You chose a door that doesn't exist. System error! Game over.")
    else:
        print("You got attacked by electric eels in the lake. Game over.")
else:
    print("You fell into a maintenance pit. Game over.")
