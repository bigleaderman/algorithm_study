import java.util.Scanner;

public class backjoon_2742_기찍N {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();

    for (int i = 0; i < n; i++) {
      System.out.println(n - i);
    }
  }
}
