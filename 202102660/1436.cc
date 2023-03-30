#include <iostream>
#include <string>

int main() {
	int N, count, title;
	std::cin >> N;
	// 0: 666, 1: 1666, ..., (6: 6660, 6+9: 6669), 6+10: 7666, 6+11: 8666, 9666, 10666, 11666, ... (16660, 
	// 그냥 666부터 1씩 더해가면서 "666"인 문자열이 포함된다면 count +1하자
	for (int i = 666; ; i++) {
		std::string str;
		str = std::to_string(i);
		if (str.find("666") != std::string::npos) {
			count++;
		}
		if (count == N) {
			title = i;
			break;
		}
	}

	std::cout << title;

	return 0;
}