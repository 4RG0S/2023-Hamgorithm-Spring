package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		sc.nextLine();
		 
		String[] str = new String[a];

		for(int i=0; i<a; i++) {
			str[i] = sc.nextLine();
		}
		
		for(int i=0; i<a; i++) {
			if(str[i].length() >= 1) {
	            System.out.print(str[i].charAt(0));
	            System.out.print(str[i].charAt(str[i].length()-1));
	        } else {
	        	System.out.print(str[i].charAt(0));
	        	System.out.print(str[i].charAt(0));
	        }
			System.out.println();
		}
	}
}

