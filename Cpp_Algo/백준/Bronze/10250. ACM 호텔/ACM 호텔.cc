#include <iostream>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    int T, H, W, N;
    cin >> T;

    for (int tc = 0; tc < T; tc++)
    {
        cin >> H >> W >> N;

        int h = N % H;
        int w = N / H + 1;

        if (h == 0) {
            h += H;
            w -= 1;
        };

        if (w < 10) {
            cout << h << "0" << w << "\n";
        }
        else {
            cout << h << w << "\n";
        }
    }

    return 0;
}
