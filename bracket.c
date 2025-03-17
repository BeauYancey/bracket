#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void main_loop();
const char* predict_winner(const char* team1, const char* team2, double chance);
double roll();

int main(int argc, char *argv[]) {
    srand(time(NULL));
    if (argc == 1) {
	// No cmd line arguments, run continuous loop
        main_loop();
    } else if (argc == 4) {
	// Two teams and a probability provided, just predict the winner
        printf("%s\n", predict_winner(argv[1], argv[2], atof(argv[3])));
    } else {
        printf("INVALID USAGE\n");
    }
    return 0;
}

void main_loop() {
    char team1[26], team2[26], chance_str[6];
    double chance;
    
    printf("Enter \"quit\" at any time to terminate the program\n");
    
    while (1) {
        printf("Enter the name of the higher seeded team: ");
        scanf("%25s", team1);
        if (strcmp(team1, "quit") == 0) break;
        
        printf("Enter the name of the lower seeded team: ");
        scanf("%25s", team2);
        if (strcmp(team2, "quit") == 0) break;
        
        printf("Enter the chances that %s will win as a decimal (i.e. 86.1%% -> .861): ", team1);
        scanf("%5s", chance_str);
        if (strcmp(chance_str, "quit") == 0) break;
        
        chance = atof(chance_str);
        
        printf("\n\t\033[1m%s\033[0m will win this game\n\n", predict_winner(team1, team2, chance));
    }
}

const char* predict_winner(const char* team1, const char* team2, double chance) {
    return (chance > roll()) ? team1 : team2;
}

double roll() {
    return (double)rand() / RAND_MAX;
}

