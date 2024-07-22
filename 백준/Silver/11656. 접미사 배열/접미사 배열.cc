#include <iostream>
#include <algorithm>
using namespace std;

string S;
string temp;
string result[1001];
int result_size = 0;

int main(void) {
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);

	cin >> S;

	temp = "";

	for (int i = 0; i < S.size(); i++)
	{
		temp = "";

		for (int j = i; j < S.size(); j++)
		{
			temp += S[j];
		}

		result[result_size++] = temp;
	}

	sort(result, result + result_size);

	for (int i = 0; i < result_size; i++)
	{
		cout << result[i] << "\n";
	}

    return 0;
}