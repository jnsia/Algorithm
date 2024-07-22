#include <iostream>
using namespace std;

char DNA[1000001];
int min_num[4];
int counts[4];

int check_sequence() {
    int result = 1;

    for (int i = 0; i < 4; i++)
    {
        if (min_num[i] > counts[i]) {
            result = 0;
            break;
        }
    }

    return result;
}

int check_base(char base) {
    if (base == 'A') return 0;
    else if (base == 'C') return 1;
    else if (base == 'G') return 2;
    else return 3;
}

int main()
{
    int S_len, P_len, temp;
    cin >> S_len >> P_len;
    cin >> DNA;

    // A C G T
    for (int i = 0; i < 4; i++)
    {
        cin >> min_num[i];
    }

    char ACGT[4] = { 'A', 'C', 'G', 'T' };

    for (int i = 0; i < P_len; i++)
    {
        temp = check_base(DNA[i]);
        counts[temp] += 1;
    }

    int answer = 0;

    if (check_sequence() == 1) {
        answer += 1;
    }
     
    for (int i = 0; i < S_len - P_len; i++)
    {
        temp = check_base(DNA[i]);
        counts[temp] -= 1;
        temp = check_base(DNA[i + P_len]);
        counts[temp] += 1;

        if (check_sequence() == 1) {
            answer += 1;
        }
    }

    cout << answer;

    return 0;
}
