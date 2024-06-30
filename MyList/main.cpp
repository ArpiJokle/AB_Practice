#include <iostream>
#include "List.h"

int main()
{
    MyList list;
    list.AddFirst(7);
    list.AddFirst(4);
    list.Print();
    std::cout << "\n";
    list.AddFirst(6);
    list.AddFirst(2);
    list.Print();
    std::cout << "\n";
    list.DeleteElement();
    list.Print();
    std::cout << "\n";
    std::cout << (list.Empty() ? "empty\n" : "not empty\n");
    std::vector<int> Vector;
    list.ToVector(Vector);
    return 0;
}