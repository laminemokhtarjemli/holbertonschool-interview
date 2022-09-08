#include "sort.h"

/**
 * power - calculate power
 * @power: power
 * Return: result
 */

int power(int power)
{
	int i, result;
	result = 1;

	for (i = 0; i < power; i++)
		result *= 10;
	return (result);
}


/**
* radix_count - Sort the array depending on exp
* @array: Array to sort
* @size: Size of @array
* @exp: Int to divide array for the digit.
* Return: void
*/

void count_radix(int *array, int size, int exp)
{
int i, *out;
int cont[10] = {0};

out = malloc(sizeof(int) * size);
if (!out)
return;

for (i = 0; i < size; i++)
cont[(array[i] / exp) % 10]++;

for (i = 1; i < 10; i++)
cont[i] += cont[i - 1];

for (i = size - 1; i >= 0; i--)
{
out[cont[(array[i] / exp) % 10] - 1] = array[i];
cont[(array[i] / exp) % 10]--;
}

for (i = 0; i < size; i++)
array[i] = out[i];
free(out);
}

/**
 * radix_sort - sort an array of integers
 * @array: the array to be sorted
 * @size: size of the array
 */
void radix_sort(int *array, size_t size)
{
	int i, mx, digit;

	if (!array || size < 2)
		return;
	mx = array[0];
	for (i = 0; i < (int)size; i++)
	{
		if (array[i] > mx)
			mx = array[i];
	}
	digit = 1;
	while (mx > 0)
	{
		mx /= 10;
		count_radix(array, size, digit);
		digit *= 10;
		print_array(array, size);
	}
}
