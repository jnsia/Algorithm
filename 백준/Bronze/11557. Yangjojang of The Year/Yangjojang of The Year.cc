#include <iostream>
using namespace std;

int T, N, L;
string S;

int main(void) {
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);

	cin >> T;

	for (int i = 0; i < T; i++)
	{
		cin >> N;

		int ml = -1;
		string ms;

		for (int i = 0; i < N; i++)
		{
			cin >> S;
			cin >> L;

			if (L > ml) {
				ml = L;
				ms = S;
			}
		}

		cout << ms << "\n";
	}

    return 0;
}