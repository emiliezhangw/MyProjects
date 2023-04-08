#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

//prompt user for text and compute the grade level
int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    float L = (float)letters / words * 100;
    float S = (float)sentences / words * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }

}
//count the number of letters
int count_letters(string text)
{
    int l = strlen(text);
    int n = 0;
    for (int i = 0; i < l; i++)
    {
        if (islower(text[i]) || isupper(text[i]))
        {
            n += 1;
        }
    }
    return n;
}
//count the number of words
int count_words(string text)
{
    int l = strlen(text);
    int n = 1;
    for (int i = 0; i < l; i++)
    {
        if (text[i] == ' ')
        {
            n += 1;
        }
    }
    return n;
}
//count the number of sentences
int count_sentences(string text)
{
    int l = strlen(text);
    int n = 0;
    for (int i = 0; i < l; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            n += 1;
        }
    }
    return n;
}
