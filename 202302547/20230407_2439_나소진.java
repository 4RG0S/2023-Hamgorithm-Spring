package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);
		
		int count = sc.nextInt();
		
		for(int i=1; i<=count; i++) {
			
			for(int l=count; l>i; l--) {
				System.out.printf(" ");
			}
			
			for(int j=0; j<i; j++) {
				System.out.printf("*");
			}
			System.out.printf("\n");
		}
	}
}
