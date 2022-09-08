#include "sort.h"
/**
* merge_sort - sorts an array of integers
* using the Merge Sort algorithm. Top-down.
* @array: array to be sorted
* @size: number of elements in the array
* Return: nothing
*/
void merge_sort(int *array, size_t size)
{
	int *tmp = NULL;

	if (array == NULL || size <= 1)
		return;

	tmp = malloc(size * sizeof(int));

	if (tmp == NULL)
		return;

	recurcion(array, size, tmp);

	free(tmp);
}
/**
 * recurcion - merge sort using recurion
 * @array: array to be sorted
 * @size: number of elements in the array
 * @tmp: array to hold information during merge
 * Return: nothing
 */
void recurcion(int *array, size_t size, int *tmp)
{
	int mid;

	if (size <= 1)
		return;
	mid = size / 2;
	recurcion(array, mid, tmp);
	recurcion(array + mid, size - mid, tmp);
	merge(array, size, mid, tmp);
}
/**
 * merge - merge two arrays
 * @array: array to merge
 * @size: number of elements in the array
 * @mid: Mid index
 * @tmp: array to hold information
 * Return: nothing
 */
void merge(int *array, int size, int mid, int *tmp)
{
	int lft = 0;
	int rght = mid;
	int idx;

	printf("Merging...\n");
	printf("[left]: ");
	print_array(array, mid);
	printf("[right]: ");
	print_array(array + mid, size - mid);
	for (idx = 0; idx < size; idx++)
	{

		if (rght == size)
		{
			tmp[idx] = array[lft];
			lft++;
		}
		else if (lft == mid)
		{
			tmp[idx] = array[rght];
			rght++;
		}
		else if (array[rght] < array[lft])
		{
			tmp[idx] = array[rght];
			rght++;
		}
		else
		{
			tmp[idx] = array[lft];
			lft++;
		}
	}
	for (idx = 0; idx < size; idx++)
	{
		array[idx] = tmp[idx];
	}
	printf("[Done]: ");
	print_array(tmp, size);
}
