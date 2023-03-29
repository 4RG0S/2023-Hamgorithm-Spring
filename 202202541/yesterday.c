#include <stdio.h>
#include <stdio.h>
#include <string.h>
int main()
{
	int b=0;
	scanf("%d",&b);
    int count =b;
    int count1=0;
    int k=0;
	for( k=0;k<b;k++)
	{
		char a[101]	;
		scanf("%s",a);
        int len=strlen(a);
        count1=2000;
        for(int ch=0;ch<(len-1);ch++)
        {
		
        for(int l=ch+1;l<len;l++)
		{
		if(a[ch]==a[l])
		{
			if(a[ch]!=a[l-1])
			{
				count--;
				count1=count;
				
				break;
			}
			
		
		}
     	}
        if(count1==count)
        {break;
		}
		 
		}    
		
	}
	
	printf("%d",count);
	
}