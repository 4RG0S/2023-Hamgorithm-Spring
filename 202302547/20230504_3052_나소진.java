package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
			Scanner sc = new Scanner(System.in);
			boolean[] arr = new boolean[42];
			
			for(int i=0 ; i<10 ; i++) {
				arr[sc.nextInt()%42] = true;
			}
			
			int cnt = 0;
			
			for(boolean value : arr) {
				if(value) {
					cnt++;
				}
			}
			System.out.println(cnt);
	}
}

