package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int[] arr = new int[n];
		
		for(int a=0; a<m; a++) {
			int i = sc.nextInt();
			int j = sc.nextInt();
			int k = sc.nextInt();
			
			for(int b=i-1; b<j; b++) {
					arr[b] = k;
			}
		}
		
		for(int i=0; i<n; i++) {
			System.out.printf("%d ", arr[i]);
		}
	}
}

