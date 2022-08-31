import java.util.Scanner;

public class backjoon_2439_별찍기2 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int Num = sc.nextInt();

    for (int i = 0; i < Num; i++) {
      int space = Num - i - 1;
      while (space != 0) {
        System.out.print(" ");
        space -= 1;
      }
      for (int j = 0; j <= i; j++) {
        System.out.print("*");
      }
      System.out.println();
    }
  }
}
