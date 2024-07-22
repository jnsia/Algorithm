#include <iostream>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    int T, c, v;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        cin >> c >> v;

        printf("You get %d piece(s) and your dad gets %d piece(s).\n", c / v, c % v);
    }

    return 0;
}
