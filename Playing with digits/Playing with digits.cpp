//Playing with digits
//https://www.codewars.com/kata/5552101f47fc5178b1000050/train/cpp

#include <math.h>
#include <vector>
#include <iostream>

class DigPow
{
public:
	static int digPow(int n, int p);
};

int DigPow::digPow(int n, int p)
{
	std::vector<int> digits;
	int m = n, sum = 0;
	while (m != 0)
	{
		digits.push_back(m % 10);
		m = (m - m % 10) / 10;
	}
	for (int i = 0; i < digits.size(); ++i)
	{
		sum += (int)pow(digits[i], (p + digits.size() - i - 1));	}

	//std::cout << sum << " " << n << std::endl;
	if (sum % n == 0)
	{
		return sum / n;
	}
	else return -1;
}

int main()
{
	std::cout << DigPow::digPow(89, 1)<<std::endl;
	std::cout << DigPow::digPow(92, 1) << std::endl;
	std::cout << DigPow::digPow(695, 2) << std::endl;
	std::cout << DigPow::digPow(46288, 3) << std::endl;
}

