import java.util.*;
import java.math.BigInteger;

public class Main {
    public static boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static boolean isSophieGermain(int p) {
        int q = 2 * p + 1;
        return isPrime(q);
    }

    public static boolean isSafePrime(int p) {
        int q = (p - 1) / 2;
        return isPrime(p) && isPrime(q);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of digits: ");
        int digits = input.nextInt();
        int max = (int) Math.pow(10, digits) - 1;
        int min = (int) Math.pow(10, digits - 1);

        System.out.println("Finding highest prime...");
        int highestPrime = 0;
        for (int i = max; i >= min; i--) {
            if (isPrime(i)) {
                highestPrime = i;
                break;
            }
        }
        System.out.println("Highest prime: " + highestPrime);

        System.out.println("Finding lower primes...");
        List<String> lowerPrimes = new ArrayList<String>();
        for (int i = 2; i < highestPrime; i++) {
            if (isPrime(i)) {
                lowerPrimes.add(String.format("%0" + digits + "d", i));
            }
        }
        System.out.println("Lower primes: " + lowerPrimes);

        System.out.println("Checking for Sophie Germain and safe primes...");
        for (String prime : lowerPrimes) {
            int p = Integer.parseInt(prime);
            if (isSophieGermain(p) && isSafePrime(p)) {
                System.out.println(p + " is a Sophie Germain and safe prime");
            } else if (isSophieGermain(p)) {
                System.out.println(p + " is a Sophie Germain prime");
            } else if (isSafePrime(p)) {
                System.out.println(p + " is a safe prime");
            }
        }
    }
}
