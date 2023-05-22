#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

int K, N;
std::vector<int> lan;

bool isPossible(int length) {
    int count = 0;

    for (int i = 0; i < K; i++) {
        count += lan[i] / length;
    }
    
    if (count >= N) {
        return true;
    }
    else {
        return false;
    }
}

void ParametricSearch() {
    sort(lan.begin(), lan.end());

    unsigned int left = 1, right = lan[lan.size() -1];
    unsigned int result = 0;

    while(left <= right) {
        unsigned int mid = (left + right) / 2;

        if (isPossible(mid)) {
            result = std::max(result, mid);
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    std::cout << result;
}

int main() {

    std::cin >> K >> N;
    lan.assign(K, 0);

    for(int i = 0; i < K; ++i) {
        std::cin >> lan[i];
    }

    ParametricSearch();

    return 0;
}
