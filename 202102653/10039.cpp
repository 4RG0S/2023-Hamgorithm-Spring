#include <iostream>
#include <vector>

int main(void) {
    // Sync off
    std::ios_base::sync_with_stdio(false);

    // Declare variable
    std::vector <unsigned int> scoreVector;
    unsigned int score, sum = 0, avg = 0;
    
    for(int i = 0; i < 5; i++) {
        std::cin >> score;
        if(score % 5 != 0) {
            std::cout << "[Error] Invalid score" << std::endl;
            std::exit(1);
        } else if(score < 40) {
            scoreVector.push_back(40);
        } else {
            scoreVector.push_back(score);
        }
    }

    for(unsigned int score : scoreVector) {
        sum += score;
    }

    avg = sum / 5;

    std::cout << avg << std::endl;

    return 0;
}
