package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int[] arr = new int[n];
		int[] tempArr = new int[n];
			
		for(int i=0; i<n; i++) {
			arr[i] = i+1;
			tempArr[i] = arr[i];
		}

		for(int i=0; i<m; i++) {
			int a = sc.nextInt()-1;
			int b = sc.nextInt()-1;
			for(int j=a; j<=(b-a)/2+a; j++) {
				int temp = arr[j];
				arr[j] = arr[b-j+a];
				arr[b-j+a] = temp;
			}
		}
		
		for(int x=0; x<n; x++) {
			System.out.printf("%d ", arr[x]);
		}
	}
}

