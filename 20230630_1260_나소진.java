package backjoon;

import java.util.*;

public class Main {
	static int n, m, v;
	static int[][] graph;
	static boolean[] vis1; // DFS 탐색
	static boolean[] vis2; // BFS 탐색

	static void dfs(int v, int[][] graph, boolean[] vis1) { // 재귀로 DFS 구현
		vis1[v] = true; // 탐색 시작 번호
		System.out.print(v + " ");

		for (int i = 1; i <= graph.length - 1; i++) {
			if (!vis1[i] && graph[v][i] == 1) { // 연결됐지만 방문하지 않았던 노드 검증
				dfs(i, graph, vis1); // 재귀 호출
			}
		}
	}

	static void bfs(int v, int[][] graph, boolean[] vis2) { // 큐로 BFS 구현
		Queue<Integer> q = new LinkedList<>();
		q.add(v);
		vis2[v] = true;

		while (!q.isEmpty()) {
			v = q.poll(); // 큐 첫 번째 값을 반환하고 제거 (비어있다면 null)
			System.out.print(v + " ");

			for (int i = 1; i <= graph.length - 1; i++) {
				if (!vis2[i] && graph[v][i] == 1) { // 연결됐지만 방문하지 않았던 노드 검증
					q.add(i);
					vis2[i] = true;
				}
			}
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		m = sc.nextInt();
		v = sc.nextInt();

		vis1 = new boolean[n + 1];
		vis2 = new boolean[n + 1];
		graph = new int[n + 1][n + 1];

		for (int i = 0; i < m; i++) { // 인접 행렬 초기화
			int v1 = sc.nextInt();
			int v2 = sc.nextInt();

			graph[v1][v2] = 1; // 간선을 양방향으로 지정
			graph[v2][v1] = 1;
		}
		dfs(v, graph, vis1);
		System.out.println(); // 줄바꿈
		bfs(v, graph, vis2);
	}
}