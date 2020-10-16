// Testing 1-2-3.cpp : This file contains the 'main' function. Program execution begins and ends there.
//https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/cpp

#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;
std::vector<std::string> number(const std::vector<std::string>& lines)
{
    vector<string> output;
    for (size_t i = 0; i < lines.size(); i++)
    {
        ostringstream s_name;
        s_name << (i + 1) << ": " << lines[i];
        string name = s_name.str();
        output.push_back(name);
    }
    return output;
}
//std::vector<std::string> number2(const std::vector<std::string>& lines) {
//    std::vector<std::string> numbered_lines;
//    for (size_t i = 1; auto line: lines)
//        numbered_lines.push_back(to_string(i++) + ": " + line);
//    return numbered_lines;
//}

int main()
{
    vector<string> test = number({ "a", "b", "c" });
    for (auto& n : test)
    {
        cout << n << endl;
    }
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
