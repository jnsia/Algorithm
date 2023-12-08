#include <iostream>
using namespace std;

char number[6];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    while (1) {
        cin >> number;

        if (number[0] == '0') {
            break;
        }

        int length = 0;

        for (int i = 0; i < 6; i++)
        {
            if (number[i] == NULL) break;
            length = i;
        }

        int mid = (length + 1) / 2;
        short is_pal = 1;
        
        for (int i = 0; i < mid; i++) {
            if (number[i] != number[length - i]) {
                is_pal = 0;
                break;
            }
        }

        if (is_pal == 1) cout << "yes" << "\n";
        else cout << "no" << "\n";
    }

    return 0;
}
