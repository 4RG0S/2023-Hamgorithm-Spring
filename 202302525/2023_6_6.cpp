#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() {
    int n, min, max;
    cin >> n;

    int num[n];

    for (int i = 0; i < n; i++){
        cin >> num[i];

        if (i == 0){
            min = num[i];
            max = num[i];
        }

        else{
            if(num[i] > max){
                max = num[i];
            }

            else if(num[i] < min){
                min = num[i];
            }
        }
    }

    cout << min << " " << max << "\n";
}