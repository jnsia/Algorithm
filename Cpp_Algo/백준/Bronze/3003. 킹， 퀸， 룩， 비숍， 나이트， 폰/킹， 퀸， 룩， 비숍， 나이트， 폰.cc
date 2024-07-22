#include <iostream>
using namespace std;

int main(void) {
	int need_piece[6] = { 1, 1, 2, 2, 2, 8 };
	int temp;

	for (int i = 0; i < 6; i++)
	{
		cin >> temp;
		need_piece[i] -= temp;
		cout << need_piece[i] << " ";
	}
}