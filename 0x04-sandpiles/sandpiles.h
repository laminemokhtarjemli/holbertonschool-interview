#ifndef SANDPILES_H
#define SANDPILES_H

#define s 3
#define R(x, y) (x >= 0 && x < 3 && y >= 0 && y < 3)

#include <stdlib.h>
#include <stdio.h>

void sandpiles_sum(int grid1[3][3], int grid2[3][3]);
void balance_sandpile(int grid1[3][3], int i, int j);
void printgrid(int grid[3][3]);

#endif