#include "menger.h"

/**
 * menger - Function that draws a 2D Menger Sponge.
 * @level: The level of the Menger Sponge to draw.
 * Return: Void - No return.
 */
void menger(int level)
{
	int i = 0, j = 0, i_2 = 0, j_2 = 0;
	int size = pow(3, level), space = 0;

	for (i = 0; i < size; i++)
	{
		for (j = 0; j < size; j++)
		{
			for (i_2 = i, j_2 = j, space = 0; i_2 || j_2; i_2 /= 3, j_2 /= 3)
				if (i_2 % 3 == 1 && j_2 % 3 == 1)
				{
					space = 1;
				}
			printf("%c", space ? ' ' : '#');
		}
		printf("\n");
	}
}
