#include <iostream>
#include <vector>
#include <algorithm>

int main(void) {
    // Sync off
    std::ios_base::sync_with_stdio(false);

    // Declare variables
	std::vector<size_t> digitVector;
	size_t numberOfInputDigits;

    // Input
    std::cin >> numberOfInputDigits;
	for (size_t i = 0; i < numberOfInputDigits; i++) {
		size_t inputDigit;
		std::cin >> inputDigit;
		digitVector.push_back(inputDigit);
	}

    // Sorting
	sort(digitVector.begin(), digitVector.end());

	size_t duplicateCount = 0;
	for (size_t i = 0; i < digitVector.size() - 1; i++) {
		if (digitVector[i + 1] == digitVector[i] + 1) {
            // Swap
			auto iter = lower_bound(digitVector.begin() + i, digitVector.end(), digitVector[i] + 2);
			if (iter != digitVector.end()) {
                std::swap(*iter, digitVector[i + 1]);
            } else {
				auto upperBound = upper_bound(digitVector.begin() + i + 1, digitVector.end(), digitVector[i]);
				auto lowerBound = lower_bound(digitVector.begin() + i - duplicateCount, digitVector.end(), digitVector[i]);
                
				while (upperBound != digitVector.end()) {
					std::swap(*lowerBound, *upperBound);
					lowerBound++; upperBound++;
				}
			}
            // Return duplicateCount to zero
			duplicateCount = 0;
		} else if (digitVector[i + 1] == digitVector[i]) {
            duplicateCount++;    // Counting
        }
	}

    // Output
    for(size_t i = 0; i < digitVector.size(); i++) {
        std::cout << digitVector[i] << " ";
    }

    return 0;
}
