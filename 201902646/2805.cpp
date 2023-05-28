#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

#define MAX 1000000

int M, N;
long long tree[MAX];

bool isPossible(int len) {
    long long count = 0;
    for (int i = 0; i < M; i++) {
        if (tree[i] < len) {
            continue;
        }
        else {
            count += tree[i] - len;
        }
    }
    
    if (count >= N) {
        return true;
    }
    else {
        return false;
    }
}


int main() {

    std::cin >> M >> N;

    for(int i = 0; i < M; ++i) {
        std::cin >> tree[i];
    }

    long long left = 1, right = *std::max_element(tree, tree+M);
    long long result = 0;

    while(left <= right) {
        long long mid = (left + right) / 2;
        if (isPossible(mid)) {
            result = std::max(result, mid);
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    std::cout << result;

    return 0;
}
