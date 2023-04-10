#include <stdio.h>
int main()
{
int a,b=0;
scanf("%d %d",&a,&b);
int max1=0;   // L=A*B/G
for(int k=1;k<=a;k++)
{
   if((a%k==0)&&(b%k==0))
   {    
       if(max1<=k)
       {max1=k;}
   }
   
}
int min1=(a*b)/max1;
printf("%d\n%d",max1,min1);






}