package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int cnt = sc.nextInt();
		int arr[] = new int[cnt];
		
		for(int a=0; a<cnt; a++) {
			arr[a] = sc.nextInt();
		}
				
		int max = Integer.MIN_VALUE;
		int min = Integer.MAX_VALUE;
		
		for(int b=0; b<cnt; b++) {
			if(arr[b] > max) {
				max = arr[b];
			}
			if(arr[b] < min) {
				min = arr[b];
			}
		}
		System.out.printf("%d %d", min, max);
	}
}

