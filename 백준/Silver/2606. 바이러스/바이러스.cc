#include <iostream>
using namespace std;

class Node {
public:
    int data;
	Node* next;

	Node(int data) {
		this->data = data;
		this->next = NULL;
	};

	~Node() {};
};

class LinkedList {
public:
	Node* head;

	LinkedList() {
		this->head = new Node(-1);
	}
	
	~LinkedList() {};
};

int N, M, s, e;
short visited[101];
LinkedList linkedList[101];

void dfs(int node) {
	visited[node] = 1;

	Node* now = linkedList[node].head;

	while (now->next != NULL) {
		now = now->next;

		if (visited[now->data] == 0) {
			dfs(now->data);
		}
	}
}

int main(void) {
	cin >> N >> M;

	for (int i = 0; i < 101; i++)
	{
		linkedList[i] = LinkedList();
	}

	for (int i = 0; i < M; i++)
	{
		cin >> s >> e;

		Node* s_node = linkedList[s].head;

		while (s_node->next != NULL) {
			s_node = s_node->next;
		}

		s_node->next = new Node(e);

		Node* e_node = linkedList[e].head;

		while (e_node->next != NULL) {
			e_node = e_node->next;
		}

		e_node->next = new Node(s);
	}

	dfs(1);

	int answer = 0;

	for (int i = 2; i < N + 1; i++)
	{
		if (visited[i] == 1) answer++;
	}

	cout << answer;

    return 0;
}