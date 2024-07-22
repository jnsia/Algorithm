#include <iostream>
using namespace std;

int keys[8];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    for (int i = 1; i <= 8; i++)
    {
        cin >> keys[i - 1];
    }

    short is_mixed = 0;

    if (keys[0] == 1) {
        for (int i = 0; i < 7; i++)
        {
            if (keys[i + 1] < keys[i]) {
                is_mixed = 1;
                break;
            }
        }
    }
    else if (keys[0] == 8)  {
        for (int i = 0; i < 7; i++)
        {
            if (keys[i + 1] > keys[i]) {
                is_mixed = 1;
                break;
            }
        }
    }
    else {
        is_mixed = 1;
    }

    if (is_mixed == 1) {
        cout << "mixed";
    }
    else {
        if (keys[0] == 1) cout << "ascending";
        else cout << "descending";
    }

    return 0;
}
