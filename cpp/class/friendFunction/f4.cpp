// overload unary - using friend function
#include <iostream>
using namespace std;

// imagime there are 2 class, one stores positive num including 0 and the other
// stored negative numbers i.e less than 0
class pos;
class neg;

// class1 is pos
class pos {
    int num;

   public:
    pos(int n = 0) {
        if (n < 0)
            num = -n;
        else
            num = n;
    }
    void setPosNum(pos n) {
        // i am comment
        num = (int)n.num;
    }
    void display() {
        // i am comment
        cout << num;
    }
    // 1. friend function can be friend of one or multiplie class
    friend int operator+(pos, neg);
    friend neg operator-(pos);
    friend pos operator-(neg);
};

// class2 is neg
class neg {
    int num;

   public:
    neg(int n = -1) {
        if (n > 0)
            num = -n;
        else if (!n)  // if n==0
            num = -1;
        else
            num = n;
    }
    void setNegNum(neg n) {
        // i am comment
        num = (int)n.num;
    }
    void display() {
        // i am comment
        cout << num;
    }
    // 1. friend function can be friend of one or multiplie class
    friend int operator+(pos, neg);
    friend neg operator-(pos);
    friend pos operator-(neg);
};

// definition outside class
int operator+(pos n1, neg n2) {
    // return sum of positive and negative number
    return n1.num + n2.num;
}

neg operator-(pos n) {
    neg number;
    number.num = -n.num;
    return number;
}

pos operator-(neg n) {
    pos number;
    number.num = -n.num;
    return number;
}

int main(void) {
    neg n(22);
    pos n1 = -n;
    n.display();
    cout << endl;
    n1.display();
    cout << endl;
    return 0;
}
