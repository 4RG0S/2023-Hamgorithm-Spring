package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		char[][] strArr = new char[5][15];
		int max = 0;

		for (int i = 0; i < 5; i++) {
			String str = sc.nextLine();
			for (int j = 0; j < str.length(); j++) {
				strArr[i][j] = str.charAt(j);
			}
			if (max < str.length()) {
				max = str.length();
			}
		}

		for (int j = 0; j < max; j++) {
			for (int i = 0; i < 5; i++) {
				if (strArr[i][j] == '\0') {
					continue;
				} else {
					System.out.printf("%c", strArr[i][j]);
				}
			}
		}

		
	}
}
