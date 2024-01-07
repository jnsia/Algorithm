#include <iostream>
using namespace std;

int N, M, A, B, X, Y;
short graph[101][101];
short visited[101];
int queue[101];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    cin >> N;
    cin >> A >> B;
    cin >> M;

    for (int i = 0; i < M; i++)
    {
        cin >> X >> Y;

        graph[X][Y] = 1;
        graph[Y][X] = 1;
    }

    int front = 0;
    int rear = 0;

    queue[rear++] = A;
    visited[A] = 1;

    while (front < rear) {
        int vertex = queue[front++];

        for (int i = 1; i < N + 1; i++)
        {
            if (graph[vertex][i] == 1 && visited[i] == 0) {
                visited[i] = visited[vertex] + 1;
                queue[rear++] = i;
            }
        }
    }

    cout << visited[B] - visited[A];

    return 0;
}