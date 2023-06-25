package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		for(int a=0; a<num; a++) {
			
			for(int b=a; b<num-1; b++) {
				System.out.print(" ");
			}
			
			for(int c=0; c<a*2+1; c++) {
				System.out.print("*");
			}
			
			System.out.print("\n");
		}
		
		for(int a=num-1; a>0; a--) {
			for(int b=num; b>a; b--) {
				System.out.print(" ");
			}
		
			for(int c=1; c<=a*2-1; c++) {
				System.out.print("*");
			}
			
			System.out.print("\n");
		}
	}
}
