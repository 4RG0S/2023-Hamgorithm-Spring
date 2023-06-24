package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();

        int[] numArr = new int[num];

        for (int i = 0; i < num; i++) {
            numArr[i] = sc.nextInt();
        }

        int max = 0;
        int min = Integer.MAX_VALUE;

        for (int i = 0; i < num; i++) {
            if (numArr[i] < min) {
                min = numArr[i];
            } else if (numArr[i] - min > max) {
                max = numArr[i] - min;
            }
        }

        System.out.println(max);
		
	}
}
