#include <iostream>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    int N;
    cin >> N;

    for (int i = 1; i < N + 1; i++)
    {
        cout << i << "\n";
    }

    return 0;
}
