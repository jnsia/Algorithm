#include <iostream>
using namespace std;

int N;
int arr[100000];
int stack[100000];
char answer[200000];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    int size = 0;
    int idx = 0;
    int cnt = 0;

    for (int i = 1; i < N + 1; i++)
    {
        while (size > 0 && stack[size - 1] == arr[idx]) {
            stack[size - 1] = 0;
            size--;
            idx++;
            answer[cnt++] = '-';
        }

        stack[size++] = i;
        answer[cnt++] = '+';
    }

    while (size > 0 && stack[size - 1] == arr[idx]) {
        stack[size - 1] = 0;
        size--;
        idx++;
        answer[cnt++] = '-';
    }

    if (size > 0) {
        cout << "NO";
    }
    else {
        for (int i = 0; i < cnt; i++)
        {
            cout << answer[i] << "\n";
        }
    }

    return 0;
}