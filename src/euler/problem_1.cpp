#include <euler/euler.hpp>

#include <range/v3/view/iota.hpp>
#include <range/v3/view/filter.hpp>
#include <range/v3/to_container.hpp>
#include <range/v3/numeric/accumulate.hpp>

namespace views = ranges::views;

std::vector<int> euler::multiples_of_three_or_five(int max) {
  return  views::ints(3, max)
          | views::filter([] (int i) { return (i % 3 == 0) || (i % 5 == 0); })
          | ranges::to<std::vector>();
}

int euler::sum_multiples_of_three_or_five(int max) {
  return ranges::accumulate(euler::multiples_of_three_or_five(max), 0);
}
