#include <stdio.h>

int main(void)
{
    int a_divisor = 0; 
    long long max = 0, min = 1000001; 

    int num_of_divisors; 
    scanf("%d", &num_of_divisors);

    for (int i = 0; i < num_of_divisors; i++) {  
        scanf("%d", &a_divisor);

        if (a_divisor > max)                
            max = a_divisor;
        if (a_divisor < min)
            min = a_divisor;
    }

    printf("%lld\n", max * min);

    return 0;
}