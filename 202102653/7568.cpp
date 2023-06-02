#include <iostream>
#include <vector>

int main(void) {
    // Declare variables
    ssize_t numberOfPeople, rank = 1;
    std::pair <ssize_t, ssize_t> arr[50];
    std::vector <ssize_t> resultVector;

    // Input
    std::cin >> numberOfPeople;

    for(ssize_t i = 0; i < numberOfPeople; i++) {
        std::cin >> arr[i].first >> arr[i].second;
    }
        
    for(ssize_t i = 0; i < numberOfPeople; i++) {
        for(ssize_t j = 0; j < numberOfPeople; j++) {
            if(arr[i].first < arr[j].first && arr[i].second < arr[j].second) {
                rank++;
            }
        }
        resultVector.push_back(rank);
        rank = 1;
    }

    // Output
    for(ssize_t result : resultVector) {
        std::cout << result << ' ';
    }

    std::cout << '\n';

    return 0;
}