#include <iostream>

using namespace std;
#define MAX 1000001
int arr[MAX]{0,};
int main() {
    int N, M;

    cin >> N >> M;

// 루트 m까지의 배수 지우기.
    for (int i=2; i<M+1; i++) {
        arr[i] = i;
    }
    
    for (int j = 2; j*j<= M; j++) {
        if (arr[j] == 0) {
            continue;
        }
        for (int i = j*j; i < M+1; i+=j) {
            
            arr[i] = 0;           
        }
        
    }
    
    for (int j = N; j < M+1; j++) {
        if (arr[j] != 0) {
            cout << arr[j] << '\n';
        }
    }

    return 0;
}
