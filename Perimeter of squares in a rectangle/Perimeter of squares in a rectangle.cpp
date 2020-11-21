//Perimeter of squares in a rectangle
//https://www.codewars.com/kata/559a28007caad2ac4e000083/train/cpp
//#Hint: See Fibonacci sequence #Ref : http ://oeis.org/A000045

#include <iostream>
typedef unsigned long long ull;
class SumFct
{
public:
	static ull perimeter(int n);
};

ull SumFct::perimeter(int n)
{
	ull prev = 1, current = 1;
	
	ull sum = prev;
	for (int i = 0; i < n; i++)
	{
		sum += static_cast<ull>(current);

		//ull temp = current;
		//current = prev + current;
		//prev = temp;	
		current = prev + current;
		prev = current - prev;
	}
	return sum*4;
}
//ull SumFct::perimeter(int n)
//{
//	return (4 * round((((std::pow(1.6180339887498948482045868343656381177203091798058L, n + 3) - 
//						 std::pow(-0.6180339887498948482045868343656381177203091798058L, (n + 3))) / sqrt(5))) - 1));
//}

int main()
{
	std::cout << SumFct::perimeter(30);
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
