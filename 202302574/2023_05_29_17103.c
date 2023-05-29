#include<stdio.h>
#define to 1000000
int main() {
    int N, cnt, num, i, j;
    int arr[1000000] = { 0, };

    //1. 배열 생성 후 각각 1로 초기화
    for (i = 2; i <= to; i++) {
        arr[i] = 1;
    }
    //2. i가 소수일 때만, i의 배수(자기 자신은 제외)를 지워나가는 방식
    for (i = 2; i <= to; i++) {
        if (arr[i] == 0) continue;
        //i가 소수가 아닐 때, continue
        //즉, i가 소수일 때만, 이하의 명령문 실행
        for (j = 2 * i; j <= to; j += i) {
            arr[j] = 0;
        }
    }
    scanf("%d", &num);
    for (int i = 0; i < num; i++) {
        cnt = 0;
        scanf("%d", &N);
        for (int j = 1; j <= N / 2; j++) {
            cnt += arr[j] && arr[N - j];
        }
        printf("%d\n", cnt);
    }
}