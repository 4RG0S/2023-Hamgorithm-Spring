#include <iostream>
#include <string>

struct queue{
    int arr[10001];
    int begin = 0;
    int end = 0;
    
    void init() {
        end = 0;
    }

    void push(int X) {
        arr[end] = X;
        end++;
    }

    int pop() {
        if(end == begin) return -1;
        int temp = arr[begin];
        arr[begin] = 0;
        begin++;
        return temp;
    }

    int size() {
        return end - begin;
    }

    bool empty() {
        if(end == begin) return 1;
        return 0;
    }

    int front() {
        if(end == begin) return -1;
        return arr[begin];
    }

    int back() {
        if(end == begin) return -1;
        return arr[end-1];
    }
};

int main() {
    int N;
    std::cin >> N;
    queue que;
    que.init();

    while(N) {
        std::string cmd;
        int num;
        std::cin >> cmd;

        if(cmd == "push") {
            std::cin >> num;
            que.push(num);
        }

        if(cmd == "pop") {
            std::cout << que.pop() << std::endl;
        }

        if (cmd == "size") {
            std::cout << que.size() << std::endl;
        }

        if (cmd == "empty") {
            std::cout << que.empty() << std::endl;
        }

        if (cmd == "front") {
            std::cout << que.front() << std::endl;
        }

        if (cmd == "back") {
            std::cout << que.back() << std::endl;
        }
        N--;
    }
    return 0;
}
