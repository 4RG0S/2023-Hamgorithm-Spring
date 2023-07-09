// 23.07.01
// BOJ 10026
// 그래프 이론

#include <iostream>
#include <cstring>

using namespace std;

int n;
char map[101][101]; //char map[100][100]으로 하면 틀린다... 이유는 모르겠다......
bool isvisited[100][100] = { {false,} };

int dx[] = { -1,0,1,0 }; //주변 탐색용
int dy[] = { 0,1,0,-1 };

bool isinside(int y, int x) { //map 안에 있는지 확인
    return (y >= 0) && (y < n) && (x >= 0) && (x < n);
}

void dfs(int y, int x, char color) {
    isvisited[y][x] = true;

    for (int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (!isinside(ny, nx)) //다음 좌표가 map 안에 없으면 continue
            continue;
        if (isvisited[ny][nx]) //다음 좌표를 했었으면 continue
            continue;
        if (map[ny][nx] != color) //다음 좌표 color 체크
            continue;

        dfs(ny, nx, color); //dfs 재귀
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;

    for (int i = 0; i < n; i++)
        cin >> map[i];
     
    //적록색약 아닐 때
    int cnt = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (!isvisited[i][j]) {
                dfs(i, j, map[i][j]); //같은 구역을 방문 처리
                cnt++;
            }
        }
    }
    cout << cnt << ' ';

    //적록색약 처리
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (map[i][j] == 'G')
                map[i][j] = 'R';
            isvisited[i][j] = false;
        }
    }

    cnt = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (!isvisited[i][j]) {
                dfs(i, j, map[i][j]);
                cnt++;
            }
        }
    }

    cout << cnt;

    return 0;
}