#include <iostream>
#include <vector>

int isPrime(std::vector<int> vec) {
    int cnt = 0;
    int result = 0;
    for(int i = 0; i < vec.size(); i++) {
        for(int j = 1; j <= vec[i]; j++) {
            if(vec[i]%j==0) cnt++;
        }
        if(cnt == 2) result++;
        cnt = 0;
    }
    return result;
}

int main() {
    int N;
    std::cin >> N;
    std::vector<int> prime;

    for(int i = 0; i < N; i++) {
        int num;
        std::cin >> num;
        prime.push_back(num);
    }
    std::cout << isPrime(prime) << std::endl;

    return 0;
}
