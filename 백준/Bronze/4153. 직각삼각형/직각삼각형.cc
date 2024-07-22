#include <iostream>
using namespace std;

int a, b, c;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    while (1) {
        cin >> a >> b >> c;

        if (a + b + c == 0) break;
        
        a = a * a;
        b = b * b;
        c = c * c;

        if (a + b == c || a + c == b || b + c == a) {
            cout << "right" << "\n";
        }
        else {
            cout << "wrong" << "\n";
        }
    }

    return 0;
}
