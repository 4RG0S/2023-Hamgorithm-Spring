package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		int temp = 0;
		
		int[] arr = new int[n];
		
		for(int b=0; b<n; b++) {
			arr[b] = b+1;
		}
				
		for(int a=0; a<m; a++) {
			int i = sc.nextInt();
			int j = sc.nextInt();

			temp = arr[i-1];
			arr[i-1] = arr[j-1];
			arr[j-1] = temp;
		}
		
		for(int b=0; b<n; b++) {
			System.out.printf("%d ", arr[b]);
		}
	}
}

