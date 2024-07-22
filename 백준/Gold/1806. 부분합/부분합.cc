#include <iostream>
using namespace std;

#define min(x, y) ((x > y) ? (y) : (x))

long long int arr[100001];

int main()
{
    int N, S;
    cin >> N >> S;

    for (int i = 1; i < N + 1; i++)
    {
        cin >> arr[i];
        arr[i] += arr[i - 1];
    }

    int i = 0;
    int j = 1;
    int answer = 100001;

    while (i < j && j <= N) {
        long long int temp = arr[j] - arr[i];

        if (temp == S) {
            answer = min(answer, (j - i));
            j++;
        }
        else if (temp > S) {
            answer = min(answer, (j - i));
            i++;
        }
        else {
            j++;
        }
    }

    if (answer == 100001) {
        cout << 0;
    }
    else {
        cout << answer;
    }

    return 0;
}
