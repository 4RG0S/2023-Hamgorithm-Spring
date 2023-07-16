// 23.07.16
// BOJ 2470
// 투 포인터

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> solution(n);
    for (int i = 0; i < n; i++)
        cin >> solution[i];
    sort(solution.begin(), solution.end()); //용액들을 오름차순 정렬

    int start = 0, end = n - 1;//두 포인터, 처음과 끝에서 시작
    int minidx[3] = { 2000000000, 0, 0 }; //두 용액의 합, 용액 1, 용액 2 

    while (start < end) { 
        if (abs(solution[end] + solution[start]) < minidx[0]) { //0에 가까운 것을 찾기 위해 절댓값 사용
            minidx[0] = abs(solution[end] + solution[start]);
            minidx[1] = solution[start];
            minidx[2] = solution[end];
        }

        if (solution[end] + solution[start] >= 0) //더한 값이 0보다 크다면 end를 감소시켜 0에 가깝게 한다
            end--;
        else //0보다 작다면 ...
            start++;
    }

    cout << minidx[1] << ' ' << minidx[2];

    return 0;
}