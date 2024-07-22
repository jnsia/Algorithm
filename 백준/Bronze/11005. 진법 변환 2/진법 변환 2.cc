#include <iostream>
using namespace std;

char char_set[100];

int main(void) {
    int N, B, temp;

    cin >> N >> B;

    int size = 0;

    while (N > 0) {
        temp = N % B;
        N /= B;

        if (temp < 10) {
            char_set[size++] = char(temp + int('0'));
        }
        else {
            char_set[size++] = char((temp - 10) + int('A'));
        }
    }

    for (int i = 0; i < size; i++)
    {
        cout << char_set[size - i - 1];
    }

    return 0;
}