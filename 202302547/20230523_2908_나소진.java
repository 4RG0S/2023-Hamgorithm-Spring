package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String str = sc.nextLine();
		String[] str_s = str.split("\\s");
		
		int num1 = Integer.parseInt(str_s[0]);
		int num2 = Integer.parseInt(str_s[1]);
		
		int num1_1 = num1/100;
		int num1_2 = (num1%100 - num1%10)/10;
		int num1_3 = num1%10;
					
		int num2_1 = num2/100;
		int num2_2 = (num2%100 - num2%10)/10;
		int num2_3 = num2%10;
		
		int a = num1_3*100 + num1_2*10 + num1_1;
		int b = num2_3*100 + num2_2*10 + num2_1;

		if(a>b) {
			System.out.println(a);
		} else {
			System.out.println(b);
		}
    }
}