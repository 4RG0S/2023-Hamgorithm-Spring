#include <stdio.h>
int key(int a);
int main()
{
	int x=0;
	scanf("%d",&x);
	int y=666;
	int z=0;
	while(1)
    {
    	if(key(y))
    	{
    		
    	z++;	
		}
    	y++;
    	if(x==z)
    	{
    		break;
	}
	}	
	printf("%d",y);
}
int key(int a)
{
    int num[10]={0};
    int u=0;
    int z=0;
    int k=0;
    while(1)
    {
    	num[z]=a%10;
    	a=a/10;
    	
    	z++;
    	if(a==0)
    	{
    		break;
		}
	}
	for(k=0;k<=7;k++)
    {
	if((num[k]==6)&&(num[k+1]==6)&&(num[k+2]==6))
	{
		u=1;
	}
    }
    
	return u;

}