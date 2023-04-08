#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool only_alphabetical(string text);
bool duplicate(string text);
char substitute(char c, string s);

int main(int argc, string argv[])
{
    //make make sure program will run with just one command-line argument, that means argc should equal 2
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    //make sure the length of argv[1] is 26, every character in argv[1] is a alphabetical and no dupilicate letters
    else if (!only_alphabetical(argv[1]) || strlen(argv[1]) != 26 || duplicate(argv[1]))
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    else
    {
        //prompt user for a string of plaintext
        string text = get_string("plaintext:  ");
        int n = strlen(text);
        printf("ciphertext: ");
        //substitute every character in the plaintext for the corresponding character in the ciphertext
        for (int i = 0; i < n; i++)
        {
            printf("%c", substitute(text[i], argv[1]));
        }
        printf("\n");
    }
    return 0;
}

//decide if argument is a alphabetical
bool only_alphabetical(string text)
{
    int l = strlen(text);
    for (int i = 0; i < l; i++)
    {
        if (!isalpha(text[i]))
        {
            return false;
        }
    }
    return true;
}

//decide if there are duplicate letters
bool duplicate(string text)
{
    int l = strlen(text);
    for (int i = 0; i < l; i++)
    {
        for (int j = 0; j < l; j++)
        {
            if (toupper(text[i]) == toupper(text [j]) && i != j)
            {
                return true;
            }
        }
    }
    return false;
}

//substitute character for the corresponding character in the ciphertext
char substitute(char c, string s)
{
    if (isupper(c))
    {
        if (isupper(s[c - 65]))
        {
            return s[c - 65];
        }
        else
        {
            return s[c - 65] - 32;
        }
    }
    else if (islower(c))
    {
        if (isupper(s[c - 97]))
        {
            return s[c - 97] + 32;
        }
        else
        {
            return s[c - 97];
        }
    }
    else
    {
        return c;
    }
}