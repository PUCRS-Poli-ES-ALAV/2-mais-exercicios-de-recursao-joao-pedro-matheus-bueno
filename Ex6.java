public class Ex6 {
    public static void main(String[] args){
       System.out.println(convBase2(5));
    }

    public static String convBase2(int n) {
        if (n == 0) {
            return "0";
        }
        if (n == 1) {
            return "1";
        }
        return convBase2(n / 2) + (n % 2);
    }
}
