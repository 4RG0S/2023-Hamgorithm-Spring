#include <stdio.h>
int main()
{
    int x=0;
    scanf("%d",&x);
    int y=0;
    int z=0;
    for(y=0;y<x;y++)
    {
        for(z=0;z<y;z++)
        {
            printf(" ");
        }
        for(z=y;z<x;z++)
        {
             printf("*");
         }
        
       printf("\n"); 
     }
    
    
    
    
}