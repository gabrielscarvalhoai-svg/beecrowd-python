import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main (String[] args) {

        Locale.setDefault(Locale.US);
        Scanner keyboard = new Scanner(System.in);

        double pi = 3.14159;
        double raio = keyboard.nextDouble();

        double resultado = pi * raio * raio;
        
        System.out.printf("A=%.4f\n", resultado);
    }
}