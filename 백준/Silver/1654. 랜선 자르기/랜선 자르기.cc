#include <iostream>
using namespace std;

int K, N;
long arr[10000];

int upper_bound() {
    long low = 1;
    long high = 2147483647;

    while (low <= high) {
        long mid = (low + high) / 2;
        long res = 0;

        for (int i = 0; i < K; i++)
        {
            res += arr[i] / mid;
        }

        if (res >= N) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }

    return high;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    cin >> K >> N;

    for (int i = 0; i < K; i++) {
        cin >> arr[i];
    }

    cout << upper_bound();

    return 0;
}
