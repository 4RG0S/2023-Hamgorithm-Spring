// 23.08.21
// BOJ 14503
// 시뮬레이션

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int map[50][50] = { 0, };
int n, m;

struct Cleaner {
    int y, x; //현재 위치
    int d; //바라보는 방향

    int dy = 0, dx = 0; //이동을 했을 시 위치

    int cleancount = 0; //청소하는 횟수

    bool checkiswall() { //벽인지 확인
        return (dy >= 0) && (dy < n) && (dx >= 0) && (dx < m) && (map[dy][dx] != 1);
    }
    void ifforward() { //앞으로 이동할시 좌표 설정
        if (d == 0) {
            dy = y - 1;
            dx = x;
        }
        if (d == 1) {
            dy = y;
            dx = x + 1;
        }
        if (d == 2) {
            dy = y + 1;
            dx = x;
        }
        if (d == 3) {
            dy = y;
            dx = x - 1;
        }
    }
    void ifbackward() { //뒤로 이동할시 좌표 설정
        if (d == 0) {
            dy = y + 1;
            dx = x;
        }
        if (d == 1) {
            dy = y;
            dx = x - 1;
        }
        if (d == 2) {
            dy = y - 1;
            dx = x;
        }
        if (d == 3) {
            dy = y;
            dx = x + 1;
        }
    }
    void movement() { //이동
        y = dy; x = dx;
    }
    void cleaning() { //현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소
        if (map[y][x] == 0) {
            cleancount++;
            map[y][x] = 2; //청소한 상태
        }
    }
    void rotation() { //반시계 회전
        d--;
        if (d == -1)
            d = 3;
    }
    bool checksurround() { //주변 확인
        for (int i = 0; i < 4; i++) { //반시계로 돔
            rotation();
            ifforward();
            if (checkiswall() && map[dy][dx] == 0) { //앞쪽 칸이 청소되지 않을 경우
                movement(); 
                return true;
            }
            dy = y; dx = x; //이동하기 전으로 돌려 놓음
        }
        return false; //주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    cin >> n >> m;

    Cleaner cleaner;
    cin >> cleaner.y >> cleaner.x >> cleaner.d;

    for (int y = 0; y < n; y++)
        for (int x = 0; x < m; x++)
            cin >> map[y][x];

    while (true) {
        cleaner.cleaning();

        if (!cleaner.checksurround()) { //주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
            cleaner.ifbackward(); //후진 해보고 벽인지 체크
            if (!cleaner.checkiswall())
                break;

            cleaner.movement(); //벽이 아니면 이동
        }
    }

    cout << cleaner.cleancount;

    return 0;
}