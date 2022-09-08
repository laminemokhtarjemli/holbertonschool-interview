#ifndef SORT_H
#define SORT_H
#include <stdlib.h>
#include <stdio.h>


void print_array(const int *array, size_t size);
void merge_sort(int *array, size_t size);
void recursion(int *array, size_t size, int *tmp);
void merge_worker(int *array, int size, int middle, int *tmp);

#endif