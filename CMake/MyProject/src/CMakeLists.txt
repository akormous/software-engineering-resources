cmake_minimum_required(VERSION 3.10)

# set project name
project(MyProject)

include_directories(../include)

# add executable to project
add_executable(MyProject main.cpp ../include/Calculator.h Calculator.cpp)