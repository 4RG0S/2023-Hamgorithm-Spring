#include <stdio.h>
int main()
{  	int a=0;
	scanf("%d",&a);
	int b=0;
	int w=0;
	for(b=0;b<a;b++)
	{
		int num1,num2=0;
		unsigned long long int e=1;
		scanf("%d %d",&num1,&num2);
		for(w=0;w<num2;w++)
		{
			e=e*num1;
			e=e%10;
		}
   		
		if(e!=0)
		{
		  printf("%d",e);
		
		}		
		else if(e==0)
		{
		  printf("%d",10);
		
		}
	
	  	
	}
	
	
}