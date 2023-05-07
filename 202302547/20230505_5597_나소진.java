package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		boolean[] arr = new boolean[30];
		int temp;
			
		for(int i=0; i<28; i++) {
			temp = sc.nextInt();
			arr[temp-1] = !arr[temp-1];
		}
		
		for(int i=0; i<30; i++) {
			if(!arr[i]) {
				System.out.println(i+1);
			}
		}		
	}
}

