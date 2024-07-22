#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int N, S;
    std::cin >> N;

    std::vector<int> arr(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    std::cin >> S;

    for (int i = 0; i < N - 1; ++i) {
        if (S == 0) {
            break;
        }

        int mx = arr[i];
        int idx = i;

        for (int j = i + 1; j < std::min(N, i + S + 1); ++j) {
            if (mx < arr[j]) {
                mx = arr[j];
                idx = j;
            }
        }

        S -= idx - i;

        for (int j = idx; j > i; --j) {
            arr[j] = arr[j - 1];
        }

        arr[i] = mx;
    }

    for (int i = 0; i < N; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
