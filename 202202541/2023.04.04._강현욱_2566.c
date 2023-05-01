#include <stdio.h>
int main()
{
	int num[9][9];
	for(int q=0;q<9;q++)
	{
		for(int w=0;w<9;w++)
		{
			scanf("%d",&num[q][w]);
			
		}
	}
	int max=num[0][0]; int z,x=0;
	for(int m=0;m<9;m++)
	{
		for(int n=0;n<9;n++)
		{
		   if(max<=num[m][n])
		   {
		   	max=num[m][n]; z=m;x=n;
		   }
		}
	}
   printf("%d\n%d %d",max,z+1,x+1)
	;
	
	
	
	
}