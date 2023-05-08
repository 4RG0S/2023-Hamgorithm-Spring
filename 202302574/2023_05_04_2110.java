import java.util.Scanner;
import java.util.Arrays;
 
public class Main {
	
	public static int[] house;
	
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		
		int N = in.nextInt();
		int M = in.nextInt();
		
		house = new int[N];
		
		for(int i = 0; i < N; i++) {
			house[i] = in.nextInt();
		}
		
		Arrays.sort(house);
		
		
		int left = 1;
		int right = house[N - 1] - house[0] + 1;
		
		while(left < right) {
			
			int mid = (right + left) / 2;

			if(whether(mid) < M) {
				right = mid;
			}
			else {
				left = mid + 1;
			}
		}

		System.out.println(left - 1);
	}
	
	public static int whether(int distance) {
		int count = 1;
		int lastLocate = house[0];
		
		for(int i = 1; i < house.length; i++) {
			int locate = house[i];
			if(locate - lastLocate >= distance) {
				count++;
				lastLocate = locate;
			}
		}
		return count;
	}
}