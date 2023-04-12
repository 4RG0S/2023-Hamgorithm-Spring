import java.util.Scanner;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), i;
        int[] arr0 = new int[n];
        
        for(i=0; i<n; i++){
            arr0[i] = sc.nextInt();
        }
        Arrays.sort(arr0);
        
        int m = sc.nextInt();
        StringBuilder sb = new StringBuilder();
        for(i=0; i<m; i++){
            int key = sc.nextInt();
            sb.append(upperBound(arr0, key) - lowerBound(arr0, key)).append(' ');
        }
        System.out.println(sb);
    }
    public static int lowerBound(int[] arr, int key){
        int left, right, mid;
        left = 0;
        right = arr.length;
        while(left<right){
            mid = (left+right)/2;
            if(key<=arr[mid]){
                right = mid;
            }
            else{
                left = mid+1;
            }
        }
        return left;
        
    }
    public static int upperBound(int[] arr, int key){
        int left, right, mid;
        left = 0;
        right = arr.length;
        while(left<right){
            mid = (left+right)/2;
            if(key<arr[mid]){
                right = mid;
            }
            else{
                left = mid+1;
            }
        }
        return left;
    }
}