import java.util.Scanner;

public class backjoon_1330_두수비교하기 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int a, b;

    a = sc.nextInt();
    b = sc.nextInt();

    if (a > b) {
      System.out.println(">");
    } else if (a < b) {
      System.out.println("<");
    } else {
      System.out.println("==");
    }
  }

}
