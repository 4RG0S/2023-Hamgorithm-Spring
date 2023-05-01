#include <iostream>
#include <unordered_map>

#define MAXLENGHT 10000000

using namespace std;

void merge(int, int);
void mergeSort(int, int);
void binarySearch(int, int, int);
// map<int, int> m;
// map<int, int>::iterator iter;
unordered_map<int, int> m;

int card1[MAXLENGHT];
int card2[MAXLENGHT];
int card_sorted[MAXLENGHT];
int ccount[MAXLENGHT];


int main() {
    int N, M, K;
    cin >> N;
    
    for (int i = 0; i < N; i++) {
        // cin >> card1[i];
        cin >> K;
        m[K] += 1;
        card1[i] = K;
    }
    
    cin >> M;

    for (int i = 0; i < M; i++) {
        cin >> card2[i];
    }
    

    // 머지소트 ->  앞으론 sort()함수 쓰깅ㅋ
    mergeSort(0, N-1);
    // 이진탐색
    for (int i = 0; i < M; i++) {
        binarySearch(0, N-1, i);
    }
    for (int i=0; i < M; i++) {
        cout << ccount[i] << ' ';
    }

}

void mergeSort(int i, int j) {

    if (i < j) {
        int mid = (i+j)/2;
        mergeSort(i, mid);
        mergeSort(mid+1, j);
        merge(i, j);
    }
    
}

void merge(int start, int end) {
    int mid = (start+end) / 2;
    int i = start;
    int j = mid+1;
    int idx = start;
    while (idx <= end) {
        if (i <= mid && j <= end) {
            if (card1[i] < card1[j]) {
                card_sorted[idx] = card1[i];
                i++;
            } else if (card1[i] == card1[j]) {
                card_sorted[idx] = card1[i];
                idx++;
                card_sorted[idx] = card1[j];
                i++;
                j++;

            }
            else {
                card_sorted[idx] = card1[j];
                j++;
            }
            idx++;
            
        } else if (mid < i) {
            // 뒤에껄 싹다 넣어야됨
            for (int k = j; k <=end; k++) {
                card_sorted[idx] = card1[k];
                idx++;
            }
        } else if (j > end) {
            for (int k = i; k <=mid; k++) {
                card_sorted[idx] = card1[k];
                idx++;
            }
        }
    }
    for (int l = start; l < end+1; l++) {
        card1[l] = card_sorted[l];
    }
}

void binarySearch(int start, int end, int idx) {
    int mid = (start+end)/2;
    if (card2[idx] < card1[mid]) {
        if (start > mid-1) return;
        binarySearch(start, mid-1, idx);
    } else if (card2[idx] > card1[mid]) {
        if (mid+1 > end) return;
        binarySearch(mid+1, end, idx);
    } else {
        ccount[idx] = m[card2[idx]];
    }
}