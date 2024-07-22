#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int N, i, j;
	int arr[100001];
	
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}

	sort(arr, arr + N);

	i = 0;
	j = N - 1;
	
	int current_value = arr[j] + arr[i];
	int optimal_value = abs(current_value);
	int optimal_condition[2] = { arr[i], arr[j] };

	while (i < j) {
		current_value = arr[j] + arr[i];

		if (current_value == 0) {
			optimal_condition[0] = arr[i];
			optimal_condition[1] = arr[j];
			break;
		}

		if (abs(current_value) < optimal_value) {
			optimal_value = abs(current_value);
			optimal_condition[0] = arr[i];
			optimal_condition[1] = arr[j];
		}

		if (current_value > 0) {
			j -= 1;
		}
		else {
			i += 1;
		}
	}

	cout << optimal_condition[0] << " " << optimal_condition[1];
}