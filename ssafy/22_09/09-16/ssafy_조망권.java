import java.util.Scanner;
import java.util.Arrays;

public class ssafy_조망권 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int T = 10;

    for (int tc = 1; tc <= 10; tc++) {
      int N = sc.nextInt();
      int arr[] = new int[N];
      for (int i = 0; i < N; i++) {
        arr[i] = sc.nextInt();
      }
      int cnt = 0;
      for (int i = 2; i < N - 2; i++) {
        int maxArray[] = { arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2] };
        Arrays.sort(maxArray);
        if (maxArray[maxArray.length - 1] < arr[i]) {
          cnt += (arr[i] - maxArray[maxArray.length - 1]);
        }
      }
      System.out.println("#" + tc + " " + cnt);
    }
  }
}
