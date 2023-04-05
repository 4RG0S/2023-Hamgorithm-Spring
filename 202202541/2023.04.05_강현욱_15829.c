#include <stdio.h>
#include <string.h>
long long kl=1234567891;
int main()
{
	int ui=0;
	scanf("%d",&ui);
	char word[51];
	scanf("%s",word);
	int len=strlen(word);
	 long long i=1;  long long sum=0;
	 long long hash=0;
	for(int a=0;a<len;a++)
	{
		
		sum=sum+((int)(word[a]-96)*i)%kl; sum%=kl;
		i=i*31; i%=kl;
	}
	printf("%lld",sum%kl);
	
	
}

