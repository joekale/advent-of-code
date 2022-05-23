project("Advent of Code")
cmake_minimum_required(VERSION 3.18)

option(ADVENT_OF_CMAKE "Run the CMake solver" OFF)

if(NOT ADVENT_OF_CMAKE)
    add_subdirectory(2019)
    add_subdirectory(2020)
    add_subdirectory(2021)
else()
    message(${CMAKE_PROJECT_NAME})
    add_subdirectory("2020")
endif()