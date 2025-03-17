# March Madness Brakcet Builder

## How does the program work?
There are some key differences between the C program the python program. The python program gets BPI information from ESPN's API, and uses that data to calculate the probability of a certain team beating a certain other team. The C program requires the user to input the probability of a certain team beating a certain other team.

The program generates a random number and compares that number to the chance of Team A winning. If the random number is greater than the chance of Team A winning, then we predict that Team B will win. If the random number is less than the chance of Team A winning, then we predict that Team A will win.

Please note that **this is entirely random.** I do not wish to be liable for any losses that you may stake on your *perfect brakcet* this year

## How to run the program
### If you have python installed:
- Just run `python3 bracket.py` in your command line application (such as Powershell).
- You can stop the program at any time by typing "quit" or by entering "CTRL + C".

### If you don't have python installed:
- Compile the C program by running `gcc -o bracket bracket.c` in your command line application (such as Powershell).
  - If the `gcc` command does not work, try using `clang` instead of `gcc`.
- Execute the compiled program by running `./bracket`.
- You can stop the program at any time by typing "quit" or by entering "CTRL + C".
