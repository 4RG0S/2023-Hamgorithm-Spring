int main()
{
	int a,b=0;
	scanf("%d %d ",&a,&b);
	int arr1[a][b];
	int arr2[a][b];

	int h=0;
	for(h=0;h<a;h++)
	{
			for(int l=0;l<b;l++)
			{
				scanf("%d",&arr1[h][l]);
				
		    }
	}
	for(h=0;h<a;h++)
	{
			for(int l=0;l<b;l++)
			{
				scanf("%d",&arr2[h][l]);
				
		    }
	}
	for(h=0;h<a;h++)
	{
			for(int l=0;l<b;l++)
			{
				arr1[h][l]=	arr1[h][l]+arr2[h][l];
				printf("%d ",arr1[h][l]);
				
		    }
		    printf("\n");
	}

		
}