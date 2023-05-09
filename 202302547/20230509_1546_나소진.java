package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int sub = sc.nextInt();
		double max = 0, sum = 0;
		double avr = 0;
		
		double[] arr = new double[sub];
		double[] arr2 = new double[sub];
			
		for(int i=0; i<sub; i++) {
			arr[i] = sc.nextDouble();
			sum += arr[i];
			if(arr[i]>max) {
				max = arr[i];
			}
		}
		
		for(int i=0; i<sub; i++) {
			arr2[i] = arr[i]/max*100;
			avr += arr2[i];
		}
		
		System.out.printf("%f", avr/sub);
	}
}

