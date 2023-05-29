#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

struct point {
    int x;
    int y;
};

int main()
{
    struct point a, b, c;
    float checker1 = 0;
    float checker2 = 0;
    int len_ab = 0;
    int len_bc = 0;
    int len_ca = 0;
    int comp1 = 0;
    int comp2 = 0;
    scanf("%d%d", &a.x, &a.y);
    scanf("%d%d", &b.x, &b.y);
    scanf("%d%d", &c.x, &c.y);

    checker1 = (b.y - a.y) / ((float)b.x - a.x);
    checker2 = (c.y - b.y) / ((float)c.x - b.x);

    if (checker1 == checker2)
    {
        printf("X");
        exit(EXIT_SUCCESS);
    }
    else
    {
        len_ab = ((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
        if (comp1 < len_ab)
            comp1 = len_ab;
        len_bc = ((b.x - c.x) * (b.x - c.x) + (b.y - c.y) * (b.y - c.y));
        if (comp1 < len_bc)
            comp1 = len_bc;
        len_ca = ((c.x - a.x) * (c.x - a.x) + (c.y - a.y) * (c.y - a.y));
        if (comp1 < len_ca)
            comp1 = len_ca;
        comp2 = len_ab + len_bc + len_ca - comp1;

        if (len_ab == len_bc && len_bc == len_ca)
        {
            printf("JungTriangle");
            exit(EXIT_SUCCESS);
        }
        else if (len_ab != len_bc && len_bc != len_ca && len_ca != len_ab)
        {
            if (comp1 > comp2)
            {
                printf("DunkakTriangle");
                exit(EXIT_SUCCESS);
            }
            else if (comp1 == comp2)
            {
                printf("JikkakTriangle");
                exit(EXIT_SUCCESS);
            }
            else
            {
                printf("YeahkakTriangle");
                exit(EXIT_SUCCESS);
            }
        }
        else
        {
            if (comp1 > comp2)
            {
                printf("Dunkak2Triangle");
                exit(EXIT_SUCCESS);
            }
            else if (comp1 == comp2)
            {
                printf("Jikkak2Triangle");
                exit(EXIT_SUCCESS);
            }
            else
            {
                printf("Yeahkak2Triangle");
                exit(EXIT_SUCCESS);
            }
        }
    }
    return 0;
}