#include <iostream>
using namespace std;

int main(void) {
    int N, K, cnt;
    cin >> N;

    N -= 1;
    K = 0;
    cnt = 1;

    while (N > 0) {
        K += 1;
        N -= 6 * K;
        cnt += 1;
    };

    cout << cnt;

    return 0;
}