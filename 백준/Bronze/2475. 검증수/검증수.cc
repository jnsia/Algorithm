#include <iostream>
using namespace std;

int main(void) {
    int temp;
    int answer = 0;
    
    for (int i = 0; i < 5; i++)
    {
        cin >> temp;
        answer += temp * temp;
    }

    cout << answer % 10;
    
    return 0;
}