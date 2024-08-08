// overload + using friend func
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
};

// definition outside class
int operator+(pos n1, neg n2) {
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
    cout << "\nSum is " << operator+(N1, N2) << endl;
    pos N3(40);
    neg N4(-55);
    N3.display();
    cout << endl;
    N4.display();
    // here operator+ can be called just by +, but first argc will be of left
    // and second argc will be of right side so be aware of that
    cout << "\nSum is " << N3 + N4 << endl;
    return 0;
}
