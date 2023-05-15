package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		char str = sc.nextLine().charAt(0);
		int a = Integer.valueOf(str);
		byte by = (byte)(a);
		
		System.out.println(by);
	}
}
