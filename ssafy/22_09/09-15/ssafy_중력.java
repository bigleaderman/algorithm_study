import java.util.Arrays;
import java.util.Scanner;

public class ssafy_중력 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int tc = sc.nextInt();
    for (int i = 1; i <= tc; i++) {
      int n = sc.nextInt();
      int arr[] = new int[n];
      int result[] = new int[n];

      for (int j = 0; j < n; j++) {
        arr[j] = sc.nextInt();
        result[j] = n - 1 - j;
      }

      for (int j = 1; j < n; j++) {
        for (int k = 0; k < j; k++) {
          if (arr[k] <= arr[j]) {
            result[k] -= 1;
          }
        }
      }

      Arrays.sort(result);
      System.out.println("#" + i + " " + result[result.length - 1]);
    }
  }
}
