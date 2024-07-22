#include <iostream>
using namespace std;

int char_count[200002][26];

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	char S[200001];
	int Q;

	cin >> S;
	cin >> Q;
	
	int S_len = 0;
	int j;

	for (int i = 0; i <= 200001; i++)
	{
		S_len = i;

		if (S[i] == NULL) {
			break;
		}

		j = int(S[i]) - int('a');

		char_count[i + 1][j] += 1;
	}

	for (int i = 1; i < S_len + 1; i++)
	{
		for (int j = 0; j < 26; j++)
		{
			char_count[i][j] += char_count[i - 1][j];
		}
	}

	char ai;
	int l, r;

	for (int i = 0; i < Q; i++)
	{
		cin >> ai >> l >> r;

		j = int(ai) - int('a');
		cout << char_count[r + 1][j] - char_count[l][j] << "\n";
	}

	return 0;
}