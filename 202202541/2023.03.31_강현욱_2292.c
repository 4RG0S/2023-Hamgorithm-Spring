#include <stdio.h>
int main()
{
	int a=0; int b=1;
	int c=0;
	scanf("%d",&a);
	
	while(1)
	{    
	    if(a==1)
	    {
	    	printf("%d",1);
	    	break;
		}
		
		else
		{
		if(b==1)
		{
		c=a-((b-1)*6)-1;
		if(c<=6)
		{
			printf("%d",2);
			break;
		}
	    }
	    
	    else if(b>=2)
	    {
	    		c=c-((b-1)*6);
	    if(c<=6*b)
		{   
			printf("%d",b+1);
			break;
		}
		
	
		
	
		
	    }
		b++;
	    }
	}
	
	
}