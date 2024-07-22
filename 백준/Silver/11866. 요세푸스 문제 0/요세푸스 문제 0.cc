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

int arr[1000];

int main(void) {
	int N, K;
	cin >> N >> K;

	Queue queue;

	for (int i = 1; i < N + 1; i++)
	{
		queue.enqueue(i);
	}

	int answer;
	int idx = 0;

	cout << '<';

	while (!queue.isEmpty()) {
		for (int i = 1; i < K; i++)
		{
			queue.dequeue(answer);
			queue.enqueue(answer);
		}

		queue.dequeue(answer);
		arr[idx++] = answer;
	}

	for (int i = 0; i < idx; i++)
	{
		if (i == idx - 1) {
			cout << arr[i];
			break;
		}

		cout << arr[i] << ", ";
	}

	cout << '>';

	return 0;
}