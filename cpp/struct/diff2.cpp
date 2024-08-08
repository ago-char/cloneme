// 2. You can encapsulate all info (variable and functions) related one
// structure while creating struct, in C we could not do so
#include <iostream>
using namespace std;
int main(void) {
    // I am comment
    struct rectangle {
       private:
        float l, b;

       public:
        //    use of constructor
        rectangle() {
            l = 0;
            b = 0;
        }
        void setLenBreadth(float len, float width) {
            l = len;
            b = width;
        }
        // give length of rectangle
        float getLen() {
            if (l > 0 && b > 0) return l;
            cout << "Please Set Data First. Call different Set Functions "
                    "available"
                 << endl;
            exit(EXIT_FAILURE);
        }
        // give width of rectangle
        float getBreadth() {
            if (l > 0 && b > 0) return b;
            cout << "Please Set Data First. Call different Set Functions "
                    "available"
                 << endl;
            exit(EXIT_FAILURE);
        }
        // calculate and return area
        float area() {
            if (l > 0 && b > 0) return l * b;
            cout << "Please Set Data First. Call different Set Functions "
                    "available"
                 << endl;
            exit(EXIT_FAILURE);
        }
        // claculate and return perimeter
        float perimeter() {
            if (l > 0 && b > 0) return 2 * (l + b);
            cout << "Please Set Data First. Call different Set Functions "
                    "available"
                 << endl;
            exit(EXIT_FAILURE);
        }
    };
    // Main code Here
    rectangle r1;
    r1.setLenBreadth(4.5F, 6.7F);
    cout << r1.area() << endl;
    return 0;
}