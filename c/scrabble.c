// Done as part of Cs50x

#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
//Lower case alphabets
char LETTERS[] ={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
//Upper case alphabets
char LETTERS2[] ={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1) ;
    int score2 = compute_score(word2);

    //Prints the winner
    if (score1 > score2)
    {
        printf("Player 1 wins! \n");
    }
    else if(score1 < score2)
    {
        printf("Player 2 wins! \n");
    }
    else
    {
        printf("Tie! \n");
    }
}

//Computes score
int compute_score(string word)
{
    //keeps track of total score
    int counter = 0;
    //iterates over characters in string 
    for (int i = 0, n = strlen(word); i < n ; i++) 
    {
        //iterates over char in array
        for (int x = 0 ; x < 26 ; x++) 
        {
            //checks if the char at ith position is equal to a char in LETTERS at the xth position
            if (word[i] == LETTERS[x] ) 
            {
               counter += POINTS[x];
            }
            else if(word[i] == LETTERS2[x])
            {
                counter += POINTS[x];
            }
        }
    }
    return counter;
}