game_list = [0, 1, 2]


def display_game(game_list):
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

    game_on = "Y"

    while game_on == "Y":
        pos = position_choice()
        replace_value(pos)
        display_game(game_list)
        game_on = input("Want to continue(Y or N): ")


game_on()
