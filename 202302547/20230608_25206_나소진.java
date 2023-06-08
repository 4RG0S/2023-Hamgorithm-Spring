package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		String[] str = new String[20];
		long credit = 0;
		double grade = 0.0;

		for (int i = 0; i < 20; i++) {
			str[i] = sc.nextLine();
		}

		for (int i = 0; i < 20; i++) {
			String[] str1 = str[i].split(" ");

			if (str1[2].equals("P") == false) {
				credit += str1[1].charAt(0) - '0';
				
				switch (str1[2]) {
				case "A+":
					grade += 4.5 * (str1[1].charAt(0) - '0');
					break;
				case "A0":
					grade += 4.0 * (str1[1].charAt(0) - '0');
					break;
				case "B+":
					grade += 3.5 * (str1[1].charAt(0) - '0');
					break;
				case "B0":
					grade += 3.0 * (str1[1].charAt(0) - '0');
					break;
				case "C+":
					grade += 2.5 * (str1[1].charAt(0) - '0');
					break;
				case "C0":
					grade += 2.0 * (str1[1].charAt(0) - '0');
					break;
				case "D+":
					grade += 1.5 * (str1[1].charAt(0) - '0');
					break;
				case "D0":
					grade += 1.0 * (str1[1].charAt(0) - '0');
					break;
				case "F":
					grade += 0.0 * (str1[1].charAt(0) - '0');
					break;
				default:
					break;
				}
			}
		}

		System.out.printf("%f", grade/credit);
	}
}
