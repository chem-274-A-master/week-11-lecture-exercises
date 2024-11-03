#!/bin/bash

set -eux

g++ -std=c++17 -Wall -pedantic -fsanitize=address main.cpp -I. -o main
./main
