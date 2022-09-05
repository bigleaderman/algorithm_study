import java.util.Scanner;

public class backjoon_2577_숫자의개수 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int num = sc.nextInt() * sc.nextInt() * sc.nextInt();
    int[] answer = new int[10];
    int input;
    while (num != 0) {
      input = num % 10;
      num = num / 10;
      answer[input] += 1;
    }
    for (int i = 0; i <= 9; i++) {
      System.out.println(answer[i]);
    }

  }
}
