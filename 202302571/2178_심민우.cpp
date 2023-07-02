// 23.06.30
// BOJ 2178
// 그래프 이론

#include <iostream>
#include <queue>

using namespace std;

struct miro { //좌표와 이동 횟수를 저장하는 구조체
    int x, y;
    int cnt;

    miro(int x, int y, int cnt) { //구조체 생성자
        this->x = x;
        this->y = y;
        this->cnt = cnt;
    }
};

int dx[] = { -1,0,1,0 }; //왼쪽 위 오른쪽 아래 (이동방향)
int dy[] = { 0,1,0,-1 };
int n, m;

char map[101][101]; //미로 저장
bool isvisited[101][101] = { {false,} }; //방문 여부 저장

bool isinside(int x, int y) { //좌표가 맵 안에 있는지 체크
    return (x >= 0) && (x <= n - 1) && (y >= 0) && (y <= m - 1);
}
    
int bfs(int x, int y) {
    queue<miro> q;
    q.push(miro(0, 0, 1)); //시작위치 (1,1)이 아닌 (0,0)

    while (!q.empty()) {
        //큐의 현재 원소 꺼내고 pop
        miro cur = q.front();
        q.pop();
        
        if (isvisited[cur.x][cur.y]) //이미 방문한 좌표면 continue
            continue;

        isvisited[cur.x][cur.y] = true; //방문하지 않았다면 방문 표시

        if (cur.x == x && cur.y == y) //목적 위치라면 return
            return cur.cnt;

        //현재 위치의 주변 확인
        for (int i = 0; i < 4; i++) {
            int nextX = cur.x + dx[i];
            int nextY = cur.y + dy[i];

            if (!isinside(nextX, nextY)) //map 밖이면 continue
                continue;
            if (map[nextX][nextY] == '0') //이동할 수 없으면 continue
                continue;

            /*
            cout << "cur.x/cur.y/cur.cnt: " << cur.x << '/' << cur.y << '/' << cur.cnt << " -> ";
            cout << "nx/ny/ncnt: " << nextX << '/' << nextY << '/' << cur.cnt + 1 << '\n';

            //디버깅용 코드
            //bfs가 왜 최단거리인지 이해
            */

            q.push(miro(nextX, nextY, cur.cnt + 1)); //자식 노드 큐에 push
        }
    }

    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;

    for (int i = 0; i < n; i++)
        cin >> map[i];

    cout << bfs(n - 1, m - 1); //시작 위치가 (1,1)이 아닌 (0,0)이므로

    return 0;
}