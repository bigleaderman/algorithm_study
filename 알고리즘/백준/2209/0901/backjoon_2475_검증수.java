import java.util.Scanner;

public class backjoon_2475_검증수 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int Sum = 0;

    for (int i = 0; i < 5; i++) {
      int num = sc.nextInt();
      Sum += num * num;
    }
    System.out.println(Sum % 10);
  }

}
