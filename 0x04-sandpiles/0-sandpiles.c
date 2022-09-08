#include "sandpiles.h"

/**
 * _print_grid - Function that prints a Sandpile.
 * @grid: Sandpile to be printed
 */
void _print_grid(int grid[3][3])
{
	int i, j;

	printf("=\n");
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (j)
				printf(" ");
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}

/**
 * balance_sandpile - Function that makes stable a Sandpile.
 * @grid1: Sandpile to be balanced.
 * @i: Posiion of the Sandpile to be balanced.
 * @j: Posiion of the Sandpile to be balanced.
 */
void balance_sandpile(int grid1[3][3], int i, int j)
{
	int l_i = 0, l_j = -1;
	int r_i = 0, r_j = 1;
	int u_i = -1, u_j = 0;
	int d_i = 1, d_j = 0;

	grid1[i][j] -= 4;

	if (R(l_i + i, l_j + j))
		grid1[l_i + i][l_j + j] += 1;
	if (R(r_i + i, r_j + j))
		grid1[r_i + i][r_j + j] += 1;
	if (R(u_i + i, u_j + j))
		grid1[u_i + i][u_j + j] += 1;
	if (R(d_i + i, d_j + j))
		grid1[d_i + i][d_j + j] += 1;
}


/**
 * sandpiles_sum - Function that computes the sum of two sandpiles.
 * @grid1: First sandpile.
 * @grid2: Second sandpile.
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int i = 0, j = 0, tmp = 0;
	int new[3][3];

	for (i = 0; i < s; i++)
	{
		for (j = 0; j < s; j++)
		{
			grid1[i][j] += grid2[i][j];
		}
	}

	do {
		tmp = 0;
		for (i = 0; i < s; i++)
			for (j = 0; j < s; j++)
			{
				if (grid1[i][j] > 3)
				{
					new[i][j] = 1;
					tmp = 1;
				}
				else
					new[i][j] = 0;
			}
		if (tmp)
		{
			_print_grid(grid1);
			for (i = 0; i < s; i++)
				for (j = 0; j < s; j++)
				{
					if (new[i][j] == 1)
						balance_sandpile(grid1, i, j);
				}
		}
	} while (tmp);
}
