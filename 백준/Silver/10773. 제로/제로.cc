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

	void push(int data, int& sum) {
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

		sum += data;
	}

	void pop(int& sum) {
		Node* temp;
		temp = top;
		top = top->prev;
		sum -= temp->data;
		delete temp;
	}
};

int main(void) {
	int K, temp;
	cin >> K;

	Stack stack;
	int sum = 0;

	for (int i = 0; i < K; i++)
	{
		cin >> temp;

		if (temp == 0) stack.pop(sum);
		else stack.push(temp, sum);
	}

	cout << sum;

	return 0;
}