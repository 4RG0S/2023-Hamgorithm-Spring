#include <stdio.h>
int main()
{
	 int i, j, c=0;
	char word[5][16]={0};
	
 
    for(c = 0; c < 5;c ++)
    {
     	scanf("%s",word[c]); 	
	}

    for(i = 0; i < 16; i++)
    {
    	for(j = 0; j < 5 ; j++)
    	{	
			if(((word[j][i]>='A')&&(word[j][i]<='Z'))||((word[j][i]>='a')&&(word[j][i]<='z'))||
			((word[j][i]>='0')&&(word[j][i]<='9')))
			{
				printf("%c",word[j][i]);
			}
    	
		}
	}
	
}