#include <iostream>
using namespace std;

const int MAX = 1000001;

int F, S, G, U, D;
int visited[MAX];
int queue[MAX];

int main() {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

    int front = 0;
    int rear = 0;

    int now;

    cin >> F >> S >> G >> U >> D;

    for (int i = 0; i < MAX; i++)
    {
        visited[i] = MAX;
    }

    visited[S] = 0;
    queue[rear++] = S;
    
    while (front != rear) {
        now = queue[front++];

        if (now + U < F + 1 && visited[now + U] == MAX) {
            queue[rear++] = now + U;
            visited[now + U] = visited[now] + 1;
        }

        if (now - D > 0 && visited[now - D] == MAX) {
            queue[rear++] = now - D;
            visited[now - D] = visited[now] + 1;
        }
    }

    if (visited[G] == MAX) {
        cout << "use the stairs";
    }
    else {
        cout << visited[G];
    }

    return 0;
}
