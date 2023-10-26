#include <iostream>
#include <algorithm>
using namespace std;

#define max(x, y) (x) > (y) ? (x) : (y);

int bag[101][100001];
int things[101][2];

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int N, K, W, V;
	cin >> N >> K;

	for (int i = 1; i < N + 1; i++)
	{
		cin >> W >> V;
		
		for (int j = 0; j < K + 1; j++)
		{
			if (W > j)	bag[i][j] = bag[i - 1][j];
			else {
				bag[i][j] = max(bag[i - 1][j], bag[i - 1][j - W] + V);
			}
		}
	}

	/*for (int i = 0; i < N + 1; i++)
	{
		for (int j = 0; j < K + 1; j++)
		{
			cout << bag[i][j] << " ";
		}
		cout << "\n";
	}*/

	cout << bag[N][K];
}