package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		while(sc.hasNextLine()) {
			String str = sc.nextLine();
			
			if(str == "") {
				sc.close();
				break;
			} 
			
			System.out.println(str);

		}
    }
}