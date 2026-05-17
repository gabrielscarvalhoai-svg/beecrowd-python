import java.util.Scanner;

public class Main {
    public static void main (String[] args) {
        Scanner keyboard = new Scanner(System.in);
        int A = keyboard.nextInt();
        int B = keyboard.nextInt();
        int Soma = A + B;
        System.out.printf("X = %d\n", Soma);
    }
}