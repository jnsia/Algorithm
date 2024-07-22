#include <iostream>
using namespace std;

int T, cnt, len;
char S[1001];

int recursion(int l, int r) {
	cnt++;

	if (l >= r) return 1;
	else if (S[l] != S[r]) return 0;
	else return recursion(l + 1, r - 1);
}

int main()
{
	cin.tie(0);
	cout.tie(0);
	iostream::sync_with_stdio(false);

	cin >> T;

	for (int i = 0; i < T; i++)
	{
		cin >> S;
	
		cnt = 0;
		len = 0;

		for (int j = 0; j < 1001; j++)
		{
			if (S[j] == NULL) break;
			len = j;
		}

		cout << recursion(0, len) << " " << cnt << "\n";
	}
}
