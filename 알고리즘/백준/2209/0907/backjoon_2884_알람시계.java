import java.util.Scanner;

public class backjoon_2884_알람시계 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int hour = sc.nextInt();
    int minute = sc.nextInt();

    if (hour == 0) {
      if (minute < 45) {
        hour = 23;
        minute = minute + 15;
      } else {
        minute = minute - 45;
      }
    } else {
      if (minute < 45) {
        hour = hour - 1;
        minute = minute + 15;
      } else {
        minute = minute - 45;
      }

    }
    System.out.println(hour + " " + minute);
  }
}
