#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(void)
{
    char N[3001], R[10000];
    int r, c = 0;
    scanf("%s", N);
    for (int i = 1;; i++)
    {
        r = i;
        sprintf(R, "%d", r);
        for (int j = 0; j < strlen(R); j++)
        {
            if (N[c] == R[j]) c++;
        }
        if (c == strlen(N)) break;
    }
    printf("%d", r);

    return 0;
}