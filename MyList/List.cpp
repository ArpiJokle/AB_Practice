#include "List.h"

void MyList::AddFirst(int Value)
{
    SElement *NEW = new SElement(Value, first);
    first = NEW;
}

void MyList::Print()
{
    for (SElement *temp = first; temp != nullptr; temp = temp->next)
        std::cout << temp->data << " ";
}

int MyList::DeleteElement()
{
    if(first == nullptr)
        return -1;
    SElement *Temp = first;
    first = first->next;
    int Value = Temp->data;
    delete Temp;
    return Value;
}

MyList::MyList()
{
    first = nullptr;
}

MyList::MyList(int a)
{
    first = new SElement(a, nullptr);
}

MyList::MyList(int a, int b, int c)
{
    first = new SElement(a, nullptr);
    SElement *temp = new SElement(b, nullptr);
    first->next = temp;
    temp = new SElement(c, nullptr);
    first->next->next = temp;
}

MyList::~MyList()
{
    while (first != nullptr)
        this->DeleteElement();
}

bool MyList::Empty()
{
    return (nullptr == first);
}

void MyList::ToVector(std::vector<int> &Vec)
{
    Vec.clear();
    for (SElement *temp = first; temp != nullptr; temp = temp->next)
        Vec.push_back(temp->data);
}