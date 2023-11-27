#include <iostream>
using namespace std;

int N;
int temp;
int arr[10001];

int main()
{
    ios::sync_with_stdio(0); // false
    cin.tie(0); // NULL
    cout.tie(NULL); // 0

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        arr[temp] += 1;
    }

    for (int i = 0; i < 10001; i++)
    {
        temp = arr[i];

        for (int j = 0; j < temp; j++)
        {
            cout << i << "\n";
        }
    }

    return 0;
}
