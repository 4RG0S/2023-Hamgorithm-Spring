#include <iostream>
#include <vector>
#include <algorithm>

// Function return possibility of cutting with our need
bool isPossible(std::vector <ssize_t> &vec, ssize_t lengthOfNeed, ssize_t height) {
    ssize_t taken = 0;

    for(ssize_t i = 0 ; i < vec.size(); i++) {
        if(vec[i] >= height) {
            taken += (vec[i] - height);
        }

        if(taken >= lengthOfNeed) {
            return true;
        }
    }
    return false;
}

// Function for find max height value setting to cutter
ssize_t findMaxHeightOfCutter(std::vector <ssize_t> &vec, ssize_t lengthOfNeed) {
    ssize_t left = 0, right = 1000000000;
    ssize_t mid, result;
    while (left <= right) {
        mid = (left + right) / 2;
        if (isPossible(vec, lengthOfNeed, mid)) {
            result = mid;
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    return result;
}

bool compare(ssize_t i, ssize_t j) {
    return j < i;
}

int main(void) {
    // Sync off
    std::ios_base::sync_with_stdio(false);

    // Declare variable
    ssize_t numberOfTrees;
    ssize_t lengthOfNeed;
    std::vector <ssize_t> treeVector;

    // Input
    std::cin >> numberOfTrees >> lengthOfNeed;
    for(ssize_t i = 0; i < numberOfTrees; i++) {
        ssize_t lengthOfTree;
        std::cin >> lengthOfTree;
        treeVector.push_back(lengthOfTree); 
    }

    // Desc sorting
    sort(treeVector.begin(), treeVector.end(), compare);

    // Calculate result
    ssize_t result = findMaxHeightOfCutter(treeVector, lengthOfNeed);

    // Output
    std::cout << result << std::endl;

    return 0;
}
