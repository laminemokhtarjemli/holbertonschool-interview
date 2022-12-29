#include <limits.h>
#include "binary_trees.h"

/**
 * binary_tree_is_bst - Recursively checks if a binary tree is a valid BST
 * @tree: Pointer to the root node of the tree to check
 * @lower: Lower bound for the values of the nodes in the tree
 * @upper: Upper bound for the values of the nodes in the tree
 *
 * Return: 1 if the tree is a valid BST, and 0 otherwise
 */
int binary_tree_is_bst(const binary_tree_t *tree, int lower, int upper)
{
    if (!tree)
        return (1);

    if (tree->n < lower || tree->n > upper)
        return (0);

    return (binary_tree_is_bst(tree->left, lower, tree->n - 1) &&
            binary_tree_is_bst(tree->right, tree->n + 1, upper));
}

/**
 * binary_tree_is_avl - Checks if a binary tree is a valid AVL tree
 * @tree: Pointer to the root node of the tree to check
 *
 * Return: 1 if the tree is a valid AVL tree, and 0 otherwise
 */
int binary_tree_is_avl(const binary_tree_t *tree)
{
    if (!tree)
        return (0);

    if (!binary_tree_is_bst(tree, INT_MIN, INT_MAX))
        return (0);

    int left_height = 0;
    int right_height = 0;

    if (tree->left)
        left_height = binary_tree_height(tree->left);
    if (tree->right)
        right_height = binary_tree_height(tree->right);

    int height_diff = abs(left_height - right_height);
    if (height_diff > 1)
        return (0);

    return (1);
}
