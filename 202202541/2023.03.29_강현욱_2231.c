#include <stdio.h>
int jali(int a);
int sum(int a);
int main()
{
	int k=0;
	scanf("%d",&k);
	int ui=0; int a[100]={0};
	for(int r=1;r<=9*jali(k);r++)
	{
		if(r==sum(k-r))
		{
		a[r-1]=k-r;	
		 ui=1;
	    }
	}
    if(ui==0)
    {
	printf("%d",0);
	}
	for(int r=9*jali(k);r>=1;r--)
	{
		if(a[r-1]!=0)
		{
			printf("%d",a[r-1]);
			break;
		}
	}
	
}
int jali(int a)
{
	 int count =1;
	while(1)
	{
		a=a/10;
		
		if(a==0)
		{break;
		}
		count++;
		
	}
	return count;
}
int sum(int a)
{
	int sum=0; int b=0;
	while(1)
	{
		
		b=a%10;
		a=a/10;
		sum=sum+b;
	    if(a==0)
		{break;
		}
	}
	
	return sum;
}