// default arguments in functions in cpp
#include <iostream>
using namespace std;
// specify default value in func declaration if those value were not passed, you
// should start providing default value from right side of the argc, to specify
// default argc for Nth position you must require default argc for N+1th
// position ( unless it is last argc ), here 2nd and 3rd have default argcs
int multiply(int, int = 1, int = 1);

int main(void) {
    int a, b, c;
    cout << "Enter two numbers to multiply :\n";
    cin >> a >> b;
    cout << "Sum of " << a << " and " << b << " is " << multiply(a, b) << ".\n";
    cout << "It's time  for you to provide us three numbers to multiply "
            ":\n";
    cin >> a >> b >> c;
    cout << "Sum of " << a << " , " << b << " and " << c << " is "
         << multiply(a, b, c) << ".\n";
    return 0;
}

int multiply(int a, int b, int c) { return a * b * c; }