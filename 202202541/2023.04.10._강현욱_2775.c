#include <stdio.h>
int main()
{
  int a,b=0; int sum=0;//kÃşlÈ£
  
  int num[15][15];
  for(int k=0;k<=14;k++)
  {
    for(int l=0;l<=14;l++)
    {
        num[l][k]=0;
    }
  }
  for(int d=0;d<=14;d++)
  {
    num[0][d]=d;
  }
   
  for(int k=1;k<=14;k++)
  {
    for(int l=1;l<=14;l++)
    for(int n=1;n<=l;n++)
    {
        num[k][l]+=num[k-1][n];


    }
  }
  int c=0;
  scanf("%d",&c);
  for(int w=0;w<c;w++)
  {
    scanf("%d %d",&a,&b);
    printf("%d\n",num[a][b]);
  }



  }
