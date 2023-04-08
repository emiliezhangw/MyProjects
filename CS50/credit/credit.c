#include <cs50.h>
#include <stdio.h>

long get_cardnumber(void);
void check_card(long n);
bool luhn_algorithm(long n);

//get card number from user and check if it is amex, mastercard, visa or invalid card
int main(void)
{
    long cardnumber = get_cardnumber();
    check_card(cardnumber);
}

//prompt user for cardnumber
long get_cardnumber(void)
{
    long l = get_long("Number: ");
    return l;
}

//check if the card is amex
bool is_amex(long n)
{
    int i = n / 10000000000000;
    if (i == 34 || i == 37)
    {
        if (luhn_algorithm(n))
        {
            return true;
        }
    }
    else
    {
        return false;
    }
    return false;
}

//check if the card is mastercard
bool is_mastercard(long n)
{
    int i = n / 100000000000000;
    if (i >= 51 && i <= 55 && luhn_algorithm(n))
    {
        if (luhn_algorithm(n))
        {
            return true;
        }
    }
    else
    {
        return false;
    }
    return false;
}

//check if the card is visa
bool is_visa(long n)
{
    int i = n / 1000000000000;
    int j = n / 1000000000000000;

    if (i == 4 || j == 4)
    {
        if (luhn_algorithm(n))
        {
            return true;
        }
    }
    else
    {
        return false;
    }
    return false;
}

//check if the card is valid using luhn's algorithm
bool luhn_algorithm(long n)
{
    int sum = 0;
    int i = 0;
    while (n > 0)
    {
        if (i % 2 == 0)
        {
            sum = sum + n % 10;
        }
        else
        {
            if ((n % 10) < 5)
            {
                sum = sum + (n % 10) * 2;
            }
            else
            {
                sum = sum + n % 10 * 2 / 10 + n % 10 * 2 % 10;
            }
        }
        n = n / 10;
        i++;
    }
    if (sum % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

//call the methods to check if the card is amex, mastercard, visa or invalid
void check_card(long n)
{
    if (is_amex(n))
    {
        printf("AMEX\n");
    }
    else if (is_mastercard(n))
    {
        printf("MASTERCARD\n");
    }
    else if (is_visa(n))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

