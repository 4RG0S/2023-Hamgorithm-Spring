#include <stdio.h>
int main()
{
	int a,b=0;
	scanf("%d %d",&a,&b);
	int c=0;
	int num[a+1];
	for(c=0;c<a+1;c++)
	{
		num[c]=0;
	}

	int i,j=0;
	for(i=1;i<=a;i++)
	{    
		if(a%i==0)
		{   j++;
			num[j]=i;
			
		}	
		
	}

	if(j>=b)
	{
		printf("%d",num[b]);
	}
	else
	{
		printf("%d",0);
	}
	
	
	
}