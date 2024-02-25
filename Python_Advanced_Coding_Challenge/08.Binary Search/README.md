# Binary Search Program

## Description
This Python program implements both naive and binary search algorithms to efficiently find a target number in a sorted list of numbers. 

Binary search is a search algorithm that works by repeatedly dividing the search interval in half. It starts by examining the middle element of the sorted list. If the target value matches the middle element, the search is successful. If the target is less than the middle element, the search continues in the lower half of the list; otherwise, it continues in the upper half. Binary search has a time complexity of O(log n), making it significantly faster than naive search for large lists.

Naive search, on the other hand, is a simple search algorithm that iterates through the list linearly, comparing each element with the target until it finds a match or reaches the end of the list. Naive search has a time complexity of O(n), where n is the number of elements in the list.

This program provides a comparison between the two search algorithms in terms of their performance and effectiveness.

## Installation
There's no installation required for this program. You can simply download the Python script and run it using a Python interpreter.

## Usage
To use the program:
1. Run the script in a Python environment.
2. Follow the prompts to input a list of numbers separated by spaces and the target number to search for.
3. The program will output the search results and execution time for both naive and binary search algorithms.

## Performance Measurement
Python's `time.perf_counter()` function is used to measure the execution time of each search method. It returns a high-resolution performance counter that can be used for benchmarking code execution time. By measuring the time before and after executing each search algorithm, we can accurately determine their performance.

## Contributing
Contributions to this project are welcome! If you'd like to contribute , please fork the repository and make a pull request.