import random

is_exit = False

def main():
    print("Welcome to Battleship Game!")
    print("Main Menu:")
    print("1 - Start", "2 - How to", "3 - Exit", sep="\n")
    choice = input("Select one of the menu: ")
    if int(choice) == 1:
        start_game()
    elif int(choice) == 2:
        how_to()
    elif int(choice) == 3:
        global is_exit
        print("Good Bye!")
        is_exit = True
    else:
        print("Please select the number")
        
def start_game():
    coor = [
        ['o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o']
    ]
    targetr = random.randint(0, len(coor))
    targetc = random.randint(0, len(coor))
    while True:
        print(*coor, sep='\n')
        row = input("row: ")
        col = input("column: ")
         
        print("coordinate: " + "({}, {})".format(row, col))
        if row.isdigit() and col.isdigit():
            row = int(row)
            col = int(col)
            if row < len(coor) and col < len(coor):
                if row == targetr and col == targetc:
                    print("You found the ship!")
                    break
                elif coor[row][col] == 'o':
                    coor[row][col] = 'x'
                else:
                    print("Your coordinate has already evaluated!")
            else:
                print("Your coordinate out of range!")
        else:
            print("You don\'t give valid coordinate!")


def how_to():
    pass


if __name__ == "__main__":
    while not is_exit:
        main()
