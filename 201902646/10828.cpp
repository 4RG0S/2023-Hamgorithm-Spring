#include <iostream>
#include <string>

struct stack {
    int arr[10001];
    int cnt;
    void init() {
        cnt = 0;
    }

    void push(int X) {
        arr[cnt] = X;
        cnt++;
    }

    int pop() {
        if (cnt == 0) return -1;
        int temp = arr[cnt-1];
        cnt--;
        return temp;
    }

    int size() {
        return cnt;
    }

    bool empty() {
        if (cnt == 0) return 1;
        else return 0;
    }

    int top() {
        if (cnt == 0) return -1;
        return arr[cnt-1];
    }
};

int main() {
    int N;
    std::cin >> N;
    stack st;
    st.init();

    while(N) {
        std::string cmd;
        int num;
        std::cin >> cmd;
        if(cmd == "push") {
            std::cin >> num;
            st.push(num);
        }
        if(cmd == "pop") {
            std::cout << st.pop() << std::endl;
        }
        if(cmd == "size") {
            std::cout << st.size() << std::endl;
        }
        if(cmd == "empty") {
            std::cout << st.empty() << std::endl;
        }
        if(cmd == "top") {
            std::cout << st.top() << std::endl;
        }
        N--;
    }
}
