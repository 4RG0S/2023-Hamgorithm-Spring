#include <iostream>
#include <queue>

int main(void) {
    // Sync off
	std::ios_base::sync_with_stdio(false);
	
    // Declare variables
	std::queue<size_t> cardQueue;
	int numberOfCard;
	
    // Input
	std::cin >> numberOfCard;
	
    // Push
	for(ssize_t i = 1; i <= numberOfCard; i++) {
		cardQueue.push(i);
	}
	
	// loop
	while(cardQueue.size() > 1) {
		cardQueue.pop();
		cardQueue.push(cardQueue.front());
		cardQueue.pop();	
	}

    // Output
	std::cout << cardQueue.front() << std::endl;
	
	return 0;
}
