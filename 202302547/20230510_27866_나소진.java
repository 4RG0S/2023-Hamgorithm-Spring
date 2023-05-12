package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String s = sc.nextLine();
		int num = sc.nextInt();
		
		String[] arr = s.split("");

		System.out.printf("%s", arr[num-1]);
	}
}

