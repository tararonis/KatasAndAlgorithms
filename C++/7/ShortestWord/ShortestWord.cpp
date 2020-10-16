// ShortestWord.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <sstream>


using namespace std;
int find_short(string& str)
{
    string delimiter = " ";
    
    size_t pos = 0;
    string token;

    size_t min_length = str.length();
    while ((pos = str.find(delimiter)) != string::npos) {
        token = str.substr(0, pos);
        if (token.length() < min_length)
            min_length = token.length();
        str.erase(0, pos + delimiter.length());
    }
    return min_length;
}
int find_short(const string& str)
{
    istringstream inp(str);
    string s;
    int len = -1;
    while (getline(inp, s, ' '))
        if (s.length() < len)
            len = s.length();
    return len;
}

int main()
{
    cout << find_short("bitcoin take over the world maybe who knows perhaps");
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
