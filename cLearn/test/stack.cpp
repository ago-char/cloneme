#include <iostream>
using namespace std;
#define SIZE 5  // for definite size stack
class stack {
    int item, pointer, size;
    int* arr;

   public:
    int createStack(int siz) {
        if (siz > 0) {
            arr = (int*)malloc(siz);
            pointer = -1;
            size = siz;
            if (arr) return 1;
            return 0;
        }
    }
    // return 1 on success, 0 on stack full
    int push(int element) {
        if (pointer < size) {
            arr[++pointer] = element;
            return 1;
        }
        return 0;
    }
    int isEmpty() {
        if (pointer == -1) return 1;
        return 0;
    }
    int isFull() {
        if (pointer == size) return 1;
        return 0;
    }
    int pop() {
        // always check pointer if returned value is less than 0, better way is
        // to pop only after checking if stack is not empty
        if (pointer > -1) {
            // int item = arr[pointer];
            // pointer--;
            // return item;
            return arr[pointer--];
        }
        return pointer;
    }
    int getPointer() { return pointer; }
};

int main(void) {
    stack s1;
    cout << s1.createStack(SIZE) << endl;
    int array[SIZE] = {1, 7, 8, 334, 54};
    int i = 0;
    while (i < SIZE) {
        s1.push(array[i++]);
    }
    i = 0;
    cout << "\n.....................\n";
    while (i++ < SIZE + 1) {
        if (s1.getPointer() >= 0 || !s1.isEmpty())
            cout << s1.pop() << endl;
        else {
            cout << "Pointer at Negative Index [-1]" << endl;
        }
    }
}