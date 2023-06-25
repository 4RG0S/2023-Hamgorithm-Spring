package backjoon;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		sc.nextLine();
		
		double[] result = new double[num];
		
		for(int i=0; i<num; i++) {
			int sum = 0;
			double avg = 0;
			int student = 0;
			
			String str = sc.nextLine();
			String[] strArr = str.split(" ");
	
			for(int j=1; j<strArr.length; j++) {
				sum += Integer.parseInt(strArr[j]);
			}
			avg = sum/(strArr.length-1);
			
			for(int j=1; j<strArr.length; j++) {
				if(Integer.parseInt(strArr[j])>avg) {
					student += 1;
				}
			}
			double answer = (double)student / (double)(strArr.length-1) * 100.0;
			result[i] = answer;
		}
		for(int i=0; i<num; i++) {
			System.out.printf("%.3f%%\n", result[i]);
		}
    }
}