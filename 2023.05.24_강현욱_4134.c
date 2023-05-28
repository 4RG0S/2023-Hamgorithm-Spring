#include <stdio.h>
int main()
{
	
	int ty =0;
	scanf("%d",&ty);
	long long i,j,num=0;
	int k=9;
	for(i=0;i<ty;i++)
	{
		scanf("%lld",&num);
		if(num==0||num==1)
		{
		printf("%d\n",2);
	 	}
	 
		else
		{
		while(1)
		{
			k=9;
	    	for(j=2;j*j<=num;j++)
			{
				if(num%j==0)
				{
					k=0;
					break;
				}
				
			}
			if(k==9)
			{
				printf("%lld\n",num);
				break;
			}
			num++;
		}
		}
		
	}
}