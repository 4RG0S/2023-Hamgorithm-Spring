// 23.08.20
// BOJ 9375
// 해시를 사용한 집합과 맵

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        map<string, int> clothes; //key:의상 종류, value:종류 key에 대한 옷의 개수
        while (n--) {
            string s1, s2; //이름, 종류
            cin >> s1 >> s2;

            if (clothes.find(s2) != clothes.end()) //종류가 존재할 때 개수++
                clothes[s2]++;

            else //존재 하지 않으면 insert
                clothes.insert({ s2, 1 }); 
        }

        int sum = 1;
        for (auto iter = clothes.begin(); iter != clothes.end(); iter++) {//key, value 탐색
            sum *= iter->second + 1;
        }
        cout << sum - 1 << '\n'; //경우의 수: 모든 key에 대한 value 곱 - 1
    }

    return 0;
}