#include <euler/euler.hpp>

#include <boost/program_options.hpp>

#include <iostream>

namespace po = boost::program_options;

int main(int argc, char **argv) {
    po::options_description description("Project Euler Problem 1 <https://projecteuler.net/>");
    int maximum{};
    description.add_options()
        ("help", "show help message")
        ("maximum", po::value<int>(&maximum)->default_value(100), "maximum number up to which to generate multiples of 3 and 5")
    ;
    po::variables_map vm;
    po::store(po::parse_command_line(argc, argv, description), vm);
    po::notify(vm);

    std::cout << "Sum of multiples of 3 and 5 up to 42 is "
      << euler::sum_multiples_of_three_or_five(maximum)
      << std::endl;

    return 0;
}
