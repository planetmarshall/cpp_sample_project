add_executable(sample main.cpp)

target_link_libraries(sample PRIVATE Euler::Euler)

install(TARGETS sample RUNTIME DESTINATION bin)
