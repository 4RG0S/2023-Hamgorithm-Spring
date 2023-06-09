package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int[][] arr1 = new int[9][9];
		int max = 0;
		int col = 0;
		int row = 0;
		
		for(int i=0; i<9; i++) {
			for(int j=0; j<9; j++) {
				arr1[i][j] = sc.nextInt();
			}
		}
		
		for(int i=0; i<9; i++) {
			for(int j=0; j<9; j++) {
				if(max < arr1[i][j]) {
					max = arr1[i][j];
					col = i;
					row = j;
				}
			}
		}
		
		System.out.println(max);
		System.out.printf("%d %d", col+1, row+1);		
	}
}
