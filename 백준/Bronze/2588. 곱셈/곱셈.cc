#include <iostream>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    int c = a * b;
    while (b >= 1) {
        cout << a * (b % 10) << endl;
        b = b / 10;
    }
    cout << c;
}