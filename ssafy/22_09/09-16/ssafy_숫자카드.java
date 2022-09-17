import java.lang.ProcessBuilder.Redirect.Type;
import java.util.Scanner;
import java.util.Arrays;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class ssafy_숫자카드 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    StringTokenizer st;

    int N = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= N; tc++) {
      int num = Integer.parseInt(br.readLine());
      st = new StringTokenizer(br.readLine());
      int numList[] = new int[10];
      System.out.println(Double.parseDouble(st.nextToken()));
      for (int i = 0; i < num; i++) {
        // numList[st.] += 1;
      }
      int maxNum = 0;
      int maxCount = 0;
      for (int i = 9; i > 0; i--) {
        if (numList[i] > maxCount) {
          maxCount = numList[i];
          maxNum = i;
        }
      }
      System.out.println("#" + tc + " " + maxNum + " " + maxCount);
    }
  }
}
