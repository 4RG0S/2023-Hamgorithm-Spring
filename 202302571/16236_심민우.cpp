// 23.08.27
// BOJ 16236
// 시뮬레이션

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <memory.h>

using namespace std;

int map[20][20] = { {0,} };
int n;

struct Shark {
    int y, x;
    int size;
    int distance = 0;
    int sizecount = 0;

    Shark(int Y, int X, int Size) : y(Y), x(X), size(Size) {}
};

bool compdistance(Shark& A, Shark& B) {
    if (A.distance == B.distance) {
        if (A.y == B.y)
            return A.x < B.x;
        else
            return A.y < B.y;
    }
    else
        return A.distance < B.distance;
}

int bfs(const Shark& babyshark, const Shark& edibleshark) {
    int dy[] = { 0,1,0,-1 };
    int dx[] = { 1,0,-1,0 };

    bool isvisited[20][20];
    memset(isvisited, false, sizeof(isvisited));

    queue<pair<Shark,int>> q;
    q.push({ babyshark,0 });
    while (!q.empty()) {
        pair<Shark, int> cur = q.front(); q.pop();
        int cury = cur.first.y;
        int curx = cur.first.x;

        if (isvisited[cury][curx])
            continue;
        isvisited[cury][curx] = true;

        if (cury == edibleshark.y && curx == edibleshark.x)
            return cur.second;

        for (int i = 0; i < 4; i++) {
            int ny = cury + dy[i];
            int nx = curx + dx[i];

            if (ny < 0 || ny >= n || nx < 0 || nx >= n)
                continue;
            if (map[ny][nx] > babyshark.size)
                continue;

            q.push({ Shark(ny,nx,babyshark.size), cur.second + 1 });
        }
    }

    return 9999;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    cin >> n;

    Shark babyshark = Shark(0, 0, 2);

    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            cin >> map[y][x];
            if (map[y][x] == 9) {
                babyshark.y = y; 
                babyshark.x = x;
            }
        }
    }
    int cnt = 0;
    while (true) {
        vector<Shark> edibleshark;
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < n; x++) {
                if (map[y][x] != 0 && map[y][x] < babyshark.size && map[y][x] != 9) {
                    edibleshark.push_back(Shark(y, x, map[y][x]));
                    edibleshark.back().distance = bfs(babyshark, edibleshark.back());
                }
            }
        }
        if (edibleshark.empty())
            break;
        sort(edibleshark.begin(), edibleshark.end(), compdistance);
        if (edibleshark.front().distance == 9999)
            break;
        cnt += edibleshark.front().distance;
        if (babyshark.size == ++babyshark.sizecount) {
            babyshark.size++;
            babyshark.sizecount = 0;
        }
        map[babyshark.y][babyshark.x] = 0;
        babyshark.y = edibleshark.front().y;
        babyshark.x = edibleshark.front().x;
        map[babyshark.y][babyshark.x] = 9;       
    }

    cout << cnt;

    return 0;
}