#include <iostream>
using namespace std;

struct Node {
	int data;
	Node* prev;
};

class Stack {
private:
	Node* top;

public:
	Stack() { 
		top = NULL;
	}

	~Stack() {}

	void enq(int data) {
		Node* newNode;
		newNode = new Node;
		newNode->data = data;
		newNode->prev = NULL;

		if (top == NULL) {
			top = newNode;
		}
		else {
			Node* temp;
			temp = top;

			while (temp->prev != NULL) {
				temp = temp->prev;
			}

			temp->prev = newNode;
		}
	}

	void push(int data) {
		Node* newNode;
		newNode = new Node;
		newNode->data = data;

		if (top == NULL) {
			newNode->prev = NULL;
			top = newNode;
		}
		else {
			newNode->prev = top;
			top = newNode;
		}
	}

	void pop() {
		Node* temp;
		temp = top;
		top = top->prev;
		delete temp;
	}

	int peek() {
		if (isEmpty()) {
			return 30000;
		}

		return top->data;
	}

	bool isEmpty() {
		return (top == NULL);
	}
};

int main(void) {
	int N, num;
	cin >> N;

	Stack stack;
	Stack waitStack;

	for (int i = 0; i < N; i++)
	{
		cin >> num;
		stack.enq(num);
	}

	int order = 1;
	int temp1, temp2;

	while (!stack.isEmpty() || !waitStack.isEmpty()) {
		temp1 = stack.peek();
		temp2 = waitStack.peek();

		if (temp1 < temp2) {
			stack.pop();

			if (order == temp1) {
				order++;
			}
			else {
				waitStack.push(temp1);
			}
		}
		else {
			waitStack.pop();

			if (order == temp2) {
				order++;
			}
			else {
				break;
			}
		}
	}

	if (order == N + 1) {
		cout << "Nice";
	}
	else {
		cout << "Sad";
	}

	return 0;
}