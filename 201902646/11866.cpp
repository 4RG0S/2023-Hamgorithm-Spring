#include <iostream>
#include <queue>

int main() {
    int N, K;
    std::queue<int> person;
    std::cin >> N >> K;

    for(int i = 1; i <= N; i++) {
        person.push(i);
    }

    std::cout << "<";
    while(!person.empty()) {
        for(int i = 1; i < K; i++) {
            person.push(person.front());
            person.pop();
        }
        std::cout << person.front();
        if (person.size() != 1) std::cout << ", ";
        person.pop();
    }
    std::cout << ">";

}
