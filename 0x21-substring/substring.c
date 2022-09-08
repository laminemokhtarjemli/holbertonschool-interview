#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "substring.h"


/**
 * find_substring - begin point
 * @s: char const
 * @words: char const
 * @nb_words: int
 * @n: int
 * Return: 0, 1
 */
int *find_substring(char const *s, char const **words, int nb_words, int *n)
{
	int a = 0, b, c, *result, *picked, length, wlength;

	length = strlen(s);
	wlength = strlen(words[0]);
	result = (int *)malloc(length * sizeof(int));
	picked = (int *)malloc(nb_words * sizeof(int));

	while (a <= length - nb_words * wlength)
	{
		for (b = 0; b < nb_words; b++)
		{
			picked[b] = 0;
		}
		for (b = 0; b < nb_words; b++)
		{
			for (c = 0; c < nb_words; c++)
			{
				if (picked[c] == 0 && strncmp(s + a + b * wlength, words[c], wlength) == 0)
				{
					picked[c] = 1;
					break;
				}
			}
			if (c == nb_words)
			{
				break;
			}
		}
		if (b == nb_words)
		{
			result[(*n)++] = a;
		}
		a++;
	}
	free(picked);
	return (result);
}
