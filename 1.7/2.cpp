#include <iostream>
using namespace std;

int main() {
    int x1;
    cout << "Input the year: ";
    cin >> x1;

    cout << ((x1%4==0)?"yes":"no") << endl;

    return 0;
}