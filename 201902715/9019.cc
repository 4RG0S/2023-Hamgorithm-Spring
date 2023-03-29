#include <iostream>
#include <queue>
#include <string>

#define MAX_NUM 10000

int D(int num) { return (2 * num) % MAX_NUM; }

int S(int num) { return (num == 0) ? 9999 : (num - 1); }

int L(int num) { return (num % 1000) * 10 + num / 1000; }

int R(int num) { return (num % 10) * 1000 + num / 10; }

int main() {
    int T;
    int A, B;

    std::cin >> T;

    for (int i = 0; i < T; i++) {
        std::queue<std::pair<int, std::string>> bfs;

        std::cin >> A >> B;
        bfs.push({A, ""});
        bool visited[MAX_NUM] = {false};

        while (true) {
            std::pair<int, std::string> pair = bfs.front();

            bfs.pop();
            A = pair.first;
            if (A == B) {
                std::cout << pair.second << std::endl;
                break;
            }

            int temp;

            temp = D(A);
            if (!visited[temp]) {
                visited[temp] = true;
                bfs.push({temp, pair.second + "D"});
            }

            temp = S(A);
            if (!visited[temp]) {
                visited[temp] = true;
                bfs.push({temp, pair.second + "S"});
            }

            temp = L(A);
            if (!visited[temp]) {
                visited[temp] = true;
                bfs.push({temp, pair.second + "L"});
            }

            temp = R(A);
            if (!visited[temp]) {
                visited[temp] = true;
                bfs.push({temp, pair.second + "R"});
            }
        }
    }

    return 0;
}