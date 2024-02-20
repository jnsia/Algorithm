#include <iostream>
#include <algorithm>
using namespace std;

int N;
int A[51];
int B[51];

int main()
{
	cin.tie(0);
	cout.tie(0);
	iostream::sync_with_stdio(false);

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> A[i];
	}

	for (int i = 0; i < N; i++)
	{
		cin >> B[i];
	}

	sort(A, A + N);
	sort(B, B + N);

	int answer = 0;

	for (int i = 0; i < N; i++)
	{
		answer += A[i] * B[N - i - 1];
	}

	cout << answer;
}
