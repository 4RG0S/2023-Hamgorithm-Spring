#include <iostream>
#include <vector>

using namespace std;

vector<pair<int, int>> stairs;
vector<int> result(301, 0);
pair<int, int> calc(int num) {
    // 1전, 2전의 최대값 비교해서 더 큰걸 선택 후, 현재 가중치 더함.
    // 위에서 1전이 선택됐다면, 1전의 flag 숫자를 1 더한 값을 현재 flag로함. 
    // 숫자가 2이라면 2를 선택해야함.

    if (num <= 1) {
        return stairs[num];
    }
    // pair<int, int> one, two;
    // one = calc(num-1);
    // two = calc(num-2);
    
    // result[num] = (max(two.first, one.first) + stairs[num].first);
    int f, s;
    if (num == 2) {
        result[num] = stairs[1].first + stairs[2].first;
    }
    if (result[num] != 0) {
        return make_pair(result[num], stairs[num].second);
    }
    f = calc(num-3).first+stairs[num-1].first+stairs[num].first;
    s = calc(num-2).first+stairs[num].first;
    // if (stairs[num-3].second == 1) {
    //     result[num] = f;
    //     stairs[num].second = 1;

    // }
    // else 
    result[num] = max(f, s);
    // if (one.first >= two.first) {
    //     stairs[num].second = stairs[num-1].second+1;
    //     if (stairs[num].second == 2) {
    //         stairs[num].second = 0;
    //         result[num] = (two.first + stairs[num].first);
    //     }
    // }
    // else {
    //         stairs[num].second = 0;
    // }
    return make_pair(result[num], stairs[num].second);
      
}

int main() {
    int n, tmp;
    cin >> n;
    stairs.push_back(make_pair(0, 0));
    for (int i=0; i < n; i++) {
        cin >> tmp;
        stairs.push_back(make_pair(tmp, 0));
    }
    cout << calc(n).first << '\n';
    return 0;
}