#include <iostream>
using namespace std;

class Node {
public:
	int data;
	Node* prev;

	Node(int x) {
		data = x;
		prev = NULL;
	}
};

class Stack {
public:
	int size;
	Node* top;

	Stack() {
		size = 0;
		top = NULL;
	}

	void push(int x) {
		Node* node = new Node(x);

		if (size == 0) {
			top = node;
		}
		else {
			node->prev = top;
			top = node;
		}

		size++;
	}

	void pop() {
		if (size == 0) {
			cout << "-1\n";
			return;
		}

		Node* temp = top;
		size--;

		if (size == 0) {
			top = NULL;
		}
		else {
			top = top->prev;
		}

		cout << temp->data << "\n";
		temp == NULL;
	}

	void length() {
		cout << size << "\n";
	}

	void empty() {
		if (size == 0) cout << 1 << "\n";
		else cout << 0 << "\n";
	}

	void peek() {
		if (size == 0) cout << -1 << "\n";
		else cout << top->data << "\n";
	}
};

char cmd[6];

int main(void) {

	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);

	int N, X;
	cin >> N;

	Stack stack = Stack();

	for (int i = 0; i < N; i++)
	{
		cin >> cmd;
		
		if (cmd[0] == 'p') {
			if (cmd[1] == 'u') {
				cin >> X;
				stack.push(X);
			}
			else stack.pop();
		}
		else if (cmd[0] == 's') stack.length();
		else if (cmd[0] == 'e') stack.empty();
		else stack.peek();
	}

    return 0;
}