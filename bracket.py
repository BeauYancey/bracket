import random
from sys import argv
from datetime import datetime
from predictors import fetch_bpi, win_probability

BPI = {}

def main():
    print('Enter "quit" at any time to terminate the program')
    while(True):
        # Get team 1 data
        team1 = input("Enter the abbreviation of the first team: ")
        if team1 == "quit":
            break
        bpi1 = 0
        try:
            bpi1 = BPI[team1]
        except:
            bpi_str = input(f"We couldn't find {team1}'s BPI. Please enter it now: ")
            if bpi_str == "quit":
                break
            bpi1 = float(bpi_str)

        # Get team 2 data
        team2 = input("Enter the abbreviation of the second team: ")
        if team2 == "quit":
            break
        bpi2 = 0
        try:
            bpi2 = BPI[team2]
        except:
            bpi_str = input(f"We couldn't find {team2}'s BPI. Please enter it now: ")
            if bpi_str == "quit":
                break
            bpi2 = float(bpi_str)

        # Compute win probability given BPIs
        chance = win_probability(bpi1, bpi2)

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
        BPI = fetch_bpi(364) # Get BPIs for all 364 D1 NCAA basketball teams
        main()
    elif (len(argv) == 4):
        print(predict_winner(argv[1], argv[2], float(argv[3])))
    else:
        print("INVALID USAGE")
