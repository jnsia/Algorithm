    import java.util.*;

    public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            String[] input = sc.nextLine().split(" ");
            int N = Integer.parseInt(input[0]);
            int M = Integer.parseInt(input[1]);

            input = sc.nextLine().split(" ");
            List<Integer> list = new ArrayList<>();

            for (String s: input) {
                list.add(Integer.parseInt(s));
            }

            int answer = 0;
            int minValue = 1000000;

            for (int i = 0; i < list.size() - 2; i++) {
                for (int j = i + 1; j < list.size() - 1; j++) {
                    for (int k = j + 1; k < list.size(); k++) {
                        int sum = list.get(i) + list.get(j) + list.get(k);
                        int diff = M - sum;

                        if (M >= sum && minValue > diff) {
                            answer = sum;
                            minValue = diff;
                        };
                    }
                }
            }

            System.out.println(answer);
        }
    }
