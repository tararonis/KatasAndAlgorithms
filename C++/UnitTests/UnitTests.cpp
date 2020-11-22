#pragma once
#include "pch.h"
#include "CppUnitTest.h"

#include "../4/Permutations/Permutations.h"




using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTests
{
	TEST_CLASS(PermutationsUnitTests)
	{
	public:
		TEST_METHOD(Permutations) {			
			Assert::IsTrue(std::vector<std::string> {"a"}== permutations("a"), L"ProblemA");
			Assert::IsTrue(std::vector<std::string> {"ab", "ba"}== permutations("ab"));
			Assert::IsTrue(std::vector<std::string> {"aabb", "abab", "abba", "baab", "baba", "bbaa"}== permutations("aabb"));
		
		}
	};
}
