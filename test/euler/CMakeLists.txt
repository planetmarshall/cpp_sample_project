include(GoogleTest)
add_executable(test_core 
    main.cpp
        test_problem_1.cpp)

target_link_libraries(test_core
    PUBLIC
    GTest::GTest
    Euler::Euler
)

add_test(
    NAME test_euler
    COMMAND test_euler
    )

