// 23.07.10
// BOJ 1806
// 투 포인터

#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int arr[100000] = { 0, };
    int n, s;
    cin >> n >> s;

    for (int i = 0; i < n; i++)
        cin >> arr[i];

    int start = 0, end = 0, partsum = 0; //두 포인터, 부분합
    int minlen = 100001; //길이 초기값
    while (end <= n) {
        if (partsum < s) { //부분합이 s보다 작으므로 end를 증가시킴
            partsum += arr[end];
            end++;
        }
        else if (partsum >= s) { 
            partsum -= arr[start];
            start++;
            minlen = min(end - start + 1, minlen);
        }
    }

    if (minlen == 100001)
        cout << "0";
    else
        cout << minlen;

    return 0;
}