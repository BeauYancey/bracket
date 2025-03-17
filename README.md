# March Madness Brakcet Builder
## How does the program work?
The program requires that you know the likelihood of any team beating any other team. These kinds of numbers can generally be found online, at least for the first round. The program generates a random number and compares that number to the chance of Team A winning. If the random number is greater than the chance of Team A winning, then we predict that Team B will win. If the random number is less than the chance of Team A winning, then we predict that Team A will win. Please note that **this is entirely random.** I will not be liable for any losses that you may stake on your *perfect brakcet* this year

## How to run the program
### If you have python installed:
Just run `python3 bracket.py` in your command line application (such as Powershell).
You can stop the program at any time by typing "quit" or by entering "CTRL + C".
### If you don't have python installed:
Compile the C program by running "gcc -o bracket bracket.c" in your command line application (such as Powershell).
If the `gcc` command does not work, try using `clang` instead of `gcc`.
Execute the compiled program by running `./bracket`.
You can stop the program at any time by typing "quit" or by entering "CTRL + C".
