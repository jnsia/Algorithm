#include <iostream>
using namespace std;

int main(void) {
    int N, K;
    cin >> N;

    K = 1;

    while (N > 0) {
        K *= 2;
        N -= 1;
    };

    cout << (K + 1) * (K + 1);

    return 0;
}