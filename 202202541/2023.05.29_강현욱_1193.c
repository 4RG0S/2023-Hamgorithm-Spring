#include <stdio.h>
int main()
{
	int num=0;
	scanf("%d",&num);
	int x=1; 
	int y=0;
	while(1)
	{
		if(num<=x*(x+1)/2)
		{
			break;
		}
		x++;
		
	}
	if(x%2==0)
	{   y=(x-1)*(x)/2;
		printf("%d/%d",num-y,x-(num-y)+1);
	}	
	else if(x%2!=0)
    {
    	y=(x-1)*(x)/2;
		printf("%d/%d",x-num+y+1,num-y);
    	
    	
	}
	
	
	
	
	
	
	
}