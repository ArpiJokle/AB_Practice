#include <iostream>
#include "List.h"

int main()
{
    MyList list;
    list.AddFirst(23);
    list.AddFirst(1);
    list.AddFirst(4);
    list.AddFirst(2);
    list.AddFirst(3);
    std::cout << "STAER\n";
    for (ListIterator iterator(&list); iterator.IsDone(); iterator.Next())
    {
        std::cout << iterator.CurrentItem() << '\n';
    }
    std::cout << "FINISH\n";
    return 0;
}