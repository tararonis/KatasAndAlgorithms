//Which are in?
//https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/cpp

#include <iostream>
#include <vector>
#include <algorithm>

class WhichAreIn
{

public:
	static std::vector<std::string> inArray(std::vector<std::string>& array1, std::vector<std::string>& array2);
};
bool IsContains(std::string& a, std::vector<std::string>& array2)
{
	for (auto s : array2)
	{
		if (s.find(a) != std::string::npos)
			return true;
	}
	return false;
}
std::vector<std::string> WhichAreIn::inArray(std::vector<std::string>& array1, std::vector<std::string>& array2)
{
	std::vector<std::string> ans;
	for (auto s : array1)
	{
		if (IsContains(s, array2))
		{
			ans.push_back(s);
		}
	}
	std::sort(ans.begin(), ans.end());
	return ans;
}



int main()
{
    std::cout << "Hello World!\n";
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
