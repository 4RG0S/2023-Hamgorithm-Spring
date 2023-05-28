#include <iostream>
#include <vector>
#include <queue>

void next(std::queue <unsigned int> &queue) {
    queue.push(queue.front());
    queue.pop();
}

void printPermutation(std::vector <unsigned int> &vec) {
    std::cout << '<';
    for(unsigned int element : vec) {
        if(element != vec.back()) {
            std::cout << element << ", ";
        } else {
            std::cout << element << '>' << std::endl;
        }
    }
}

int main(void) {
    // Sync off
    std::ios_base::sync_with_stdio(false);

    // Declare variables
    unsigned int sizeOfQueue, order;
    std::queue <unsigned int> numberQueue;
    std::vector <unsigned int> resultVector;

    // Input
    std::cin >> sizeOfQueue >> order;

    for(unsigned int i = 1; i <= sizeOfQueue; i++) {
        numberQueue.push(i);
    }

    while(resultVector.size() != sizeOfQueue) {
        for(unsigned int i = 0; i < order - 1; i++) {
            next(numberQueue);
        }
        resultVector.push_back(numberQueue.front());
        numberQueue.pop();
    }

    // Output
    printPermutation(resultVector);

    return 0;
}