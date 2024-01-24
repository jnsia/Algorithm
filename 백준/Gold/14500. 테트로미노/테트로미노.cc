#include <iostream>
using namespace std;

#define max(a, b) (a > b) ? (a) : (b)

int N, M, ans;
int board[500][500];
short visited[500][500];

int dx[] = { 1, 0, -1, 0 };
int dy[] = { 0, 1, 0, -1 };

void dfs(int x, int y, int move, int res) {
    if (move == 3) {
        ans = max(ans, res);
        return;
    }

    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 || nx >= N || ny < 0 || ny >= M || visited[nx][ny] == 1) continue;

        if (move == 1) {
            visited[nx][ny] = 1;
            dfs(x, y, move + 1, res + board[nx][ny]);
            visited[nx][ny] = 0;
        }

        visited[nx][ny] = 1;
        dfs(nx, ny, move + 1, res + board[nx][ny]);
        visited[nx][ny] = 0;
    }
}

int main(void) {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);
    
    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++) {
            cin >> board[i][j];
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++) {
            visited[i][j] = 1;
            dfs(i, j, 0, board[i][j]);
            visited[i][j] = 0;
        }
    }
    
    cout << ans;

    return 0;
}