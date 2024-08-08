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
    friend int add(pos, neg);
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
    friend int add(pos, neg);
};

// definition outside class
int add(pos n1, neg n2) {
    // return sum of positive and negative number
    return n1.num + n2.num;
}

int main(void) {
    // i am comment
    pos N1;
    N1.setPosNum(-2);
    neg N2;
    N2.setNegNum(-22);
    cout << "N1 is ";
    N1.display();
    cout << "\nN2 is ";
    N2.display();
    cout << "\nSum is " << add(N1, N2) << endl;
    return 0;
}
