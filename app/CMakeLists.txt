add_executable(eulerapp main.cpp)

target_link_libraries(eulerapp PRIVATE Euler::Euler)

install(TARGETS eulerapp RUNTIME DESTINATION bin)
