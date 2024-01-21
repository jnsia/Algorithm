#include <iostream>
using namespace std;

int main() {

    int A[10];
    int B[10];

    for (int i = 0; i < 10; i++) {
        cin >> A[i];
    }

    for (int i = 0; i < 10; i++) {
        cin >> B[i];
    }

    int aw = 0, bw = 0;

    for (int i = 0; i < 10; i++) {
        if (A[i] > B[i]) {
            aw++;
        } else if (A[i] < B[i]) {
            bw++;
        }
    }

    if (aw == bw) {
        cout << 'D' << endl;
    } else if (aw > bw) {
        cout << 'A' << endl;
    } else {
        cout << 'B' << endl;
    }

    return 0;
}
