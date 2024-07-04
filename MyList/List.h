#pragma once
#include <iostream>
#include <vector>

struct SElement
{
    int data;
    SElement *next;
    SElement(int data_, SElement *next_)
        : data{data_}, next{next_} {};
    ~SElement() = default;
};

class MyList
{
private:
    SElement *first;
public:
    // Конструктор без параметров создает пустой список
    MyList(); 
    // Конструктор с 1 параметром создает список из одного элемента
    MyList(int a);
    // Конструктор с 3 параметрами создает список из 3 элементов
    MyList(int a, int b, int c);
    // Деструктор MyList очищает выделенную на узлы списка памяти 
    ~MyList();
    // Возвращает состояние списка
    bool Empty();
    // Добавляет элемент в начало списка
    void AddFirst(int Value);
    // Удаляет первый элемент списка
    int DeleteElement();
    // Выводит на экран весь список
    void Print();
    // Возвращает количество элементов в списке
    int Count();
    // Возвращает значение первого элемента списка
    int Get(int);
    // Преобразует список в вектор
    void ToVector(std::vector<int>&);
};
