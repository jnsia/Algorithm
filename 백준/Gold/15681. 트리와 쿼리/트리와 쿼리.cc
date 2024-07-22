#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int data) {
        this->data = data;
        this->next = NULL;
    }
};

class LinkedList {
public:
    Node* start;
    Node* end;

    LinkedList() {
        this->start = NULL;
        this->end = NULL;
    }

    void append(int data) {
        Node* node = new Node(data);

        if (this->start == NULL) {
            this->end = node;
            this->start = this->end;
        }
        else {
            this->end->next = node;
            this->end = this->end->next;
        }
    }
};

class Queue {
public:
    int size;
    Node* front;
    Node* rear;

    Queue() {
        this->size = 0;
        this->front = NULL;
        this->rear = NULL;
    }

    int is_empty() {
        return this->size == 0 ? true : false;
    }

    void enqueue(int data) {
        Node* node = new Node(data);
        
        if (is_empty()) {
            this->rear = node;
            this->front = this->rear;
        }
        else {
            this->rear->next = node;
            this->rear = this->rear->next;
        }

        this->size++;
    }

    int dequeue() {
        int result = this->front->data;

        if (this->size == 1) {
            this->front = NULL;
            this->rear = NULL;
        }
        else {
            Node* temp = this->front->next;
            this->front = temp;
        }

        this->size--;

        return result;
    }
};

int dfs(int node, int visited[], int answer[], LinkedList* graph[]) {
    visited[node] = 1;
    Node* now_node = graph[node]->start;
    int result = 1;

    while (now_node != NULL) {
        if (visited[now_node->data] == 0) {
            result += dfs(now_node->data, visited, answer, graph);
        }
        now_node = now_node->next;
    }

    answer[node] = result;
    return result;
}

int N, R, Q;
int visited[100001];
int answer[100001];
LinkedList* graph[100001];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    cin >> N >> R >> Q;

    for (int i = 1; i < N + 1; i++)
    {
        Node* node = new Node(i);
        graph[i] = new LinkedList();
    }

    int u, v;

    for (int i = 0; i < N - 1; i++)
    {
        cin >> u >> v;

        graph[u]->append(v);
        graph[v]->append(u);
    }

    dfs(R, visited, answer, graph);

    for (int i = 0; i < Q; i++)
    {
        cin >> u;
        cout << answer[u] << "\n";
    }

    return 0;
}
