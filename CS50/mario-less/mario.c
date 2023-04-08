#include <cs50.h>
#include <stdio.h>

int get_height(void);
void print_pyramid(int height);

//print an left-aligned pyramid with the user input height
int main(void)
{
    int i = get_height();
    print_pyramid(i);
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
//print left-aligned pyramid of the height

void print_pyramid(int height)
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 1; j < height - i; j++)
        {
            printf(" ");
        }
        for (int k = 0; k <= i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}