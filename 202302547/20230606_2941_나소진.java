package backjoon;

import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine();
        char[] strArr = str.toCharArray();

        int cnt = 0;
        String word = null;

        for (int i = 0; i < strArr.length; i++) {
            word = Character.toString(strArr[i]);

            if (i < strArr.length - 1) {
                word += Character.toString(strArr[i + 1]);
            }

            switch (word) {
                case "c=":
                case "c-":
                case "d-":
                case "lj":
                case "nj":
                case "s=":
                    cnt++;
                    i++;
                    break;
                case "dz":
                    if (i + 2 < strArr.length && Character.toString(strArr[i + 2]).equals("=")) {
                        cnt++;
                        i += 2;
                    } else {
                        cnt++;
                    }
                    break;
                case "z=":
                    cnt++;
                    i++;
                    break;
                default:
                    cnt++;
            }
        }

        System.out.println(cnt);
    }
}
