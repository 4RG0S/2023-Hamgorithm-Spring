package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		String str = sc.nextLine();
		String[] arr = str.split(" ");

		int num = Integer.parseInt(arr[1]);
		int a = 0;
		int idx = 0;
		int sum = 0;

		for (int i = arr[0].length()-1; i >= 0; i--) {
			char c = arr[0].charAt(i);

			if (c >= '0' && c <= '9') {
				a = c - '0';
			} else {
				a = c - 55;
			}
			
			sum += a * Math.pow(num, idx++);
			
		}	
			System.out.println(sum);
		}
}
