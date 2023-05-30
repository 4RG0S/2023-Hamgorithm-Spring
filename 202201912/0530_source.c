#include <stdio.h>

int arr[10];

int main() {
    int n, k, ans = 0;
    int sum = 0;

    scanf("%d %d", &n, &k);

    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    for (int i = n - 1; i >= 1; i--) {
        int cnt = (k - sum) / arr[i];

        ans += cnt;
        sum += cnt * arr[i];
    }

    ans += k - sum;

    printf("%d", ans);

    return 0;
}