#include <iostream>
#include <algorithm>
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

class Queue {
public:
	Node* front;
	Node* rear;
	int size;

	Queue() {
		this->front = NULL;
		this->rear = NULL;
		this->size = 0;
	}

	void enqueue(int data) {
		Node* node = new Node(data);
		
		if (size == 0) {
			this->front = node;
		}
		else {
			this->rear->next = node;
		}

		this->rear = node;
		this->size++;
	}

	void dequeue() {
		if (size == 0) {
			cout << -1 << "\n";
			return;
		}

		Node* temp = this->front;
		this->size--;

		if (size == 0) {
			this->front = NULL;
		}
		else {
			this->front = this->front->next;
		}

		cout << temp->data << "\n";
		temp = NULL;
	}

	void qsize() {
		cout << this->size << "\n";
	}

	void empty() {
		if (size == 0) cout << 1 << "\n";
		else cout << 0 << "\n";
	}

	void notback() {
		if (size == 0) cout << -1 << "\n";
		else cout << this->front->data << "\n";
	}

	void back() {
		if (size == 0) cout << -1 << "\n";
		else cout << this->rear->data << "\n";
	}
};

char cmd[6];

int main(void) {

	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);

	int N, X;
	cin >> N;

	Queue queue = Queue();

	for (int i = 0; i < N; i++)
	{
		cin >> cmd;

		if (cmd[0] == 'p') {
			if (cmd[1] == 'u') {
				cin >> X;
				queue.enqueue(X);
			}
			else {
				queue.dequeue();
			}
		}
		else if (cmd[0] == 's') {
			queue.qsize();
		}
		else if (cmd[0] == 'e') {
			queue.empty();
		}
		else if (cmd[0] == 'f') {
			queue.notback();
		}
		else {
			queue.back();
		}
	}

    return 0;
}