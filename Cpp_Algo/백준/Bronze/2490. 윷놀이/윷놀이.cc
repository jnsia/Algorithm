#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    int a, b, c, d;

    for (int i = 0; i < 3; i++)
    {
        cin >> a >> b >> c >> d;

        int result = a + b + c + d;
        
        if (result == 0) {
            cout << "D\n";
        }
        else if (result == 1) {
            cout << "C\n";
        }
        else if (result == 2) {
            cout << "B\n";
        }
        else if (result == 3) {
            cout << "A\n";
        }
        else if (result == 4) {
            cout << "E\n";
        }
    }

    return 0;
}