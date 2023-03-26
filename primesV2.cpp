#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

bool is_prime(int num) {
    if (num < 2) {
        return false;
    }
    for (int i = 2; i <= sqrt(num); ++i) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

bool is_sophie_germain(int num) {
    return is_prime(num) && is_prime(2 * num + 1);
}

bool is_safe_prime(int num) {
    return is_prime(num) && is_prime((num - 1) / 2);
}

vector<int> get_lower_primes(int num) {
    vector<int> primes;
    for (int i = 2; i < num; ++i) {
        if (is_prime(i)) {
            primes.push_back(i);
        }
    }
    return primes;
}

int main() {
    int num_digits;
    cout << "Enter the number of digits: ";
    cin >> num_digits;

    int max_num = pow(10, num_digits) - 1;
    cout << "Finding highest prime...\n";
    int p = max_num;
    while (!is_prime(p)) {
        --p;
    }
    cout << "Highest prime: " << p << endl;

    cout << "Finding lower primes...\n";
    vector<int> lower_primes = get_lower_primes(p);
    cout << "Lower primes: [";
    for (int i = 0; i < lower_primes.size(); ++i) {
        if (lower_primes[i] < pow(10, num_digits - 1)) {
            cout << "0";
        }
        cout << to_string(lower_primes[i]);
        if (i < lower_primes.size() - 1) {
            cout << ", ";
        }
    }
    cout << "]" << endl;

    cout << "Checking for Sophie Germain and safe primes...\n";
    for (int prime : lower_primes) {
        cout << prime;
        if (is_sophie_germain(prime)) {
            cout << " is a Sophie Germain prime";
            if (is_safe_prime(prime)) {
                cout << " and a safe prime";
            }
        } else if (is_safe_prime(prime)) {
            cout << " is a safe prime";
        }
        cout << endl;
    }

    return 0;
}
