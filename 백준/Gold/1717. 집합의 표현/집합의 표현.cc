#include <iostream>
using namespace std;

int parent[1000001];

int find_set(int parent[], int x) {
	if (parent[x] == x) {
		return x;
	}

	parent[x] = find_set(parent, parent[x]);
	return parent[x];
}

void union_set(int parent[], int x, int y) {
	x = find_set(parent, x);
	y = find_set(parent, y);

	if (x > y) {
		parent[x] = y;
	}
	else {
		parent[y] = x;
	}
}

int main(void) {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	int N, M;
	cin >> N >> M;

	for (int i = 1; i < N + 1; i++)
	{
		parent[i] = i;
	}

	int cmd, A, B;

	for (int i = 0; i < M; i++)
	{
		cin >> cmd >> A >> B;

		if (cmd == 0) {
			union_set(parent, A, B);
		}
		else {
			cout << (find_set(parent, A) == find_set(parent, B) ? "YES" : "NO") << "\n";
		}
	}


	return 0;
}