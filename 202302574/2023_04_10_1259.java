import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int i;
        
        while(true){
            String n = sc.nextLine();
            if(n.equals("0")) break;
            
            int len = n.length();
            for(i=0; i< len/2; i++){
                if(n.charAt(i) != n.charAt(len-1-i)) break;
            }
            if(i == len/2) System.out.println("yes");
            else System.out.println("no");
        }
        
        
    }
}