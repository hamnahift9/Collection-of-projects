// Done as part of Cs50x 

#include <stdio.h>
#include <cs50.h>

int limited_input(void);
void make_hashes(int i);
void make_spaces(int);

int main(void)
{
    //Gets user input
    int height = limited_input();
    
    //Iterates through height
    for (int i = 1; i <= height ; i++)
    {
        // Makes height - i number of spaces
        make_spaces(height - i);
        
        //Makes 2i number of hashes with a space at i
        make_hashes(i);
        printf("  ");
        make_hashes(i);
        
        //Prints new line
        printf("\n");
    }
}

//Functions
//Makes hashes
void make_hashes(int i)
{

    //Makes i number of hashes
    for (int j = 0; j < i; j++)
    {
        printf("#");
    }
}

//Makes spaces
void make_spaces(int i)
{

    //Makes i-1 number of spaces
    for (int j = 0 ; j < i ; j++)
    {
        printf(" ");
    }
}

//Limits user_input
int limited_input(void)
{
    int height = 0;
    do
    {
        height = get_int("Height:");
    }
    while (height > 8 || height < 1);

    return height;
}
