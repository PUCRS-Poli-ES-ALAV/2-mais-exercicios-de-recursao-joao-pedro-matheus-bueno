import java.util.ArrayList;
import java.util.Arrays;

public class Ex8 {
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(3, 7, 2, 9, 4, 10, 1));
        System.out.println("Maior elemento: " + findBiggest(numbers));
    }
    
    public static int findBiggest(ArrayList<Integer> ar) {
        if (ar.size() == 1) {
            return ar.get(0);
        }

        int first = ar.remove(0);

        int biggestRest = findBiggest(ar);

        return Math.max(first, biggestRest);
    }
}
