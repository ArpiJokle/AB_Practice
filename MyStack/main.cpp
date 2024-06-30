#include <iostream>
#include "MyStack.h"

int main()
{
    MyStack stack;
    stack.Push(7);
    stack.Push(4);
    stack.Push(6);
    stack.Push(2);
    stack.PrintStack();
    std::cout << std::endl;
    std::vector<int> Vector;
    stack.toVector(Vector);
    for(auto i : Vector)
        std::cout << i << "\n";
    return 0;
}