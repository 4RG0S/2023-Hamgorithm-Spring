package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int arr[] = new int[10];
		
		for(int a=0; a<9; a++) {
			arr[a] = sc.nextInt();
		}
				
		int max = Integer.MIN_VALUE;
		int maxIdx = 0;
		
		for(int b=0; b<9; b++) {
			if(arr[b] > max) {
				max = arr[b];
				maxIdx = b+1;
			}			
		}
		System.out.printf("%d \n%d", max, maxIdx);
	}
}

