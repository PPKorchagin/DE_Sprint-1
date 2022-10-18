#include <iostream>
using namespace std;

int main() {
    int x1;
    cout << "Input the number: ";
    cin >> x1;

    cout << ((x1%2==0)?"even":"odd") << endl;

    return 0;
}