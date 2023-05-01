package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);
		
		while(true) {
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		
		if(num1 + num2==0) {
			break;
		} else {
			System.out.printf("%d\n", num1 + num2);
		}
		}
	}
}

