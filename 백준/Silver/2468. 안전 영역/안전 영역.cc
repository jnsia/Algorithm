#include <iostream>
using namespace std;

#define max(a, b) (a > b) ? (a) : (b)

int N;
int board[100][100];
short visited[100][100];

int dx[] = { 1, 0, -1, 0 };
int dy[] = { 0, 1, 0, -1 };

void dfs(int x, int y) {
    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx >= 0 and nx < N and ny >= 0 and ny < N and visited[nx][ny] == 0) {
            visited[nx][ny] = 1;
            dfs(nx, ny);
        }
    }
}

int main(void) {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);
    
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++) {
            cin >> board[i][j];
        }
    }

    int answer = 0;

    for (int height = 0; height < 101; height++)
    {
        int result = 0;
        
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (board[i][j] > height) visited[i][j] = 0;
                else visited[i][j] = 1;
            }
        }

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (visited[i][j] == 0) {
                    visited[i][j] = 1;
                    dfs(i, j);
                    result += 1;
                }
            }
        }

        answer = max(answer, result);
    }

    cout << answer;
    
    return 0;
}