#include <stdio.h>
int main()
{
	int x,y=0;
	while(1)
	{
		scanf("%d %d",&x,&y);
	    if((x==0)||(y==0))
		{
			break;
		}
		
		else if((x%y==0)||(y%x==0))
		{
			if((x%y==0))
			{
				printf("multiple\n");
			}
			else if((y%x==0))
			{
				printf("factor\n");
			}
		}
		
		
	
		else 
		{
			printf("neither\n");
		}
	}
	
	
}