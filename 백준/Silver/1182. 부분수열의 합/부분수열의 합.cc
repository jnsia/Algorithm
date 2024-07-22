#include <iostream>
using namespace std;

int N, S;
int arr[1000000];
int ans = 0;

void dfs(int idx, int res, int cnt) {
	if (idx == N) {
		if (res == S && cnt > 0) {
			ans++;
		}
		return;
	}

	dfs(idx + 1, res + arr[idx], cnt + 1);
	dfs(idx + 1, res, cnt);
}

int main(void) {

	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);

	cin >> N >> S;

	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}

	dfs(0, 0, 0);

	cout << ans;

    return 0;
}