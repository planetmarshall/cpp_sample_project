#include <euler/euler.h>

#include <gtest/gtest.h>

TEST(TestProblem1, ListOfMultiplesBelow10) {
  auto multiples = euler::multiples_of_three_or_five(10);
  ASSERT_EQ((std::vector<int>{3, 5, 6, 9}), multiples);
}

TEST(TestProblem1, SumOfMultiplesBelow10) {
  auto sum = euler::sum_multiples_of_three_or_five(10);
  ASSERT_EQ(23, sum);
}
