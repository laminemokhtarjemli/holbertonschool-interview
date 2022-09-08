#ifndef SORT_H
#define SORT_H
#include <stdlib.h>
#include <stdio.h>


void print_array(const int *array, size_t size);
void merge_sort(int *array, size_t size);
void recurcion(int *array, size_t size, int *tmp);
void merge(int *array, int size, int middle, int *tmp);

#endif