// Done as part of Cs50x

#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

//Arrays
char LETTERS[] = { 'a' , 'b' , 'c' , 'd' , 'e' ,'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' ,'v' , 'w' , 'x' , 'y' , 'z' };

//Prototypes
int validate_key(string key, int arg);
void encipher(string key);

int main(int arg, string argv[])
{
    string key = argv[1];

    if(arg != 2)
    {
        printf("Usage: ./substitution KEY\n");
        return 1;
    }

    //runs the program if key is valid
    if(validate_key(key, arg) == 0)
    {
        encipher(key);
        return 0;
    }
    else
    {
        return 1;
    }
}

//Functions
int validate_key(string key, int arg)
{
    //keeps track of problems
    int counter = 0 ;

    //length of key
    int n = strlen(key);

    //checks if key contains 26 characters
    if(n < 26)
    {
        printf("Key does not contain 26 characters\n");
        counter = 1;
    }

    //checks if key contains repeated characters
    for(int i = 0 ; i < n ; i++)
    {
        for(int x = i + 1 ; x <= n ; x++)
        {
            if(key[i] == key[x])
            {
                printf("Key must not contain repeated chracters\n");
                counter = 2 ;
            }
        }
    }

    //checks if key contains non-alphabetic characters
    for(int x = 0 ; x < n ; x++)
    {
        if(isalpha(key[x]))
        {

        }
        else
        {
            printf("Key must only contain alphabetic characters\n");
            counter = 3;
        }
    }
    return counter;
}

void encipher(string key)
{
    string plain_text = get_string("plaintext: ");
    printf("ciphertext: ");
    //enciphers plain text into cipher text
    for(int i = 0 , n = strlen(plain_text) ; i < n; i++)
    {
        //checks if character at ith position is an alphabet
        if(isalpha(plain_text[i]))
        {
            for(int x = 0 ; x < 26 ; x++)
            {
                //prints the replacement of the letter at ith position
                if(plain_text[i] == tolower(LETTERS[x]))
                {
                    printf("%c",tolower(key[x]));
                }
                else if(plain_text[i] == toupper(LETTERS[x]))
                {
                    printf("%c",toupper(key[x]));
                }
            }

        }
        else
        {
            printf("%c",plain_text[i]);
        }
    }
    printf("\n");
}


