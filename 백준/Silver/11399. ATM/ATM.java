     import java.util.*;

    public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            String[] input = sc.nextLine().split(" ");
            int N = Integer.parseInt(input[0]);

            input = sc.nextLine().split(" ");
            List<Integer> list = new ArrayList<>();

            for (String s: input) {
                list.add(Integer.parseInt(s));
            }

            Collections.sort(list);

            int sum = 0;
            int answer = 0;

            for (int number: list) {
                answer += number + sum;
                sum += number;
            }

            System.out.println(answer);
        }

    }
