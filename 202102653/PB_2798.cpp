#include <iostream>
#include <vector>

int main(void) {
    // Sync off
    std::ios_base::sync_with_stdio(false);

    // Declare variable
    ssize_t numberOfCard;
    ssize_t maxOfPossibleSum;
    ssize_t sumOfCards;
    ssize_t max = 0;
    std::vector <ssize_t> cardVector;

    // Input
    std::cin >> numberOfCard >> maxOfPossibleSum;

    for(ssize_t i = 0; i < numberOfCard; i++) {
        ssize_t cardNumber;
        std::cin >> cardNumber;
        cardVector.push_back(cardNumber);
    }

    // loop without overlapping
    for(ssize_t i = 0; i < numberOfCard; i++) {
        for(ssize_t j = i + 1; j < numberOfCard; j++) {
            for(ssize_t k = j + 1; k < numberOfCard; k++) {
                sumOfCards = cardVector[i] + cardVector[j] + cardVector[k];
                if(sumOfCards > max && sumOfCards <= maxOfPossibleSum) {
                    max = sumOfCards;
                }
            }
        }
    }

    // Output
    std::cout << max << std::endl;

    return 0;   
}
