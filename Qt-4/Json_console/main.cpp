#include <iostream>
#include <fstream>
#include <string>
#include "json.hpp"

int main()
{
    std::string fileName;
    std::cout << "input file name : ";
    std::cin >> fileName;
    std::fstream fin(fileName);
    if(!fin.is_open()){
        std::cout << "Wrong file name\n";
        return 0;
    }
    nlohmann::json json_input = nlohmann::json::parse( fin );
    fin.close();
    while(true){
        std::cout << "input.json : \n";
        std::cout << json_input.dump(4) << "\n\n";
        std::cout << "input new field name to add new field\n";
        std::cout << "input 'save' to save changes\n";
        std::cout << "input 'exit' to exit\n";
        std::cout << "=-=: ";
        std::string command;
        std::cin >> command;
        if (command == "save")
        {
            std::string file;
            std::cout << "input save file name : ";
            std::cin >> file;
            std::fstream fout;
            fout.open(file, std::fstream::out);
            fout << json_input.dump(4);
            fout.close();
            continue;
        }
        if (command == "exit")
        {
            break;
        }
        std::cout << "input int value : ";
        int value;
        std::cin >> value;
        json_input[command] = value;
    }
    return 0;
}