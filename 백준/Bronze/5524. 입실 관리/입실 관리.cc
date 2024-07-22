#include <iostream>
using namespace std;

int N;
char name[21];

int main(void) {
    cin >> N;

    for (int j = 0; j < N; j++)
    {
        cin >> name;

        for (int i = 0; i < 21; i++)
        {
            if (name[i] == NULL) break;

            if (name[i] <= 'Z') cout << char(name[i] - 'A' + 'a');
            else cout << name[i];
        }

        cout << "\n";
    }

    return 0;
}