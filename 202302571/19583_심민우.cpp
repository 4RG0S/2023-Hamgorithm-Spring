// 23.08.20
// BOJ 19583
// 해시를 사용한 집합과 맵

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

int timetoint(string s) { //ex: (string)23:40 -> (int)2340
    return (s[0] - '0') * 1000 + (s[1] - '0') * 100 + (s[3] - '0') * 10 + (s[4] - '0');
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    string s, e, q;
    cin >> s >> e >> q;

    int S = timetoint(s), E = timetoint(e), Q = timetoint(q);
    
    map<string, bool> enter; //입장한 사람 목록
    map<string, bool> leave; //퇴장한 사람 목록
    string time, name;

    while (cin >> time >> name) { //eof 처리
        int t = timetoint(time);

        if (t <= S) //입장 목록 추가
            enter.insert({ name, true });

        else if (t >= E && t <= Q) //퇴장 목록 추가
            leave.insert({ name, true });
    }

    int countattend = 0;
    //퇴장한 사람 탐색
    for (auto iter = leave.begin(); iter != leave.end(); iter++) {
        if (enter.find(iter->first) != enter.end()) //퇴장한 사람중에 입장한 사람 목록에 이름이 있으면 출석 확인
            countattend++;
    }
    cout << countattend;

    return 0;
}