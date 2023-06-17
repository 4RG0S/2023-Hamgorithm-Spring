#include <iostream>
#include <deque>
#include <string>

int main() {

	std::deque<int> deq;
	std::string cmd;

	int N;
	std::cin >> N;
	int X;

	for (int i = 0; i < N; ++i) {
		std::cin >> cmd;
		if (cmd == "push_front") {
			std::cin >> X;
			deq.push_front(X);
		}
		else if (cmd == "push_back") {
			std::cin >> X;
			deq.push_back(X);
		}
		else if (cmd == "pop_front") {
			if (deq.empty()) {
				std::cout << -1 << std::endl;
			}
			else {
				std::cout << deq.front() << std::endl;
				deq.pop_front();
			}
		}
		else if (cmd == "pop_back") {
			if (deq.empty()) {
				std::cout << -1 << std::endl;
			}
			else {
				std::cout << deq.back() << std::endl;
				deq.pop_back();
			}
		}
		else if (cmd == "size") {
			std::cout << deq.size() << std::endl;
		}
		else if (cmd == "empty") {
			if (deq.empty()) {
				std::cout << 1 << std::endl;
			}
			else {
				std::cout << 0 << std::endl;
			}
		}
		else if (cmd == "front") {
			if (deq.empty()) {
				std::cout << -1 << std::endl;
			}
			else {
				std::cout << deq.front() << std::endl;
			}
		}
		else if (cmd == "back") {
			if (deq.empty()) {
				std::cout << -1 << std::endl;
			}
			else {
				std::cout << deq.back() << std::endl;
			}
		}
	}

	return 0;
}
