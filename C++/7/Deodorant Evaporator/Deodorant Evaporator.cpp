// Deodorant Evaporator.cpp : This file contains the 'main' function. Program execution begins and ends there.
// https://www.codewars.com/kata/5506b230a11c0aeab3000c1f/train/cpp

#include <iostream>
#include <cmath>
using namespace std;
class Evaporator
{

public:
    static int evaporator(double content, double evap_per_day, double threshold)
    {
        int c = 0;
        double o_content = content;
        while (content > o_content / 100 * threshold)
        {
            content = content - (content / 100 * evap_per_day);
            c++;
        }
        return c;
    }
    static int evaporator2(double content, double evap_per_day, double threshold)
    {
        return ceil(log(threshold / 100) / log(1.0 - (evap_per_day / 100)));
    }

};

int main()
{
    Evaporator e;
    cout<<e.evaporator2(10, 10, 10);
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
