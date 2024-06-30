#include <iostream>
#include "List.h"

int main()
{
    MyList list;
    list.AddFirst(7);
    list.AddFirst(4);
    list.AddFirst(6);
    list.AddFirst(2);
    list.Print();
    std::cout << std::endl;
    std::vector<int> Vector;
    list.ToVector(Vector);
    for(auto i : Vector)
        std::cout << i << "\n";
    return 0;
}