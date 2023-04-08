// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string text);

int main(int argc, string argv[])
{
    //make sure the program will run with only one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./no-vowels word\n");
        return 1;
    }
    //replace the vowels on the word with numbers
    string word = replace(argv[1]);
    printf("%s\n", word);
}
//replace each vowels in the string into a specific number
string replace(string text)
{
    for (int i = 0; i < strlen(text); i++)
    {
        switch (text[i])
        {
            case 'a':
                text[i] = '6';
                break;
            case 'e':
                text[i] = '3';
                break;
            case 'i':
                text[i] = '1';
                break;
            case 'o':
                text[i] = '0';
                break;
            default:
                break;
        }
    }
    return text;
}
