package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String str = sc.nextLine();
		int sec = 0;
		int sec_sum = 0;
		
		for(int i=0; i<str.length(); i++) {
			char ch = str.charAt(i);
			int idx = ch - 'A';
			
			if(idx<=2) {sec = 3;}
			else if(idx<=5) {sec = 4;}
			else if(idx<=8) {sec = 5;}
			else if(idx<=11) {sec = 6;}
			else if(idx<=14) {sec = 7;}
			else if(idx<=18) {sec = 8;}
			else if(idx<=21) {sec = 9;}
			else {sec = 10;}
			
			sec_sum = sec_sum + sec;
		}
		System.out.println(sec_sum);
    }
}