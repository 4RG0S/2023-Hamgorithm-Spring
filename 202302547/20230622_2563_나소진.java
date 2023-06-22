package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int[][] arr = new int[100][100];
		int area = 0;

		int cnt = sc.nextInt();

		for (int i = 0; i < cnt; i++) {
			int length = sc.nextInt();
			int width = sc.nextInt();

			for (int l = 0; l < 10; l++) {
				for (int w = 0; w < 10; w++) {
					arr[length + l][width + w] += 1;
				}
			}
		}

		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				if (arr[i][j] > 0) {
					area += 1;
				}
			}
		}
		
		System.out.println(area);
	}
}
