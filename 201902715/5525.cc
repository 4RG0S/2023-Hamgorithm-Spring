#include <iostream>
#include <string>
#include <vector>

int main() {
    int N, M;
    std::string str;

    std::cin >> N >> M >> str;

    std::vector<int> IOIO_pattern_length_list;

    char cur = 'I';
    char next = 'O';
    char temp;
    int temp_len = 0;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == cur) {
            temp = cur;
            cur = next;
            next = temp;
            temp_len++;
            continue;
        } else {
            if (str[i] == 'I') {
                cur = 'O';
                next = 'I';
                if (temp_len == 0) {
                    temp_len = 1;
                } else {
                    IOIO_pattern_length_list.push_back(temp_len);
                    temp_len = 1;
                }
            } else {
                cur = 'I';
                next = 'O';
                if (temp_len != 0) {
                    IOIO_pattern_length_list.push_back(temp_len);
                    temp_len = 0;
                }
            }
        }
    }
    if (temp_len != 0) IOIO_pattern_length_list.push_back(temp_len);

    int result = 0;
    for (int i = 0; i < IOIO_pattern_length_list.size(); i++) {
        int pattern_length = IOIO_pattern_length_list.at(i);
        if (pattern_length % 2 == 0) pattern_length -= 1;

        int diff = (pattern_length - (2 * N + 1)) / 2;

        if (diff < 0) continue;

        result += diff + 1;
    }

    std::cout << result << std::endl;

    return 0;
}
