

CMAKE_MINIMUM_REQUIRED(VERSION 3.2)

PROJECT(MDScatter CXX)
SET(foo_VERSION_MAJOR 1)
SET(foo_VERSION_MINOR 0)


# C++11 Stuff
SET(CMAKE_CXX_STANDARD 11)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

SET(SRC dft.cpp)

INCLUDE_DIRECTORIES("/usr/include/python3.6m")

FIND_PACKAGE(pybind11 REQUIRED)

FIND_PACKAGE(OpenMP)
IF(OpenMP_FOUND)
	SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
ENDIF(OpenMP_FOUND)

add_library(mdscatter MODULE ${SRC})
target_link_libraries(mdscatter PRIVATE pybind11::module)
set_target_properties(mdscatter PROPERTIES PREFIX "${PYTHON_MODULE_PREFIX}"
                                         SUFFIX "${PYTHON_MODULE_EXTENSION}")
