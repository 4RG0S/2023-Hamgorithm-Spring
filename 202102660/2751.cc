#include <iostream>
#include <algorithm>

#define MAXLEN 1000000

using namespace std;

int arr[MAXLEN];

int main() {
    int N;
    cin >> N;

    for (int i=0; i <N; i++) {
        cin >> arr[i];
    }

    sort(arr, arr+N);

    for (int i=0; i <N; i++) {
        cout << arr[i] << '\n';
    }
    
}