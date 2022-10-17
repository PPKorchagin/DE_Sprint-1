#include <iostream>
using namespace std;

int main() {
    int x1=0;
    int x2=0;
    cout << "Input the first number: ";
    cin >> x1;

    cout << "Input the second number: ";
    cin >> x2;

    cout << "x1: " << x1 << ", x2: " << x2 << endl;

    if (x1>x2) {
        cout << x1 << ">" << x2;
    }else if (x1<x2) {
        cout << x1 << "<" << x2;
    }else {
        cout << x1 << "=" << x2;
    }

    cout << endl;


    return 0;
}