// Permutations
//https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/cpp

#include<algorithm>
#include "Permutations.h"

std::vector<std::string> permutations(std::string s) {
	std::vector<std::string> ans;
	std::sort(s.begin(), s.end(), std::greater<char>());
	do {
		ans.push_back(s);
		std::cout << s << std::endl;
	} while (std::prev_permutation(s.begin(), s.end()));
	std::sort(ans.begin(), ans.end());
	return ans;
}

int main()
{
	return 0;
}


