#include <stdio.h>
#include <string.h>
int multiply(int n1,int n);
int main()
{
	int num1=0;
	char num3[100000];
	scanf("%s %d",num3,&num1);
	int i=0; int sum=0;
	int length=strlen(num3);
	for(i=1;i<=length;i++)
	{    
	
	    if((int)num3[length-i]>=65)
		{
		    sum=sum+((int)(num3[length-i])-55)*multiply(num1,i);
		}
		else
		{
			sum=sum+(int)(num3[length-i]-'0')*multiply(num1,i);
		}
			
	}
	printf("%d",sum);
	
	
}
int multiply(int n1,int n)
{
	
	int s=1;
	int g=0;
	if(n==1)
	{
	 return 1;
	}
	else{
	for(g=1;g<=n-1;g++)
	{
		s=s*n1;			
	}
	return s;
    }
	
}