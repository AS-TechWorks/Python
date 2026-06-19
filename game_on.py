game_list = [0, 1, 2]

def display_game():
    print("Here is the current game list:")
    print(game_list)

def position_choice():

    choice = "wrong"
    while choice not in ["0", "1", "2"]:
        choice = input("Enter a position choice from (0,1,2): ")
        if choice not in ["0", "1", "2"]:
            print("sorry, wrong input!")

    return int(choice)


def replace_value(pos):
    game_list[pos] = input("Enter new value: ")


def game_on():

    choice = "wrong"
    while choice not in ["Y", "N"]:
        choice = input("Want to continue playing game (Y/N): ")
        
        if choice not in ["Y", "N"]:
            print("Incorrect input, please enter Y or N")

    if choice == "Y":
        return True
    else:
        return False

display_game()
while game_on():
    pos = position_choice()
    replace_value(pos)
    display_game()
    