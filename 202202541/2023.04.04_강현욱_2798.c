#include <stdio.h>
int main()
{
	int a=0; int u=0; int y=0;
	scanf("%d %d",&a,&u); 
	int num[a];
	for(int b=0;b<a;b++)
	{
	scanf("%d",&num[b]);
    }
    int c=0;
    for(int i=0;i<a;i++)
    {
    	 for(int j=0;j<a;j++)
    	 {
    	 	 if(i==j)
    	 	    {
				 
				 continue;
			}
    	 	for(int k=0;k<a;k++)
    	 	{   if(i==k||j==k)
    	         {
				 continue;
				 }
    	 	    c=num[i]+num[j]+num[k];
    	 		if(c<=u&&c>=y)
    	 		{
    	 			y=c;
				 }
    	 		
				
    	 	}
    	 	
    	 	
        }
    	
    }
    printf("%d",y);
}