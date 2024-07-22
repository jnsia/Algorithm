#include <iostream>
using namespace std;

int main(void) {
    int X, i, line;
    cin >> X;

    line = 0;
    i = 1;

    while (X > 0) {
        X -= i;
        line += 1;
        i += 1;
    }

    int x, y;

    if (line % 2 == 0) {
        x = line + X;
        y = line + 1 - x;
    }
    else {
        y = line + X;
        x = line + 1 - y;
    }

    cout << x << '/' << y;

    return 0;
}