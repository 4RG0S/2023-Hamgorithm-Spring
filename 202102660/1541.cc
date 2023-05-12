// 앞에서부터 검사하면서 +니까 다 더해서 vector에 넣기. - 나오면 
// 다음 - 나올때까지 +해서 vector에 넣기.

#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int main() {
    string inp, strtmp="";
    cin >> inp;
    int tmp=0;
    bool isMin = false;
    vector<int> vec;
    vector<string> strvec;
    // vector<string> 
    // +, - 가 나올때 까지 하나의 string str에 계속 붙이기
    // 기호 나오면 vector에 푸시, 기호도 푸시
    for(int i=0; i < inp.length(); i++) {
        char s = inp.at(i);
        if (s == '+' || s == '-') {
            strvec.push_back(strtmp);
            strtmp = "";
            strvec.push_back(string(1, s));
        } else {
            strtmp += s;
            // cout << "strtmp: " << strtmp << '\n';
        }
    }
    strvec.push_back(strtmp);
    for (string s: strvec) {
        // cout << s << '\n';
        if (s.compare("+") == 0) {
        
        } else if (s.compare("-") == 0) {
            if (isMin) {
                vec.push_back(-tmp);
            }
            else vec.push_back(tmp);
            tmp = 0;
            isMin = true;
        } else {
            // 숫자라면
            tmp += stoi(s);
            // cout << "tmp: " << tmp << '\n';
            
        }
    }

    if (isMin) vec.push_back(-tmp);
    else vec.push_back(tmp);
    // for (int i : vec) {
    //     cout << i << '\n';
    // }

    tmp = 0;

    for (int num : vec) {
        tmp += num;
    }

    cout << tmp << '\n';

    return 0;
}
