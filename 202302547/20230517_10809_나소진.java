package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        int[] arr2 = new int[26];

        
        for(int i = 0; i < 26; i++) {
        	if(arr2[i] == 0) {
        		arr2[i] = -1;
        	}
        }
        
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            int index = ch - 'a';
            if (arr2[index] == -1) {
                arr2[index] = i;
            }
        }
        
        for (int i = 0; i < 26; i++) {
            System.out.print(arr2[i] + " ");
        }
    }
}