package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String str = sc.nextLine();
		String strLow = str.toLowerCase();
		
		char[] strArr = strLow.toCharArray();
		int[] alp = new int[26];
		int max = 0;
		int equal = 0;
		char answer = ' ';
		
		for(int i=0; i<26; i++) {
			for(int j=0; j<str.length(); j++) {
				if((char)('a'+i) == strArr[j]) {
					alp[i] = alp[i] + 1;
				}
			}
		}
		
		for(int i=0; i<26; i++) {
			if(max<alp[i]) {
				max = alp[i];
				answer = (char) ('A' + i);
			}
		}
		
		for(int i=0; i<26; i++) {
			if(max==alp[i]) {
				equal = equal+1;
			}
		}
		
		if(equal>1) {
			System.out.println("?");
		} else {
			System.out.println(answer);
		}
	}
}