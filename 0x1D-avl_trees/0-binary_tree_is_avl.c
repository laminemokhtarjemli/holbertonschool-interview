#include <stdlib.h>
#include <stdio.h>
#include "binary_trees.h"

int binary_tree_is_avl(const binary_tree_t *tree)
{
    if (tree == NULL)
    {
        return 0;
    }

    int left_height = 0;
    int right_height = 0;

    if (tree->left)
    {
        left_height = binary_tree_height(tree->left);
    }
    if (tree->right)
    {
        right_height = binary_tree_height(tree->right);
    }

    int height_diff = abs(left_height - right_height);
    if (height_diff > 1)
    {
        return 0;
    }

    int is_left_avl = binary_tree_is_avl(tree->left);
    int is_right_avl = binary_tree_is_avl(tree->right);

    if (is_left_avl == 0 || is_right_avl == 0)
    {
        return 0;
    }

    return 1;
}
