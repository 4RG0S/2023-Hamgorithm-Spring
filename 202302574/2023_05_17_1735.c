#include<stdio.h>
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
void simplify(int *a, int *b) {
    int temp = gcd(*a, *b);
    *a /= temp;
    *b /= temp;
    return;
}
int main() {
    int numA, denA, numB, denB;
    int denLcd, tempSum;
    scanf("%d%d%d%d", &numA, &denA, &numB, &denB);

    simplify(&numA, &denA); simplify(&numB, &denB);

    denLcd = denA * denB / gcd(denA, denB);
    tempSum = numA * (denLcd / denA) + numB * (denLcd / denB);

    simplify(&tempSum, &denLcd);
    printf("%d %d", tempSum, denLcd);

}
