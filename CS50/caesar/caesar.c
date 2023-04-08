#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

//add the function’s prototype, atop the file, enables main to call it
bool only_digits(string text);
char rotate(char letter, int k);

int main(int argc, string argv[])
{
    //make sure program will run with just one command-line argument, that means argc should equal 2
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    //make sure every character in argv[1] is a digit
    else if (!only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        //convert argv[1] from a 'string' to an 'int' with atoi function
        int k = atoi(argv[1]);

        //prompt user for plaintext
        string text = get_string("plaintext:  ");
        int n = strlen(text);
        printf("ciphertext: ");
        //for every character in the plaintext, rotate the character which is a letter by k positions, while non-alphabetical characters unchanged
        for (int i = 0; i < n; i++)
        {
            printf("%c", rotate(text[i], k));
        }
        printf("\n");
        return 0;
    }
}

//decide whether argument is a number
bool only_digits(string text)
{
    int l = strlen(text);
    for (int i = 0; i < l; i++)
    {
        if (text[i] > 57 || text[i] < 48)
        {
            return false;
        }
    }
    return true;
}

char rotate(char c, int n)
{
    if (isupper(c))
    {
        return (c - 65 + n) % 26 + 65;
    }
    else if (islower(c))
    {
        return (c - 97 + n) % 26 + 97;
    }
    else
    {
        return c;
    }
}
