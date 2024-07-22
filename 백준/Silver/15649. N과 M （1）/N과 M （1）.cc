#include <iostream>
using namespace std;

int N, M;
int arr[9];
int collected[9];

static void dfs(int depth) {
	if (depth == M) {
		for (int i = 0; i < M; i++)
		{
			cout << arr[i] << " ";
		}
		cout << "\n";
	}


	for (int i = 1; i < N + 1; i++)
	{
		if (collected[i] == 0) {
			collected[i] = 1;
			arr[depth] = i;
			dfs(depth + 1);
			collected[i] = 0;
		}
	}
}

int main()
{
	cin >> N >> M;

	dfs(0);
}

