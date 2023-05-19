#include <iostream>

// Function for calculate number of envelope
ssize_t calculateNumberOfEnvelope(ssize_t amount) {
    
    // amount >= 3 && amount <= 5000
    if(amount == 4 || amount == 7) {
        return -1;
    }
    
    else {
        ssize_t result, rest;

        result = amount / 5;
        rest = amount % 5;

        switch(rest) {
            case 0:     // 5, 10, 15, ...
                break;
            case 1:     // 6, 11, 16, ...
            case 3:     // 8, 13, 18, ...
                result++;
                break;
            case 2:     // 12, 17, 22, ...
            case 4:     // 9, 14, 19, ...
                result += 2;
                break;
        }
        
        return result;
    }

}

int main(void) {
    // Sync off
    std::ios_base::sync_with_stdio(false);
    
    // Declare variables
    ssize_t numberOfEnvelope;
    ssize_t amountOfNeed;

    // Input
    std::cin >> amountOfNeed;

    numberOfEnvelope = calculateNumberOfEnvelope(amountOfNeed);

    // Output
    std::cout << numberOfEnvelope << std::endl;

    return 0;
}
