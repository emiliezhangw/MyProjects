#include <stdio.h>
//#include <cs50.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    printf("%p\n", p);
    printf("%i\n", *p);

    //string s = "HI!";
    //printf("%p\n", s);
    //printf("%p\n", &s[0]);
    //printf("%p\n", &s[1]);
    //printf("%p\n", &s[2]);
    //printf("%p\n", &s[3]);

    char *s = "HI!";
    printf("%p\n", s);
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);

    printf("%c\n", s[0]);
    printf("%c\n", s[1]);
    printf("%c\n", s[2]);

    printf("%c\n", *s);
    printf("%c\n", *(s + 1));
    printf("%c\n", *(s + 2));
}