#include <iostream>
#include <stack>

std::stack<int> num;

int main() {
    int N;
    int temp;
    std::scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        std::scanf("%d", &temp);
        if (temp != 0) {
            num.push(temp);
        }
        else {
            num.pop();
        }
    }
    int sum = 0;
    while(!num.empty()) {
        sum += num.top();
        num.pop();
    }
    std::printf("%d", sum);
}
