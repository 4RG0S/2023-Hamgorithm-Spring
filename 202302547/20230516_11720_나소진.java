package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		sc.nextLine();
		String str = sc.nextLine();
		
		
		char[] arr = str.toCharArray();
		int sum = 0;
		
		for(int i=0; i<num; i++) {
			int a = (int)(arr[i] - '0');
			sum += a;
		}
		
		System.out.println(sum);
	}
}