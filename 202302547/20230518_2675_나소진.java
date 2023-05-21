package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		sc.nextLine();
		
		for(int i=0; i<num; i++) {
			String str = sc.nextLine();
			char[] arr = str.toCharArray();
			int arrNum = arr[0] - '0';

			
			for(int j=2; j<arr.length; j++) {
				for(int k=0; k<arrNum; k++) {
					System.out.printf("%c", arr[j]);
				}
			}
			System.out.println();
		}
    }
}