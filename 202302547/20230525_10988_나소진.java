package cp1_hw;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String str = sc.nextLine();
		int sum = 0;

		char[] strArr = str.toCharArray();
		
		for(int i=0; i<str.length(); i++) {
			if(strArr[i]==strArr[str.length()-1-i]) {
				sum += 1;
			} 
			
		}

		if(sum==str.length()) {
			System.out.println("1");
		} else {
			System.out.println("0");
		}
	}
}
