# CMake Tutorial for Noobs

## What is CMake?
CMake is a tool to manage building of source code. Originally, CMake was designed as a generator for various dialects of Makefile, today CMake generates modern build systems such as Ninja as well as project files for IDEs such as Visual Studio and Xcode.
CMake is widely used for the C and C++ languages, but it supports other languages too.

## CMakeLists.txt
This is THE file. This is all that is required. This file should be in the project’s root directory. It contains a set of directives and instructions describing the project’s source files and targets (executable, library, or both).
For a single cpp file, just specify these 3 lines in CMakeLists.txt.

```cpp
cmake_minimum_required(VERSION 3.10)
# set the project name
project(MyProject)
# add the executable
add_executable(MyProject main.cpp)
```
## How to build?
A good way to build a project is to keep the build files in a separate folder named 'build'. CMake provides an option to create a build directory.

*CMake responsibility is to **generate** native build tool files from abstracted configuration code.*

Generate native build system
```
cmake -B build -S src
```
Call that build system to actually compile/link the project
```
cmake --build build
```