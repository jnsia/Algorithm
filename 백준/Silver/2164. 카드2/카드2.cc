#include <iostream>
using namespace std;

struct Node {
	int data;
	Node* next;
};

class Queue {
private:
	Node* front;
	Node* rear;

public:
	Queue() {
		front = NULL;
		rear = NULL;
	}

	~Queue() {}

	void enqueue(int data) {
		Node* newNode;
		newNode = new Node;
		newNode->data = data;
		newNode->next = NULL;

		if (front == NULL) {
			front = newNode;
		} else {
			rear->next = newNode;
		}

		rear = newNode;
	}

	void dequeue(int& answer) {
		Node* temp;
		temp = front;
		front = front->next;

		if (front == NULL) {
			rear = NULL;
		}

		answer = temp->data;
		delete temp;
	}

	bool isEmpty() {
		return (front == NULL);
	}
};

int main(void) {
	int N;
	cin >> N;

	Queue queue;

	for (int i = 1; i < N + 1; i++)
	{
		queue.enqueue(i);
	}

	int answer;

	while (!queue.isEmpty()) {
		queue.dequeue(answer);

		if (!queue.isEmpty()) {
			queue.dequeue(answer);
			queue.enqueue(answer);
		}
	}

	cout << answer;

	return 0;
}