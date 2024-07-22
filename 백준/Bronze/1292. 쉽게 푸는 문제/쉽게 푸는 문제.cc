#include <iostream>
using namespace std;

int arr[500501];

int main() {
    int A, B;
    cin >> A >> B;

    int size = 1;

    for (int i = 1; i <= 1000; ++i) {
        for (int j = 0; j < i; ++j) {
            arr[size++] = i;
        }
    }

    int answer = 0;

    for (int i = A; i <= B; ++i) {
        answer += arr[i];
    }

    cout << answer << "\n";

    return 0;
}
