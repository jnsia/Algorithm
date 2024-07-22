#include <iostream>
using namespace std;

int findIndex(char colors[][7], char str[]) {
    int index = -1;

    for (int i = 0; i < 10; i++)
    {
        if (index > -1) break;

        for (int j = 0; j < 7; j++) {
            if (colors[i][j] == NULL) {
                index = i;
                break;
            }

            if (str[j] == NULL) break;

            if (colors[i][j] != str[j]) break;
        }
    }
    
    return index;
}

int power(int times) {
    long long int res = 1;

    for (int i = 0; i < times; i++)
    {
        res *= 10;
    }

    return res;
}

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    char colors[10][7] = {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};
    char first[7], second[7], third[7];
    cin >> first >> second >> third;

    long long int one, two, three;

    one = findIndex(colors, first);
    two = findIndex(colors, second);
    three = findIndex(colors, third);

    cout << (one * 10 + two) * power(three);
    
    return 0;
}
