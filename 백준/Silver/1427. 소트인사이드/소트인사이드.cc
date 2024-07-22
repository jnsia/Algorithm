#include <iostream>
using namespace std;

int temp;
int arr[10];

void sort(int len) {
    for (int i = 0; i < len; i++)
    {
        for (int j = i; j < len; j++)
        {
            if (arr[i] < arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(0); // false
    cin.tie(0); // NULL
    cout.tie(NULL); // 0

    int N;
    cin >> N;

    int len = 0;

    while (N > 0) {
        arr[len] = N % 10;
        N /= 10;
        len += 1;
    }

    sort(len);

    for (int i = 0; i < len; i++)
    {
        cout << arr[i];
    }

    return 0;
}
