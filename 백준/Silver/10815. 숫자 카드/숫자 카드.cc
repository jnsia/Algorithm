#include <iostream>
#include <algorithm>
using namespace std;

int binary_search(int cards[], int low, int high, int key) {
	int mid;
	
	while (low <= high) {
		mid = (low + high) / 2;

		if (cards[mid] == key) return 1;
		else if (cards[mid] > key) high = mid - 1;
		else low = mid + 1;
	}
	
	return 0;
}

int cards[500000];

int main(void) {

	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);

	int N, M, key;
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> cards[i];
	}

	sort(cards, cards + N);

	cin >> M;

	for (int i = 0; i < M; i++)
	{
		cin >> key;
		cout << binary_search(cards, 0, N - 1, key) << " ";
	}

    return 0;
}