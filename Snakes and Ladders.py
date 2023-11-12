from random import randint
import time
import os


# FUNCTIONS

# Get player names
def input_name(n):
    while True:
        print('')
        name = input(f" Player {n} name:  ")
        if len(name) > 5:
            print(" Please insert less than 6 char")
            continue
        elif len(name) == 0:
            print(" Please insert a name")
            continue
        elif len(name) <= 5:
            return name.upper()


# Product a random number between 1 and 6
def roll_dice():
    random = randint(1, 6)
    print(f' your roll: {random}')
    return random


# Run the game
def run_game(place, player_name):
    print('\n')
    input(f" {player_name} Press ENTER to roll dice: ")
    print('\n')
    new = roll_dice()
    if (100 - place) >= new:
        new_place = (place + new)
        # Check the snakes and ladders
        new_place = snake_ladder_handle(new_place)
        if new_place == 100:
            print(f'\n Congratulations... {player_name} WON ')
            time.sleep(4)
            quit()
        elif new_place != 100:
            return new_place, new
    else:
        print(' Sorry your dice is larger than you need')
    return place, new


# Player must roll a six for start the game
def start_game(player_name):
    input(f"\n {player_name} Press ENTER to roll dice. You can not move forward "
          f"until you roll a six: ")
    print('')
    start_dice = roll_dice()
    if start_dice == 6:
        return True
    else:
        return False


# Print and refresh the board
def print_board():
    time.sleep(1)
    os.system('cls')
    print()
    count = 100
    while count > 0:
        for j in range(10):
            snakes_ladders = snake_ladder_print(count)
            if snakes_ladders != count:
                print("{:^11}".format(snakes_ladders), end="")
                count -= 1
            else:
                section = str(count)
                if count == place_A and count == place_B:
                    section = f'{name_A}, {name_B}'
                elif count == place_B:
                    section = name_B
                elif count == place_A:
                    section = name_A
                print("{:^11}".format(section), end="")
                count -= 1
        print('\n\n')
        count -= 9
        for x in range(10):
            snakes_ladders = snake_ladder_print(count)
            if snakes_ladders != count:
                print("{:^11}".format(snakes_ladders), end="")
                count += 1
            else:
                section = str(count)
                if count == place_A and count == place_B:
                    section = f'{name_A}, {name_B}'
                elif count == place_B:
                    section = name_B
                elif count == place_A:
                    section = name_A
                print("{:^11}".format(section), end="")
                count += 1
        print('\n\n')
        count -= 11


# Place the snakes and ladders on the board
def snake_ladder_print(number):
    if number in snakes:
        return f'--{snakes[number]}--'
    elif number in ladders:
        return f'++{ladders[number]}++'
    else:
        return number


# Manage of bit and climb
def snake_ladder_handle(number):
    if number in snakes:
        print('\n The snake bit you')
        time.sleep(2)
        return snakes[number]
    elif number in ladders:
        print('\n You climbed a ladder')
        time.sleep(2)
        return ladders[number]
    else:
        return number


# INITIAL VALUES
(place_A, place_B) = (1, 1)
last_roll = 0
start_flag_player_A = False
start_flag_player_B = False

# Snakes Places
snakes = {
    17: 7,
    62: 19,
    54: 34,
    64: 60,
    87: 36,
    93: 73,
    95: 75,
    98: 79
}

# Ladders places
ladders = {
    4: 14,
    2: 38,
    9: 31,
    21: 42,
    28: 84,
    51: 67,
    72: 91,
    80: 99
}

name_A = input_name('A')
name_B = input_name('B')

while True:
    print_board()
    if start_flag_player_A:
        place_A, last_roll = run_game(place_A, name_A)
        print_board()
        while last_roll == 6:
            print()
            print(f" ***** {name_A} has an extra turn *****")
            place_A, last_roll = run_game(place_A, name_A)
            print_board()
    else:
        start_flag_player_A = start_game(name_A)
    if start_flag_player_B:
        place_B, last_roll = run_game(place_B, name_B)
        print_board()
        while last_roll == 6:
            print()
            print(f" ***** {name_B} has an extra turn *****")
            place_B, last_roll = run_game(place_B, name_B)
            print_board()
    else:
        start_flag_player_B = start_game(name_B)
