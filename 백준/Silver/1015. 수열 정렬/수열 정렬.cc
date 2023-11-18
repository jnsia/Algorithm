#include <iostream>
using namespace std;

int N;
int arr[50];
int counting[1001];
int prefix[1001];
int answer[1001];

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    cin >> N;

    int temp;

    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        arr[i] = temp;
        counting[temp] += 1;
    }

    for (int i = 1; i < 1001; i++)
    {
        prefix[i] = prefix[i - 1] + counting[i];
    }

    for (int i = 0; i < N; i++)
    {
        temp = arr[i];
        answer[i] = prefix[temp] - counting[temp];
        counting[temp] -= 1;
    }

    for (int i = 0; i < N; i++)
    {
        cout << answer[i] << " ";
    }

    return 0;
}
