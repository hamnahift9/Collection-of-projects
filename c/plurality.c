// Done as part of Cs50x 

#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
    return 0;
}

// Update vote totals given a new vote
bool vote(string name)
{
    bool vote_result = false;
    for (int i = 0; i < candidate_count ; i++)
    {
        if (strcmp(name, candidates[i].name) == 0)
        {
            candidates[i].votes ++ ;
            vote_result = true;
        }
    }
    return vote_result;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    for (int i = 0; i < 9 ; i++)
    {
        for (int x = 0; x < 9; x++)
        {
            //checks if at any point the number of ith votes is lesser than the number of xth votes
            if (candidates[i].votes < candidates[x].votes)
            {
                //turns all the votes that are lesser than other votes to 0 leaving only the largest values 
                candidates[i].votes = 0;
            }
        }
        //prints the names associated with the non 0 values
        if (candidates[i].votes != 0)
        {
            printf("%s\n", candidates[i].name);
        }
    }

}

