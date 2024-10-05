    import java.util.*;

    public class Main {

         static class Coord {
            int x;
            int y;

            Coord(int x, int y) {
                this.x = x;
                this.y = y;
            }
        }

        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            int N = sc.nextInt();
            List<Coord> arr = new ArrayList<>();

            for (int i = 0; i < N; i++) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                arr.add(new Coord(x, y));
            }

            arr.sort(comparator);


            for (int i = 0; i < N; i++) {
                System.out.println(arr.get(i).x + " " + arr.get(i).y);
            }
        }

        static Comparator<Coord> comparator = new Comparator<>() {
            @Override
            public int compare(Coord o1, Coord o2) {
                if (o1.x > o2.x) {
                    return 1;
                } else if (o1.x < o2.x) {
                    return -1;
                } else {
                    if (o1.y > o2.y) {
                        return 1;
                    } else if (o1.y < o2.y) {
                        return -1;
                    } else {
                        return 0;
                    }
                }
            }
        };
    }
