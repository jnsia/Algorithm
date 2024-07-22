#include <iostream>
#include <cmath>
using namespace std;

#define min(a, b) (a) > (b) ? (b) : (a)
#define max(a, b) (a) > (b) ? (a) : (b)

int min_tree[1000000];
int max_tree[1000000];

int max_value, min_value;

int find(int start, int end, int node, int left, int right) {
	if ((start > right) || (end < left)) {
		return 0;
	}

	if ((start <= left) && (end >= right)) {
		min_value = min(min_value, min_tree[node]);
		max_value = max(max_value, max_tree[node]);
		return 0;
	}

	int mid = (left + right) / 2;
	find(start, end, node * 2, left, mid);
	find(start, end, node * 2 + 1, mid + 1, right);

	return 0;
}

int power_2(int times) {
	int result = 1;

	while (times > 0) {
		result *= 2;
		times -= 1;
	}

	return result;
}

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int N, M, temp, a, b;
	cin >> N >> M;
	
	int log = ceil(log2(N));
	int size = power_2(log);

	for (int i = 0; i < size * 2; i++)
	{
		min_tree[i] = 1000000001;
	}

	for (int i = 0; i < N; i++)
	{
		cin >> temp;
		
		min_tree[i + size] = temp;
		max_tree[i + size] = temp;

		int cur_i = i + size;

		while (cur_i > 0) {
			cur_i /= 2;
			min_tree[cur_i] = min(min_tree[cur_i * 2], min_tree[cur_i * 2 + 1]);
			max_tree[cur_i] = max(max_tree[cur_i * 2], max_tree[cur_i * 2 + 1]);
		}
	}

	for (int i = 0; i < M; i++)
	{
		max_value = 0;
		min_value = 10000000001;

		cin >> a >> b;
		find(a, b, 1, 1, size);

		cout << min_value << " " << max_value << "\n";
	}
}