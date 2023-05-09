#include <iostream>
#include <string>
int coin[11];

int main() {
    int N, K;
    int count = 0;
    std::cin >> N >> K;

    int num;
    for(int i=1; i<=N; i++) {
        std::cin >> coin[i];
    }
    
    int A = N;

    while(K) {
        while(K - coin[A] >= 0) {
            K -= coin[A];
            count++;
        }
        A--;
    }
    std::cout << count;
}
