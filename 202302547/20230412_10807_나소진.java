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
		
		int idx = sc.nextInt();
		int numcnt = 0;
		
		for(int b=0; b<cnt; b++) {
			if(arr[b]==idx) {
				numcnt++;
			}
		}
		System.out.print(numcnt);
	}
}

