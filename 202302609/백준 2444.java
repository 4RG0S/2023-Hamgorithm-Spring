package cp1_hw;
public class Star {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for  (int i =7;i>0;i--) {
			for (int j =0 ; j<i ; j++) {
				System.out.print(" ");
			}
			for (int j =7; j>i;j--) {
				System.out.print("*");
			}
			for (int j =6; j>i;j--) {
				System.out.print("*");
			}
			System.out.printf("\n");
		}
		for  (int i =7;i>0;i--) {
			for (int j =7 ; j>i ; j--) {
				System.out.print(" ");
			}
			for (int j =0; j<i;j++) {
				System.out.print("*");
			}
			for (int j =1; j<i;j++) {
				System.out.print("*");
			}
			System.out.printf("\n");
		}
	}
}
