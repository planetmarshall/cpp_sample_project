#include <euler/euler.h>

#include <iostream>

int main() {
    std::cout << "Sum of multiples of 3 and 5 up to 42 is "
      << euler::sum_multiples_of_three_or_five(42)
      << std::endl;

    return 0;
}
