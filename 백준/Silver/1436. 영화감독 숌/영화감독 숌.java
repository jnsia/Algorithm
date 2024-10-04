    import java.util.*;

    public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            int N = sc.nextInt();

            List<Integer> list = new ArrayList<>();

            int number = 0;

            while (list.size() < 10000) {
                if ((number + "").contains("666")) {
                    list.add(number);
                }

                number++;
            }

            System.out.println(list.get(N - 1));
        }
    }
