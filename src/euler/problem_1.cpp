#include <euler/euler.hpp>

#include <algorithm>
#include <numeric>
#include <ranges>

namespace views = std::ranges::views;

std::vector<int> euler::multiples_of_three_or_five(int max) {
    // NOLINTBEGIN(*-magic-numbers)
    auto multiples = std::ranges::views::iota(3, max)
           | views::filter([](int num) { return (num % 3 == 0) || (num % 5 == 0); });
    // NOLINTEND(*-magic-numbers)

    auto result = std::vector<int>{};
    std::ranges::copy(multiples, std::back_inserter(result));
    return result;
}

int euler::sum_multiples_of_three_or_five(int max) {
    auto multiples = multiples_of_three_or_five(max);
    return std::accumulate(std::begin(multiples), std::end(multiples), 0);
}
