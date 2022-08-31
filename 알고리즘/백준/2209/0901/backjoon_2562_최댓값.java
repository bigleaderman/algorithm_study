import java.util.Scanner;

public class backjoon_2562_최댓값 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int maxNum = 0;
    int maxNumIndx = 0;

    for (int i = 0; i < 9; i++) {
      int newNum = sc.nextInt();
      if (newNum > maxNum) {
        maxNum = newNum;
        maxNumIndx = i + 1;
      }
    }
    System.out.println(maxNum);
    System.out.println(maxNumIndx);
  }
}
