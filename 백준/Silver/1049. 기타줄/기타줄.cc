#include <iostream>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    int min_package = 1001;
    int min_each = 1001;

    for (int i = 0; i < M; ++i) {
        int package, each;
        cin >> package >> each;
        if (package < min_package)
            min_package = package;
        if (each < min_each)
            min_each = each;
    }

    if (min_each * 6 < min_package) {
        cout << N * min_each << endl;
    } else {
        int answer = (N / 6) * min_package;
        N %= 6;
        if (min_each * N < min_package)
            answer += min_each * N;
        else
            answer += min_package;
        cout << answer << endl;
    }

    return 0;
}
