#include <iostream>
using namespace std;

int N, K;
int arr[51];
int answer = 0;

void dfs(int node) {
	short is_leaf = 1;

	if (node == K) {
		return;
	}

	for (int i = 0; i < N; i++)
	{
		if (arr[i] == node && i != K) {
			dfs(i);
			is_leaf = 0;
		}
	}

	if (is_leaf == 1) {
		answer++;
	}
}

int main()
{
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}

	cin >> K;

	for (int i = 0; i < N; i++)
	{
		if (arr[i] == -1) {
			dfs(i);
		}
	}

	cout << answer;
}

