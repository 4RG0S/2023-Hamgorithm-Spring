#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	char name[21];
	int num;
}Pocketmon;

Pocketmon pocket[100001];
Pocketmon pocket_word[100001];

int compare(const void* a, const void* b)
{
	Pocketmon* ptA = (Pocketmon*)a;
	Pocketmon* ptB = (Pocketmon*)b;
	return strcmp(ptA->name, ptB->name);
}

int binary(Pocketmon* pocket, char* string, int start, int end) {
	while (start <= end) {
		int mid = (start + end) / 2;
		int cmp = strcmp(pocket[mid].name, string);

		if (cmp > 0) end = mid - 1;
		else if (cmp < 0)  start = mid + 1;
		else
			return mid;
	}
	return 0;
}

int main() {
	int N, M, value;
	scanf("%d %d", &N, &M);
	char string[21];

	for (int i = 0; i < N; i++) {
		scanf("%s", pocket[i].name);
		strcpy(pocket_word[i].name, pocket[i].name);
		pocket[i].num = pocket_word[i].num = i + 1;
	}
	qsort(pocket_word, N, sizeof(Pocketmon), compare);

	for (int i = 0; i < M; i++) {
		scanf("%s", string);
		if (string[0] <= 57) printf("%s\n", pocket[atoi(string) - 1].name);
		else {
			printf("%d\n", pocket_word[binary(pocket_word, string, 0, N - 1)].num);
		}

	}
}