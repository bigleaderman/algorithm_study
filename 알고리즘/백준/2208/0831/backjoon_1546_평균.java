import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class backjoon_1546_평균 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());
    StringTokenizer st = new StringTokenizer(br.readLine());
    double[] arr = new double[N];
    double sum = 0;
    double score = 0;
    double maxNum = 0;
    for (int i = 0; i < N; i++) {
      score = Integer.parseInt(st.nextToken());
      if (score > maxNum) {
        maxNum = score;
      }
      arr[i] = score;
    }

    for (int i = 0; i < N; i++) {
      double newNum = arr[i] / maxNum * 100;
      arr[i] = (newNum);
      sum += newNum;
    }
    System.out.println(sum / N);
  }
}
