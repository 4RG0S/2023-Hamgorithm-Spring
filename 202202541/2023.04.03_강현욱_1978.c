#include <stdio.h>
int main()
{
	int a=0;
	scanf("%d",&a);
	int num[a];
	for(int b=0;b<a;b++)
	{
		scanf("%d",&num[b]);
	}
	
	for(int c=0;c<a;c++)
	{
		for(int d=2;d<num[c];d++)
		{
			if(num[c]%d==0)
			{
				num[c]=1001;
				break;
			}
			
		}
		
		
	}
	int count=0;
	for(int i=0;i<a;i++)
	{
		if(num[i]==1)
		continue;
		else if(num[i]!=1001)
		count++;
		
		
	}
	printf("%d",count);
	
	
	
	
}