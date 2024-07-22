#include <iostream>
using namespace std;

int N, K;
int temp;
int arr[1000];

void sort() {
    for (int i = 0; i < N; i++)
    {
        for (int j = i; j < N; j++)
        {
            if (arr[i] > arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    cin >> N >> K;

    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    sort();

    for (int i = 1; i < K + 1; i++)
    {
        if (i == K) {
            cout << arr[N - i];
            break;
        }
    }

    return 0;
}
