#include <iostream>
using namespace std;

#define min(x, y) ((x > y) ? (y) : (x))

int main(void) {
    int X, Y, W, H, a, b;
    cin >> X >> Y >> W >> H;

    a = min(X, Y);
    b = min((W - X), (H - Y));

    cout << min(a, b);

    return 0;
}