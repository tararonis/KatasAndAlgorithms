//Josephus Survivor
//https://www.codewars.com/kata/555624b601231dc7a400017a/cpp

#include <iostream>
#include <vector>
#include <algorithm>


/*int josephusSurvivor(int n, int k) {
	// your code here
	int survivor = 0;
	for (int i = 2; i < n + 1; i++) {
		survivor = (survivor + k) % i;
	}
	return survivor + 1;
}*/

int josephusSurvivor(int n, int k) {
	std::vector<int> people;
	for (int i = 1; i <= n; ++i) {
		people.push_back(i);
	}
	int j = --k;
	while (people.size() > 1) {
		if (j >= people.size()) j = (j - people.size()) % people.size();
		people.erase(people.begin() + j);
		j += k;
	}

	return people.front();
}




int main()
{
    std::cout << josephusSurvivor(7,3);
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
