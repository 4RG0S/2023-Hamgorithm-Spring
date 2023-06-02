#include <iostream>
#include <vector>

int main(void) {
    // Sync off
    std::ios_base::sync_with_stdio(false);

    // Input
    ssize_t numberOfTestcases;
    ssize_t height, width, order;
    std::vector <ssize_t> resultVector;

    std::cin >> numberOfTestcases;

    for(ssize_t i = 0; i < numberOfTestcases; i++) {
        std::cin >> height >> width >> order;
        ssize_t floor = order % height;
        ssize_t room = (order / height) + 1;

        if(floor == 0) {
            floor = height;
            room--;
        }

        resultVector.push_back(floor * 100 + room);
    }

    // Output
    for(ssize_t i = 0; i < numberOfTestcases; i++) {
        std::cout << resultVector[i] << '\n';
    }
    
    return 0;
}