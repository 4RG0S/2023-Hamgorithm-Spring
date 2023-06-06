#include <stdio.h>
#include <string.h>

int main(void)
{
    char str1[1500];
    char str2[1500];

    int c1[256];
    int c2[256];
    int q = 0;
    int i;

    while (gets(str1))
    {
        gets(str2);
        for (i = 0; i < 256; i++)
            c1[i] = c2[i] = 0;

        for (i = 0; i < strlen(str1); i++)
        {
            c1[str1[i]]++;
        }
        for (i = 0; i < strlen(str2); i++)
        {
            c2[str2[i]]++;
        }

        for (i = 0; i < 256; i++)
        {
            while (c1[i] && c2[i])
            {
                putchar((char)i);
                c1[i]--;
                c2[i]--;
            }
        }
        putchar('\n');
    }

    return 0;
}
