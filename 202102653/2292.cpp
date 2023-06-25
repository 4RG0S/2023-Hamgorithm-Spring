#include <iostream>

int main(void) {
    // Sync off
    std::ios_base::sync_with_stdio(false);

    // Declare variables
	ssize_t inputNumber;
	ssize_t resultNumber = 1;
	ssize_t endNumber = 1;
	ssize_t addNumber = 6;

    // Input
    std::cin >> inputNumber;

	while(true) {
        // Break condition
		if (inputNumber <= endNumber) {
            break;
        }

		endNumber += addNumber;
		addNumber += 6;
		++resultNumber;
	}

    // Output
    std::cout << resultNumber << std::endl;

	return 0;
}
