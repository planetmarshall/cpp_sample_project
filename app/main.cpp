#include <euler/euler.hpp>

#include <CLI/CLI.hpp>

#include <iostream>


int main(int argc, char **argv) {
    auto app = CLI::App("Project Euler Problem 1 <https://projecteuler.net/>");
    int maximum = 100;
    app.add_option("--maximum", maximum, "maximum number up to which to generate multiples of 3 and 5");

    try {
        app.parse(argc, argv);

        std::cout << "Sum of multiples of 3 and 5 up to 42 is "
            << euler::sum_multiples_of_three_or_five(maximum)
            << std::endl;

        return 0;
    }
    catch (const std::exception &ex) {
        std::cerr << "Error: " << ex.what();
        return -1;
    }
    catch (...) {
        std::cerr << "Unknown error";
        return -1;
    }
}
