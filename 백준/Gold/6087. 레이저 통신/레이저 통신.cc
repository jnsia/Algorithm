#include <iostream>
#include <vector>
using namespace std;

#define abs(x) ((x > 0) ? (x) : (-x));

class Node {
public:
	int m;
	int d;
	int x;
	int y;

	Node(int m, int d, int x, int y) {
		this->m = m;
		this->d = d;
		this->x = x;
		this->y = y;
	}

	~Node() {};
};

static void pop_front(vector<Node*> &queue) {
	if (queue.size() > 0) {
		queue.erase(queue.begin());
	}
}

const int MAX = 10001;

int W, H, sx, sy, ex, ey;
char board[101][101];
int visited[100][100][4];

int dx[] = { 1, 0, -1, 0 };
int dy[] = { 0, 1, 0, -1 };

int main(void) {
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);

	cin >> W >> H;

	sx = -1;
	sy = -1;
	ex = -1;
	ey = -1;

	for (int i = 0; i < H; i++)
	{
		cin >> board[i];

		for (int j = 0; j < W; j++)
		{
			if (board[i][j] == 'C') {
				if (sx == -1 && sy == -1) {
					sx = i;
					sy = j;
				}
				else {
					ex = i;
					ey = j;
				}
			}
		}
	}

	for (int i = 0; i < H; i++)
	{
		for (int j = 0; j < W; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				visited[i][j][k] = MAX;
			}
		}
	}

	vector<Node*> queue;

	for (int d = 0; d < 4; d++)
	{
		visited[sx][sy][d] = 0;

		Node* node = new Node(0, d, sx, sy);
		queue.push_back(node);
	}

	while (!queue.empty())
	{
		Node* node = queue.front();
		pop_front(queue);

		for (int i = -1; i <= 1; i++)
		{
			int nm = node->m + abs(i);
			int nd = (node->d + i + 4) % 4;
			int nx = node->x + dx[nd];
			int ny = node->y + dy[nd];

			if (nx >= 0 && nx < H && ny >= 0 && ny < W && board[nx][ny] != '*') {
				if (visited[nx][ny][nd] > nm) {
					visited[nx][ny][nd] = nm;

					Node* node = new Node(nm, nd, nx, ny);
					queue.push_back(node);
				}
			}
		}
	}

	int answer = MAX;

	for (int i = 0; i < 4; i++)
	{
		if (answer > visited[ex][ey][i]) {
			answer = visited[ex][ey][i];
		}
	}

	cout << answer;

    return 0;
}