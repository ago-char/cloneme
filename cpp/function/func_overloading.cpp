// let me demonstrate function overloading in cpp
#include <iostream>
using namespace std;

/*
Rules for function overloading:
1. function overloading is defined by arguments of the function and not the
return type meaning that if argcs and name are same but return type is different
then it is not overloading it yeilds ERROR

2. while matching compiler looks for exact match, if not found:
    i.) after match in No. of args, it converts actual argument to meet the
requirement of formal argument via implicit conversion i.e. char, unsigned char,
short to int; float to double ii.) if implicit conversion does not works or do
the job, it does standard conversion where any data type could be convert to any
if they can be converted
*/

float area(float);  // area of Square you need to give 'R' as float value
int area(int);
float area(float, float);  // area of rectangle

int main(void) {
    cout << "Area : " << area(2.5F) << endl;
    // cout << "Area : " << area(2.5) << endl; ERROR 1 see below
    // area("sagar"); ERROR 2 see below
    return 0;
}

float area(float R) { return 3.14F * R * R; }
int area(int R) { return 3.14 * R * R; }

/*
Note: Case of ERROR:
1. more than one instances of overloaded function 'func' matches arguments list
for ex: in this code "area(2.5)" will match both instance of area func as such :
float area(float) and int area(int). Why is that? as argument is 2.5 it should
match to float ?
==> Yes but when compiler sees argc list it says
i) it's ok 2.5 is float lets match with float area(float)
ii) but, oh 2.5 with standard conversion can be converted to int as 2 to match
int float(int) As i and ii argues, compiler Raised the ERROR no.1

2. when type can not be converted even with standard conversion compiler raises
error as: "no instance of overloaded function 'fun' matches the argc list"
foreg: if you call area as "area("String")" it will raise this ERROR because
argument passed to area i.e "String" is char* type or array of character type
with can not be converted either to 'int' to match "int area(int)" or to 'float'
to match "float area(float)"
*/