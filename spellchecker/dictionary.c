// Implements the dictionary's functionality

#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

int wordcount = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 474554;

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int index = hash(word);
    node *tmp = table[index];
    while (tmp != NULL)
    {
        if (strcasecmp(word, tmp->word) == 0)
        {
            return true;
        }
        tmp = tmp->next;
    }
    free(tmp);
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    if (strlen(word) == 1)
    {
        return 0;
    }
    if (strlen(word) == 2)
    {
        return 1;
    }
    if (strlen(word) == 3)
    {
    int l0 = (int)toupper(word[0]) - 'A';
    int l1 = (int)toupper(word[1]) - 'A';
    int l2 = (int)toupper(word[2]) - 'A';
    int x = 2 + (l0 * 26 * 26) + (l1 * 26) + l2;
    return x;
    }
    else
    {
    int l0 = (int)toupper(word[0]) - 'A';
    int l1 = (int)toupper(word[1]) - 'A';
    int l2 = (int)toupper(word[2]) - 'A';
    int l3 = (int)toupper(word[3]) - 'A';
    int x = 17578 + (l0 * 26 * 26 * 26) +(l1 * 26 * 26) + (l2 * 26) + l3;
    return x;
    }
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }
    else
    {
        while (1)
        {
            char *w = malloc(LENGTH + 1);
            if (fscanf(file, "%s", w) == EOF)
            {
                break;
            }
            node *n = malloc(sizeof(node));
            if (n == NULL)
            {
                return false;
            }
            strcpy(n->word, w);
            n->next = NULL;
            int index = hash(w);
            if (table[index] == NULL)
            {
                table[index] = n;
                wordcount++;
            }
            else
            {
                n->next = table[index];
                table[index] = n;
                wordcount++;
            }
        }
    }
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return wordcount;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *tmp1 = table[i];
        node *tmp2 = table[i];
        while (tmp2 != NULL)
        {
            tmp2 = tmp2->next;
            free(tmp1);
            tmp1 = tmp2;
        }
        free(tmp2);
    }
    return true;
}
