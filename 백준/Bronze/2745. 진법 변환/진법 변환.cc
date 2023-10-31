#include <iostream>
using namespace std;

int binary[60];

int power(int num, int times) {
    int result = 1;

    for (int i = 0; i < times; i++)
    {
        result *= num;
    }
    
    return result;
}

int main(void) {
    char N[60];
    int B, temp_int;
    char temp_char;
    int answer = 0;

    cin >> N >> B;

    int size = 0;

    for (int i = 0; i < 60; i++)
    {
        size = i;
        if (N[i] == NULL) break;
    }

    for (int i = 0; i < size; i++)
    {
        temp_char = N[size - i - 1];

        if (temp_char == NULL) break;

        if (int(temp_char) - int('9') <= 0) {
            temp_int = int(temp_char) - int('0');
        }
        else {
            temp_int = int(temp_char) - int('A') + 10;
        }

        answer += temp_int * int(power(B, i));
    }

    cout << answer;

    return 0;
}