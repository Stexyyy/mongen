#include <iostream>
using namespace std;

int mongen();

int main() {
	int room = 1;
	char choice;

	cout << "Bruh text based game" << endl;
	do {
		switch (room) {
		case 1:
			cout << "you're in room 1, you can  go (e)ast. " << endl;
			cin >> choice;
			if (choice == 'e')
				room = 2;
			else
				cout << "Huh???" << endl;
			break;

		case 2:
			cout << "you're in room 2, you can  go (w)est, or (s)outh. " << endl;
			cin >> choice;
			mongen();
			if (choice == 'w')
				room = 1;
			else if (choice == 's')
				room = 3;
			else
				cout << "Huh???" << endl;
			break;

		case 3:
			cout << "you're in room 3, you can (n)orth " << endl;
			cin >> choice;
			if (choice == 'n')
				room = 2;
			else
				cout << "Huh???" << endl;
			break;
		}//end switch
	} while (choice != 'q');

}

// function def
int mongen() {
	int num = rand() % 100;
	if (num < 30) {
		cout << "a zombie appeared!! AAAA" << endl;
		return 10;
	}
	else if (num < 50) {
		cout << "A skeleton appeared!! (I hate skeletons in minecraft so much btw) " << endl;
		return 15;
	}
	else {
		cout << "theres no monsters for now.." << endl;
		return 0;
	}

}
