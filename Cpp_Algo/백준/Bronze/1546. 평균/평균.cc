#include <iostream>
using namespace std;

int main(void) {
	float N, score, max_score, total_score;
	float scores[1001];

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		scores[i] = 0;
	}

	max_score = -1;
	total_score = 0;

	for (int i = 0; i < N; i++) {
		cin >> score;
		total_score += score;
		scores[i] = score;

		if (max_score < score) max_score = score;
	}

	cout << (total_score * 100) / N / max_score;
}