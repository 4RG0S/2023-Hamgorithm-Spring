package backjoon;

import java.util.*;

public class Main {
	static int t, m, n, k;
	static int cnt;
	static int[][] field;
	static boolean[][] vis;
	static int[] dx = { 1, 0, -1, 0 };
	static int[] dy = { 0, 1, 0, -1 };

	static void bfs(int x, int y) {
		Queue<int[]> q = new LinkedList<int[]>();
		q.add(new int[] { x, y });

		while (!q.isEmpty()) {
			x = q.peek()[0]; // 큐 첫 번째 항목(배열)의 첫 번째 값인 x에 접근
			y = q.peek()[1]; // 큐 첫 번째 항목(배열)의 두 번째 값인 y에 접근
			vis[x][y] = true; 
			q.poll(); // 큐 첫번째 값을 반환하고 제거 비어있다면 null

			// 인접한 방향의 노드 탐색 반복문
			for (int i = 0; i < 4; i++) { 				
				int ax = x + dx[i];
				int ay = y + dy[i];

				if (ax >= 0 && ay >= 0 && ax < m && ay < n) { // 각 노드의 in Range 검증
					if (!vis[ax][ay] && field[ax][ay] == 1) { // 배추가 있지만 방문하지 않았던 노드 검증
						q.add(new int[] { ax, ay });
						vis[ax][ay] = true;
					}
				}
			}
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		t = sc.nextInt();
		
		for (int c = 0; c < t; c++) { 
			m = sc.nextInt(); 
			n = sc.nextInt(); 
			k = sc.nextInt(); 
			cnt = 0;
			
			field = new int[m][n]; // 각 노드가 연결된 정보를 2차원 배열로 표현 (배추밭)
			vis = new boolean[m][n]; // 각 노드의 방문 정보를 1차원 배열로 표현 (방문 1, 미방문 0)
			
			for (int j = 0; j < k; j++) {
				int x = sc.nextInt();
				int y = sc.nextInt();
	
				field[x][y] = 1;
			}
			
			for(int i=0; i<m; i++) {
				for(int j=0; j<n; j++) {
					if(field[i][j]==1&&!vis[i][j]) { // 배추가 있지만 방문하지 않았던 노드 검증
						bfs(i, j);
						cnt++;
					}
				}
			}
			
			System.out.println(cnt);
		}
	}
}
