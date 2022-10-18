#include <iostream>
#include <string>
using namespace std;

int main() {
    string line;
    cout << "input a numbers separated by space: ";
    getline(cin, line);

    int max=-1;
    int pos;
    while ((pos=line.find(" "))!=std::string::npos) {
//        cout << "'" << line.substr(0,pos) << "'" << endl;
        int n=stoi(line.substr(0,pos));
        if (n>max) {
            max=n;
        }

        line = line.substr(pos+1,line.length()-pos);
    }

    try {
    int n=stoi(line);
    if (n>max) {
        max=n;
    }

    }
    catch (std::invalid_argument &err) {
    }

    cout << max << endl;


    return 0;
}