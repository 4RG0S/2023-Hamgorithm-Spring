package baekjoon;

import java.io.*;
import java.util.Arrays;

public class pb_10808 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder stringBuilder = new StringBuilder();

        // Array for counting
        int[] alphabet_arr = new int[26];
        String input = br.readLine();

        // Init array
        Arrays.fill(alphabet_arr, 0);

        // Counting
        for(int i = 0; i < input.length(); i++) {
            alphabet_arr[input.toCharArray()[i] - 'a']++;
        }

        // Making stringBuilder
        for(int i = 0; i < 26; i++) {
            stringBuilder.append(alphabet_arr[i]).append(" ");
        }

        // Printing
        bw.write(stringBuilder.toString().trim());
        bw.flush();
        br.close();
        bw.close();
    }
}
