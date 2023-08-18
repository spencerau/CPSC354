#include <iostream>

using namespace std;

void q1();
void spaghetti_1();
void q2();
void spaghetti_2();

int main() {
    q1();
    spaghetti_1();
    q2();
    spaghetti_2();

    return 0;
}

void q1() {
    int max;
    cout << "Enter a positive integer: " << endl;
    cin >> max;
    int sum = 0;

    for(int i = 0; i < max; ++i) {
        sum+= i;
    }

    printf("Q1 Sum: %d\n", sum);

}

void spaghetti_1() {
    int max;
    cout << "Enter a positive integer: " << endl;
    cin >> max;
    int sum = 0;

    int i = 0;
    loop_start1:
    if (i < max) {
        sum += i;
        i++;
        goto loop_start1;
    }

    printf("Spaghetti_1 Sum: %d\n", sum);
}

void q2() {
    cout << "Enter a positive integer: " << endl;
    int candidate;
    cin >> candidate;
    bool isPowerOfTwo = true;

    while(candidate != 1) {
        if(candidate % 2 != 0){
            isPowerOfTwo = false;
            break;
        }
        candidate /= 2;
    }

    if(isPowerOfTwo){
        cout << "Your number is a power of two..." << endl;
    } else{
        cout << "Your number is NOT a power of two..." << endl;
    }
}

void spaghetti_2() {
    cout << "Enter a positive integer: " << endl;
    int candidate;
    cin >> candidate;
    bool isPowerOfTwo = true;

    loop_start2:
    if (candidate != 1) {
        if (candidate % 2 != 0) {
            isPowerOfTwo = false;
        }
        candidate /= 2;
        goto loop_start2;
    }

    if (isPowerOfTwo) {
        cout << "Power of 2 is True" << endl;
    } else {
        cout << "Power of 2 is False" << endl;
    }
}

