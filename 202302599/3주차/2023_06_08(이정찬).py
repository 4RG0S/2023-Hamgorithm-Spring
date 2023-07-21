import java.util.Scanner;

public class CP_P_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long N = sc.nextLong();

        long result = 0L;

        long [] M = new long [(int) (N-1)];
        long [] K = new long [(int) (N)];

        for( int i = 0 ; i < N-1 ; i++ ) {
            M[i] = sc.nextLong();
        }
        for( int i = 0 ; i < N ; i++ ) {
            K[i] = sc.nextLong();
        }
        
        long a = 1000000001;

        for ( int i = 0 ; i < N-1; i++) {
            if (a < K[i]) {
                result += (long)a*(long)M[i];
                continue;
            }
            else{
                a = (long)K[i];
                result += (long)K[i] * (long)M[i];
            }
        }
        System.out.println(result);
        
    }
}
