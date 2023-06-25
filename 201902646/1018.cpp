#include <iostream>

char chess[51][51];
char wb[8][8] = {
    'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W'
    };
char bw[8][8] = {
    'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B',
	'B','W','B','W','B','W','B','W',
	'W','B','W','B','W','B','W','B'
};
int result = 10000000;

int white(int x, int y) {
    int cnt = 0;
    for(int i = 0; i < 8; i++) {
        for(int j = 0; j < 8; j++) {
            if(chess[x + i][y + j] != wb[i][j]) cnt++;
        }
    }
    return cnt;
}

int black(int x, int y) {
    int cnt = 0;
    for(int i = 0; i < 8; i++) {
        for(int j = 0; j < 8; j++) {
            if(chess[x + i][y + j] != bw[i][j]) cnt++;
        }
    }
    return cnt;
}


int main() {
    int N, M;
    std::cin >> N >> M;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            std::cin >> chess[i][j];
        }
    }
    int W, B;
    for(int i = 0; i <= N-8; i++) {
        for(int j = 0; j <= M-8; j++) {
            W = white(i, j);
            B = black(i, j);
            if (W < B) {
                result = (W < result) ? W : result;
            }
            else {
                result = (B < result) ? B : result;
            }
        }
    }
    std::cout << result << std::endl;
    return 0;
}
