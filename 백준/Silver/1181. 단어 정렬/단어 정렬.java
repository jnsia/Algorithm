    import java.util.*;

    public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            int N = sc.nextInt();

            Set<String> set = new HashSet<>();
            List<String> arr = new ArrayList<>();

            for (int i = 0; i < N; i++) {
                String input = sc.next();
                set.add(input);
            }

            for (String string: set) {
                arr.add(string);
            }

            arr.sort(comparator);

            for (int i = 0; i < arr.size(); i++) {
                System.out.println(arr.get(i));
            }
        }

        static Comparator<String> comparator = new Comparator<>() {
            @Override
            public int compare(String o1, String o2) {
                if (o1.length() > o2.length()) {
                    return 1;
                } else if (o1.length() < o2.length()) {
                    return -1;
                } else {
                    return o1.compareTo(o2);
                }
            }
        };
    }
