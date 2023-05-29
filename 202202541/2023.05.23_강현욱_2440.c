#include <stdio.h>
int main()
{
    int x=0;
    scanf("%d",&x);
    int i,j=0;
    for(i=x;i>0;i--)
    { 
     for(j=0;j<i;j++)
     {
         printf("*");
     }
        printf("\n");

       
    }  
    
    
    
}