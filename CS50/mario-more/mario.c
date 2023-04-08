#include <cs50.h>
#include <stdio.h>

int get_height(void);
void print_pyramid(int n);

//print two adjacent pyramid with the user input height and a gap of two hashes
int main(void)
{
    int height = get_height();
    print_pyramid(height);
}

//prompt user for height
int get_height(void)
{
    int i;
    do
    {
        i = get_int("Height: ");
    }
    while (i < 1 || i > 8);
    return i;
}

//print the two adjacent pyramid of the height and gap
void print_pyramid(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 1; j < n - i; j++)
        {
            printf(" ");
        }
        for (int k = 0; k <= i; k++)
        {
            printf("#");
        }
        printf("  ");
        for (int l = 0; l <= i; l++)
        {
            printf("#");
        }
        printf("\n");
    }
}