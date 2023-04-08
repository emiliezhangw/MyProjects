// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol!\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    bool is_digit = false;
    bool is_symbol = false;
    bool is_upperletter = false;
    bool is_lowerletter = false;
    int n = strlen(password);
    for (int i = 0; i < n; i++)
    {
        if (isupper(password[i]))
        {
            is_upperletter = true;
        }
        if (islower(password[i]))
        {
            is_lowerletter = true;
        }
        if (isdigit(password[i]))
        {
            is_digit = true;
        }
        if (password[i] == '!' || password[i] == '?' || password[i] == ',' || password[i] == '.' || password[i] == '('
            || password[i] == ')' || password[i] == '~' || password[i] == '@' || password[i] == '#' || password[i] == '%' || password[i] == '^'
            || password[i] == '&' || password[i] == '*' || password[i] == '-' || password[i] == '=' || password[i] == '_' || password[i] == '+'
            || password[i] == '[' || password[i] == ']' || password[i] == '{' || password[i] == '}' || password[i] == '|' || password[i] == '<'
            || password[i] == '>' || password[i] == '/' || password[i] == '`')
        {
            is_symbol = true;
        }
    }
    if (is_digit && is_symbol && is_upperletter && is_lowerletter)
    {
        return true;
    }
    return false;
}
