// Done as part of Cs50x
// Simulate genetic inheritance of blood type

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Each person has two parents and two alleles
typedef struct person
{
    struct person *parents[2];
    char alleles[2];
}
person;

const int GENERATIONS = 3;
const int INDENT_LENGTH = 4;

person *create_family(int generations);
void print_family(person *p, int generation);
void free_family(person *p);
char random_allele();

int main(void)
{
    // Seed random number generator
    srand(time(0));

    // Create a new family with three generations
    person *p = create_family(GENERATIONS);

    // Print family tree of blood types
    print_family(p, 0);

    // Free memory
    free_family(p);
}

// Create a new individual with `generations`
person *create_family(int generations)
{
    // TODO: Allocate memory for new person
    person *p = malloc(sizeof(person));

    // Generation with parent data
    if (generations > 1)
    {
        // TODO: Recursively create blood type histories for parents
        for (int i = 0 ; i < 2 ; i++)
        {
            p->parents[i] = create_family(1);
        }
        // TODO: Randomly assign child alleles based on parents
        for (int i = 0 ; i < 2 ; i++)
        {
            int r = rand() % 2;
            p->parents[0]->alleles[i] = p->parents[0]->parents[i]->alleles[r];
            int rtwo = rand() % 2;
            p->parents[1]->alleles[i] = p->parents[1]->parents[i]->alleles[rtwo];
        }
        int r = rand() % 2;
        p->alleles[0] = p->parents[0]->alleles[r];
        int rtwo = rand() % 2;
        p->alleles[1] = p->parents[1]->alleles[rtwo];
    }
    // Generation without parent dat
    else
    {
        // TODO: Set parent pointers to NULL
        p->parents[0] = malloc(sizeof(person));
        p->parents[1] = malloc(sizeof(person));
    
        for (int i = 0 ; i < 2 ; i++)
        {
            p->parents[0]->parents[i] = NULL;
            p->parents[1]->parents[i] = NULL;
        }
        // TODO: Randomly assign alleles
        for (int i = 0 ; i < 2 ; i++)
        {
            p->parents[0]->alleles[i] = random_allele();
            p->parents[1]->alleles[i] = random_allele();
        }
    }
    return p;
}

// Free `p` and all ancestors of `p`.
void free_family(person *p)
{
    // TODO: Handle base case
    if (p == NULL)
    {
        return;
    }
    // TODO: Free parents
    for (int i = 0; i < 2 ; i++)
    {
        for (int x = 0 ; x < 2 ; x++)
        {
            free(p->parents[i]->parents[x]);
        }
    }
    for (int i = 0; i < 2 ; i++)
    {
        free(p->parents[i]);
    }

    // TODO: Free child
    free(p);
}

// Print each family member and their alleles.
void print_family(person *p, int generation)
{
    // Handle base case
    if (p == NULL)
    {
        return;
    }

    // Print indentation
    for (int i = 0; i < generation * INDENT_LENGTH; i++)
    {
        printf(" ");
    }

    // Print person
    printf("Generation %i, blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    print_family(p->parents[0], generation + 1);
    print_family(p->parents[1], generation + 1);
}

// Randomly chooses a blood type allele.
char random_allele()
{
    int r = rand() % 3;
    if (r == 0)
    {
        return 'A';
    }
    else if (r == 1)
    {
        return 'B';
    }
    else
    {
        return 'O';
    }
}
