#pragma once
#include "mylist.h"

class MyStack : private MyList
{
public:
    MyStack() : MyList() {}
    MyStack(int a) : MyList(a) {}
    MyStack(int a, int b, int c) : MyList(a, b, c) {}
    ~MyStack() = default;
    int Pop();
    void Push(int);
    bool IsEmpty();
    void PrintStack();
    void toVector(std::vector<int> &);
};
