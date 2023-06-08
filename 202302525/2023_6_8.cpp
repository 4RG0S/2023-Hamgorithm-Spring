#include <iostream>
#include <string>

using namespace std;

int main() {
    string str;
    string result;
    int alpha[26] = {0, };
    int high = 0;

    cin >> str;


    for (int i = 0; i < str.length(); i++){
        if (str[i] >= 'a' && str[i] <= 'z'){
            str[i] -= 32;
        }

        alpha[str[i]-65] += 1;

        if (alpha[str[i]-65] > high){
            high = alpha[str[i]-65];
            result = str[i];
        }

        else if (alpha[str[i]-65] == high){
            result = "?";
        } 
    }

    cout << result << "\n";
}