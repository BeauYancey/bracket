import random
from sys import argv
from datetime import datetime

def main():
    print('Enter "quit" at any time to terminate the program')
    while(True):
        team1 = input("Enter the name of the higher seeded team: ")
        if team1 == "quit":
            break

        team2 = input("Enter the name of the lower seeded team: ")
        if team2 == "quit":
            break

        chance_str = input(f"Enter the chances that {team1} will win as a decimal (i.e. 86.1% -> .861): ")
        if chance_str == "quit":
            break
        chance = float(chance_str)

        print(f"\n\t\033[1m{predict_winner(team1, team2, chance)}\033[0m will win this game\n")
    return


def predict_winner(team1, team2, chance):
    val = roll()
    if (chance > val):
        return team1
    else:
        return team2

def roll():
    random.seed(datetime.now().timestamp())
    return random.random()

if __name__ == "__main__":
    if (len(argv) == 1):
        main()
    elif (len(argv) == 4):
        print(predict_winner(argv[1], argv[2], float(argv[3])))
    else:
        print("INVALID USAGE")
