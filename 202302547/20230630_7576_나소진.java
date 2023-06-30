package backjoon;

import java.util.*;

public class Main {
	static int m, n, max = 0;
	static boolean min;
	static int[][] box;
	static boolean[][] vis;
	static int[] dx = { 1, 0, -1, 0 };
	static int[] dy = { 0, 1, 0, -1 };
	static Queue<int[]> q = new LinkedList<int[]>();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		m = sc.nextInt();
		n = sc.nextInt();

		box = new int[n][m];
		vis = new boolean[n][m];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				box[i][j] = sc.nextInt();
				if (box[i][j] == 1) { // 토마토가 있는 지점(1)을 큐에 저장
					q.offer(new int[] { i, j });
				}
			}
		}
		if (!q.isEmpty()) {
		    bfs(q.peek()[0], q.peek()[1]); // 토마토가 있는 지점(1)에서부터 탐색 시작
		}

		for (int i = 0; i < n; i++) { // 배열을 전체 탐색하여 결과 확인
			for (int j = 0; j < m; j++) {
				if (box[i][j] > max) { // '가장 큰 날짜 - 1'을 경과일자로 인식
					max = box[i][j];
				}
				if (box[i][j] == 0) { // 익지 않은 토마토(0)이 하나라도 있으면 min 활성화
					min = true;
				}
			}
		}

		if (min) { // True면 익지 않은 토마토(0)가 있으므로 -1 출력
			System.out.println(-1);
		} else { // 익지 않은 토마토(0)가 없으면 '가장 큰 날짜 - 1'을 경과일자로 인식
			System.out.println(max - 1);
		}
	}

	static void bfs(int x, int y) { // 큐를 사용한 BFS 탐색
		while (!q.isEmpty()) {
			x = q.peek()[0]; // 큐 첫 번째 항목(배열)의 첫 번째 값인 x에 접근
			y = q.peek()[1]; // 큐 첫 번째 항목(배열)의 두 번째 값인 y에 접근
			vis[x][y] = true;
			q.poll(); // 큐 첫 번째 값을 반환(비어있다면 null)

			// 인접한 방향의 노드 탐색 반복문
			for (int i = 0; i < 4; i++) {
				int ax = x + dx[i];
				int ay = y + dy[i];

				if (ax >= 0 && ay >= 0 && ax < n && ay < m) { // 각 노드의 in Range 검증
					if (!vis[ax][ay] && box[ax][ay] == 0) { // 노드 방문 여부와 익지 않은 토마토(0) 판별
						q.add(new int[] { ax, ay });
						vis[ax][ay] = true;
						box[ax][ay] = 1 + box[x][y]; // 1을 더하여 경과일자를 인식 (누적합)
					}
				}
			}
		}
	}
}
