#include <iostream>
#include <string>
#include <queue>

std::queue<int> card;

int main() {
    int N;
    std::scanf("%d", &N);
    for(int i = 1; i <= N; i++) {
        card.push(i);
    }
    while(card.size() != 1){
        card.pop();
        card.push(card.front());
        card.pop();
    }
    std::printf("%d", card.front());
    
}
