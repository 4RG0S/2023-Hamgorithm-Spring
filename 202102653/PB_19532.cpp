#include <iostream>

int findXvalue(int a, int b, int c, int d, int e, int f) {
    return (c * e - b * f) / (a * e - b * d);   
}

int findYvalue(int a, int b, int c, int d, int e, int f) {
    return (a * f - c * d) / (a * e - b * d);   
}

int main(void) {

    // Sync off

    std::ios_base::sync_with_stdio(false);

    // Declare variable

    int a, b, c, d, e, f;

    // Input

    std::cin >> a >> b >> c >> d >> e >> f;

    // Output

    std::cout << findXvalue(a, b, c, d, e, f) << ' ' << findYvalue(a, b, c, d, e, f) << std::endl;

    return 0;   

}
