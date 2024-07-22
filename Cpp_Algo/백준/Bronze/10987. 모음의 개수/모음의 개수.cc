#include <iostream>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    char input[101];
    cin >> input;

    int answer = 0;

    for (int i = 0; i < 101; i++)
    {
        if (input[i] == NULL) break;

        if (input[i] == 'a' || input[i] == 'e' || input[i] == 'i' || input[i] == 'o' || input[i] == 'u') answer++;
    }

    cout << answer;

    return 0;
}
