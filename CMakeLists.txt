cmake_minimum_required(VERSION 2.8.12)
project(mdscatter)

add_subdirectory(pybind11)
pybind11_add_module(mdscatter src/dft.cpp)
