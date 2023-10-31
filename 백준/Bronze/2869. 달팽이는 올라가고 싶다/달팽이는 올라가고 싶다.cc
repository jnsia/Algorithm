#include <iostream>
using namespace std;

int main(void) {
    int A, B, V, diff;
    cin >> A >> B >> V;

    diff = A - B;

    int answer = (V - A) / diff + 1;

    V = (V - A) % diff;

    if (V > 0) {
        answer += 1;
    }

    cout << answer;

    return 0;
}