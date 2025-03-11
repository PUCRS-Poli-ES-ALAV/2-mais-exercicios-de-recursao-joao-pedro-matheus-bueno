public class Ex10 {
   public static void main(String[] args) {
        System.out.println(nroDigit(123456789));
   } 

   public static int nroDigit(int n){

        if(n < 10){
            return 1;
        }

        return 1 + nroDigit(n / 10); 
   }
}
