#include <stdlib.h>
#include <stdio.h>

#include "palindrome.h"

/**
 * is_palindrome - Function that checks a given Number is a Palindrome.
 * @n: Number to be checked.
 * Return: Return 1 if n is a palindrome, and 0 otherwise.
 */

int is_palindrome(unsigned long n)
{
	unsigned long array[1024];
	unsigned long num = n;
	int i = 0, j = 0;

	while (num != 0)
	{
		array[i++] = num % 10;
		num = num / 10;
	}

	i--;
	for (; i > j; i--, j++)
	{
		if (array[i] != array[j])
			return (0);
	}

	return (1);
}
