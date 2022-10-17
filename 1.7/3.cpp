//Правда, сделал только для случая, когда коэффициенты при исках целочисленные
#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;
using std::string;

int a2=0;
int a1=0;
int a0=0;

bool isdig(string str){
    int i;
    for (i=0;i<str.length();i++){
        if (!isdigit(str[i])) {
            //cout << "power " << str << " is not number, exiting" << endl;
            return false;
        }
    }
    return true;
}


int process_part(int sign, string part) {
    cout<< "process " << sign << "*" << part  << endl;
    int tpos;

    // if part is const
    if (part.find("x")==std::string::npos) {
            int i;
            if (!isdig(part)) {
                cout << part << " is not number, exiting" << endl;
                return 1;
            }
            a0+=sign*stoi(part);
//            cout << stoi(part) << endl;
    }
    else if ((tpos=part.find("^"))!=std::string::npos) {
        string spow=part.substr(tpos+1,part.length()-1);
//        cout << "power " << spow << endl;
        if (spow.length()==0) {
            cout << "power should not be empty" << endl;
            return 1;
        }
        int i;
        if (!isdig(spow)) {
            cout << "power " << spow << " is not number, exiting" << endl;
            return 1;
        }

        int pow = stoi(spow);

        if (pow>2) {
            cout << "power " << pow << " should be >=0 and <=2" << endl;
            return 1;
        }

        string sfirst=part.substr(0,tpos);

        if (sfirst[sfirst.length()-1]!='x') {
            cout << sfirst << " should be end with x" << endl;
            return 1;
        }

        sfirst=sfirst.substr(0,sfirst.length()-1);


        if (!isdig(sfirst)) {
            cout << "coeff " << sfirst << " is not number, exiting" << endl;
            return 1;
        }

        int coeff=stoi(sfirst);

        switch (pow) {
            case 0:
                a0+=sign*coeff;
                break;
            case 1:
                a1+=sign*coeff;
                break;
            default:
                a2+=sign*coeff;
                break;
        }
    } else {
        if (part[part.length()-1]!='x') {
                cout << part << " should be end with x" << endl;
                return 1;
        }

        string sfirst=part.substr(0,part.length()-1);

        if (!isdig(sfirst)) {
            cout << "coeff " << sfirst << " is not number, exiting" << endl;
            return 1;
        }

        int coeff=stoi(sfirst);

        a1+=sign*coeff;

    }

    return 0;
}

int main() {
    string eq;
    cout << "Input the equation with form '34x^2+41x-10=0': ";
//    getline(cin, eq);
    eq="34x^2+5+41x-10-10x^2-1x+2x^0-3x^1=0";
    //eq="2x^2+5x-3=0";
    //eq="4x^2+21x+5=0";

    if (eq.substr(eq.length()-2,2)!="=0") {
        cout << "wrong equation, it should be ends with =0" << endl;
        return 1;
    }

    eq=eq.substr(0,eq.length()-2);

    cout << eq << endl;

    int pos;
    char last_sign='+';
//    bool c=true;
    while (true) {
        int posp=eq.find("+");
        int posm=eq.find("-");
        if (posp==std::string::npos && posm==std::string::npos) {
            break;
        }else if (posp==std::string::npos) {
            pos=posm;
        }else if (posm==std::string::npos) {
            pos=posp;
        } else {
            if (posm>posp) {
                pos=posp;
            }else {
                pos=posm;
            }
        }

        string sub=eq.substr(0,pos);
        if (process_part((last_sign=='-')?-1:1,sub)!=0){
            return 1;
        }

        last_sign=eq[pos];
        eq.erase(0, pos + 1);
    }
    if (process_part((last_sign=='-')?-1:1,eq)!=0) {
        return 1;
    }


    cout << a2 << "x^2" << (a1>0?"+":"") << a1  << "x"<< (a0>0?"+":"") << a0 << "=0" << endl;

    int odisc=a1*a1-4*a0*a2;
    if (odisc<0) {
        cout << "no roots" << endl;
    }else {
        float x1=(-a1+sqrt(odisc))/(2*a2);
        float x2=(-a1-sqrt(odisc))/(2*a2);

        cout << "x1=" << x1 << ", x2=" << x2 << endl;
    }
    return 0;


}