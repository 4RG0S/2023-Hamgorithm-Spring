#include <stdio.h>

int fibonacci(int n) {
  int table[n];

  table[0] = 1;
  table[1] = 1;

  for (int i = 2; i < n; i++) {
    table[i] = table[i - 1] + table[i - 2];
  }

  return (table[n - 1]);
}

int main(void) {
  int testcase;
  int n;

  scanf("%d", &testcase);
  int arr[testcase];

  for (int i = 0; i < testcase; i++) {
    scanf("%d", &n);

    arr[i] = n;
  }

  for (int i = 0; i < testcase; i++) {
    if (arr[i] == 0) {
      printf("1 0\n");
    } else if (arr[i] == 1) {
      printf("0 1\n");
    } else {
      printf("%d %d\n", fibonacci(arr[i] - 1), fibonacci(arr[i]));
    }
  }

  return 0;
}