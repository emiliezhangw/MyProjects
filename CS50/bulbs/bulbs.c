#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string text = get_string("Message: ");
    int l = strlen(text);
    int bit[BITS_IN_BYTE];
    for (int i = 0; i < l; i++)
    {
        int m = text[i];
        for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
        {
            if (m % 2 == 0)
            {
                bit[j] = 0;
            }
            else
            {
                bit[j] = 1;
            }
            m = m / 2;
        }
        for (int k = 0; k < BITS_IN_BYTE; k++)
        {
            print_bulb(bit[k]);
        }
        printf("\n");

    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
