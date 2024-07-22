#include <iostream>
using namespace std;

short is_primes[4000001];
long long int primes[4000001];

int main(void) {
	int N;
	cin >> N;

	is_primes[1] = 1;

	for (int i = 2; i <= N; i++)
	{
		if (is_primes[i] == 0) {
			for (int k = i + i; k <= N; k += i)
			{
				is_primes[k] = 1;
			}
		}
	}

	int size = 1;

	for (int i = 1; i <= N; i++)
	{
		if (is_primes[i] == 0) {
			primes[size] = i;
			primes[size] += primes[size - 1];
			size++;
		}
	}

	int left = 0;
	int right = 1;
	int sum = 0;
	int answer = 0;

	while (left < right && right <= size) {
		sum = primes[right] - primes[left];
		
		if (sum == N) {
			answer++;
			right++;
		}
		else if (sum > N) {
			left++;
		}
		else {
			right++;
		}
	}
	
	cout << answer;

    return 0;
}