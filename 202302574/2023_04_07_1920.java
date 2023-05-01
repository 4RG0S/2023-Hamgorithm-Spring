import java.util.Scanner;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static int binarySearch(int[] arr, int key) {
        int from = 0;
        int to = arr.length-1;
        
        while(from<=to){
            int mid = (from+to)/2;
            if(key>arr[mid]){
                from = mid+1;
            }
            else if(key<arr[mid]){
                to = mid-1;
            }
            else{
                return mid;
            }
            
        }
        return -1;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int[] arr = new int[num];
        
        for(int i=0; i<num; i++){
            arr[i]=sc.nextInt();
        }
        
        Arrays.sort(arr);
        
        int M = sc.nextInt();
        
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<M; i++){
            if(binarySearch(arr, sc.nextInt())>=0){
                sb.append(1).append('\n');
            }
            else{
                sb.append(0).append('\n');
            }
        }
        System.out.println(sb);
    }
}
