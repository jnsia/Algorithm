#include <iostream>
using namespace std;

char lectures[20][51];
double scores[20];
char grades[20][3];

int main(void) {
	double total_score = 0;
	double scored_lecture_num = 0;

	for (int i = 0; i < 20; i++)
	{
		cin >> lectures[i];
		cin >> scores[i];
		cin >> grades[i];
	}

	double score;
	char tc;

	for (int i = 0; i < 20; i++)
	{
		tc = grades[i][0];
		
		if (tc == 'P') continue;

		if (tc == 'F') { 
			scored_lecture_num += scores[i];
			continue;
		};
		
		if (tc == 'A') {
			score = 4;
		}
		else if (tc == 'B') {
			score = 3;
		}
		else if (tc == 'C') {
			score = 2;
		}
		else {
			score = 1;
		}

		if (grades[i][1] == '+') {
			score += 0.5;
		}

		total_score += score * scores[i];
		scored_lecture_num += scores[i];
	}

	cout << total_score / scored_lecture_num;

	return 0;
}