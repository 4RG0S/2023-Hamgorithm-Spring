// 23.08.20
// BOJ 1620
// 해시를 사용한 집합과 맵

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

string pokenum1[100001]; //pokenum1[도감번호] = 포켓몬이름
map<string, int> pokenum2; //pokenum2[포켓몬이름] = 도감번호

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    for (int i = 1; i <= n; i++) {
        string s;
        cin >> s;

        pokenum1[i] = s;
        pokenum2.insert({ s,i });
    }

    while (m--) {
        string s;
        cin >> s;

        if (s[0] >= 'A') { //입력이 문자일때
            cout << pokenum2[s] << '\n';
        }
        else {
            cout << pokenum1[stoi(s)] << '\n';
        }
    }

    return 0;
}