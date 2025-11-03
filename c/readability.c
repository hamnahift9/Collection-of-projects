// Done as part of Cs50x

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

//Array
char LETTERS[] = { 'a' , 'b' , 'c' , 'd' , 'e' ,'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' ,'v' , 'w' , 'x' , 'y' , 'z' };


//Prototypes 
int calc_letters(string text);
int calc_words(string test);
int calc_sentences(string text);


int main(void)
{
    //user input
    string text = get_string("Text:");
    
    //storing letters,words and sentences
    int letters = calc_letters(text);
    int words = calc_words(text);
    int sentences = calc_sentences(text);
    
    //average number of letters per 100 words
    float L = (letters / (float)words) * 100;

    //average number of sentences per 100 words
    float S = (sentences / (float )words) * 100;
    
    //Coleman-liau index
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    
    if(index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if(index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n",index);
    }
}

//Functions
//Calculates the number of letters in the given text
int calc_letters(string text)
{
    
    int counter = 0;
      for (int i = 0, n = strlen(text); i < n ; i++) 
    {
        if(isalpha(text[i]))
        {
            counter ++;
         }
    }
    return counter;
}


//calculates the number of words in the given text
int calc_words(string text)
{
    int counter = 1;
    for (int i = 0, n = strlen(text); i < n ; i++) 
    {
        //checks if the char at ith position is a space
        if (text[i] == ' ' ) 
        {
          counter ++;
        }
    }
    return counter;
}

//calculates the number of sentences in the given text
int calc_sentences(string text)
{
    int counter = 0;
    for(int i = 0 , n = strlen(text) ; i < n ; i++)
    {
        if(text[i] == '.' ) 
        {
            counter++;
        }
        else if(text[i] == '!')
        {
            counter++;
        }
        else if(text[i] == '?')
        {
            counter++;
        }
    }
    return counter;
}













