import java.util.*;

public class p_149 {
    static int maxPoint(int[][] points) {
        if (points.length == 1)
            return 1;

        Arrays.sort(points, (item_1, item_2) -> Integer.compare(item_1[0], item_2[0]));
        int global_max = Integer.MIN_VALUE;

        for (int i = 0; i < points.length; i++) {
            HashMap<Double, Integer> shared_points = new HashMap<>();
            int local_max = Integer.MIN_VALUE;

            for (int j = i + 1; j < points.length; j++) {
                double dx = points[j][0] - points[i][0];
                double dy = points[j][1] - points[i][1];

                double slope;
                if (dx == 0) {
                    slope = Double.MAX_VALUE;
                } else {
                    slope = (double) (dy / dx);
                }

                if (shared_points.get(slope) == null) {
                    shared_points.put(slope, 2);
                } else {
                    shared_points.put(slope, shared_points.get(slope) + 1);
                }

                if (shared_points.get(slope) > local_max)
                    local_max = shared_points.get(slope);
            }

            if (local_max > global_max)
                global_max = local_max;
        }
        return global_max;
    }

    public static void main(String[] args) {
        int[][] points = { { 1, 1 }, { 3, 2 }, { 5, 3 }, { 4, 1 }, { 2, 3 }, { 1, 4 } };
        System.out.println(maxPoint(points));
    }
}
