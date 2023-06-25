package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int num = sc.nextInt();
		int[] c = new int[num];

		for (int i = 0; i < num; i++) {
			c[i] = sc.nextInt();
		}

		for (int i = 0; i < num; i++) {
			int q = c[i] / 25;
			int d = (c[i] % 25) / 10;
			int n = (c[i] - q * 25 - d * 10) / 5;
			int p = c[i] % 5;

			System.out.printf("%d %d %d %d\n", q, d, n, p);
		}

	}
}
