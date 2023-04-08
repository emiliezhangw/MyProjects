#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);
int num;

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    num = input[0] - 48;

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    if (strlen(input) <= 1)
    {
        return num;
    }
    for (int i = 0; i < strlen(input); i++)
    {
        input[i] = input[i + 1];
    }
    num = num * 10 + input[0] - 48;
    convert(input);
    // TODO
    return num;
}