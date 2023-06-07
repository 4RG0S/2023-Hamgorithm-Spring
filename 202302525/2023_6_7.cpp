#include <iostream>
#include <string>

using namespace std;

int main() {
    int num, cnt;
    string str, result;
    char k;

    cin >> num;

    for(int i = 0; i < num; i++){
        result = "";
        cin >> cnt >> str;

        int len = str.length();

        for(int j = 0; j < len; j++){
            k = str[j];
            
            result.append(cnt, k);
        }

        cout << result << "\n";
    }
}