import java.util.Arrays;
import java.util.Scanner;

public class Backjoon_1157 {
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    String input = sc.next();
    input = input.toUpperCase();

    int[] arr = new int[26];
    int[] Tarr = new int[26];

    for (int i = 0; i < input.length(); i++) {
      int temp = input.charAt(i) - 'A';

      arr[temp] += 1;
      Tarr[temp] += 1;
    }

    Arrays.sort(Tarr);
    int max = 0;
    int count = 0;
    if (Tarr[25] == Tarr[24]) {
      System.out.println("?");
    } else {
      for (int i = 0; i < arr.length; i++) {
        if (max < arr[i]) {
          max = arr[i];
          count = i;
        }
      }
      count = count + 65;
      // 해당 알파벳 위치에 처음에 빼준 A를 더해줌
      char answer = (char) count;
      System.out.println(answer);
    }

  }
}
