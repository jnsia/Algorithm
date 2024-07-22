#include <iostream>
using namespace std;

int N;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    cin >> N;

    int answer = 0;

    for (int i = 1; i < N + 1; i++)
    {
        int num = i;
        while (num > 0 && num % 5 == 0) {
            answer += 1;
            num /= 5;
        }
    }
    
    cout << answer;

    return 0;
}
