#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int cal(int a) {
    int cnt = 99;

    if (a == 1000){
        a--;
    }

    for (int i = 100; i <= a; i ++){
        if ((i / 100 - ((i / 10) % 10)) == ((i / 10) % 10 - i % 10)) {
            cnt++;
        }
    }

    return cnt;
}

int main() {
    int num;
    cin >> num;

    if (num < 100){
        cout << num;
    }

    else {
        int result = cal(num);

        cout << result;
    }
}