#include <stdio.h>

void swap(int* n1, int* n2) {
	int tmp = *n1;
	*n1 = *n2;
	*n2 = tmp;
}

void add_to_heap(int* heap, int i, int tip) {
	int pi = i / 2;

	heap[i] = tip;

	while (pi < i && heap[pi] > heap[i]) {
		swap(&heap[pi], &heap[i]);
		i = pi;
		pi = pi / 2;
	}
}

void make_heap(int* heap, int dirty_index, int count) {
	int p1 = dirty_index * 2 + 1;
	int p2 = dirty_index * 2 + 2;
	if (p1 >= count)
		return;

	int p = p2 >= count ? p1 : (heap[p1] < heap[p2] ? p1 : p2);

	if (heap[p] < heap[dirty_index]) {
		swap(&heap[p], &heap[dirty_index]);
		make_heap(heap, p, count);
	}

}

void sort_heap(int* heap, int count) {
	int i, pi;
	while (--count >= 0) {
		swap(heap, &heap[count]);

		make_heap(heap, 0, count);
	}
}

int main() {
	long sum = 0;
	int heap[100000] = { 0 };

	int count, tip;
	scanf("%d", &count);

	for (int i = 0; i < count; i++) {
		scanf("%d", &tip);
		add_to_heap(heap, i, tip);
	}

	sort_heap(heap, count);

	int t;
	for (int i = 0; i < count; i++) {
		t = heap[i] - i;
		if (t > 0)
			sum += t;
		else
			break;
	}

	printf("%ld", sum);

	return 0;
}