import random

def Roll():
    dice_face = {
        1: (
            "____________",
            "|          |",
            "|          |",
            "|    @     |",
            "|          |",
            "|__________|",
        ), 
        2: (
            "____________",
            "|          |",
            "|  @       |",
            "|          |",
            "|       @  |",
            "|__________|",
        ), 
        3: (
            "____________",
            "|          |",
            "|  @       |",
            "|    @     |",
            "|       @  |",
            "|__________|",
        ),
        4: (
            "____________",
            "|          |",
            "|  @    @  |",
            "|          |",
            "|  @    @  |",
            "|__________|",
        ),
        5: (
            "____________",
            "|          |",
            "|  @    @  |",
            "|    @     |",
            "|  @    @  |",
            "|__________|",
        ),
        6: (
            "____________",
            "|          |",
            "|  @  @  @ |",
            "|          |",
            "|  @  @  @ |",
            "|__________|",
        ),
    }
    roll_dice = input("Press 'Y' to roll the dices or press 'N' to exit : ")
    
    while roll_dice.lower() == "Y".lower():
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)

        print("you got {} and {}".format(dice_1, dice_2))
        print("\n".join(dice_face[dice_1]))
        print("\n".join(dice_face[dice_2]))
        
        roll_dice = input("Roll Again Y/N : ")
    
Roll()
