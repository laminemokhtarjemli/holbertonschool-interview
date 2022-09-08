#include "binary_trees.h"

/**
 * binary_height - measures the height
 * @tree: pointer to the root node
 *
 * Return: Height or 0 if NULL
 */
size_t binary_height(const binary_tree_t *tree)
{
	size_t height_l = 0;
	size_t height_r = 0;

	if (!tree)
		return (0);

	if (tree->left)
		height_l = 1 + binary_height(tree->left);

	if (tree->right)
		height_r = 1 + binary_height(tree->right);

	if (height_l > height_r)
		return (height_l);
	return (height_r);
}

/**
 * isBEST - check if node has a less value than himself
 * @root: node to check
 * @min: min value to check
 * @max: max value to check
 * Return: 1 if is a BST or 0 otherwise
 */
int isBEST(const binary_tree_t *root,
		  const binary_tree_t *min, const binary_tree_t *max)
{
	if (root == NULL)
		return (1);

	if (min != NULL && root->n <= min->n)
		return (0);

	if (max != NULL && root->n >= max->n)
		return (0);

	return (isBEST(root->left, min, root) &&
			isBEST(root->right, root, max));
}
/**
 * tree_is_best - checks if a nid Binary Search Tree
 * @tree: a pointer to the node to check
 * Return: 1 if BEST, and 0 otherwise
 */
int tree_is_best(const binary_tree_t *tree)
{
	if (!tree)
		return (0);

	return (isBEST(tree, NULL, NULL));
}

/**
 * avl_checke - checks if a tree is a valid AVL Tree
 * @tree: pointer to the node of the tree to check
 *
 * Return: 1 if tree is a valid AVL Tree, and 0 otherwise
 */
int avl_checke(const binary_tree_t *tree)
{
	int diff, heightL = 0, heightR = 0;

	if (!tree)
		return (1);

	if (!tree_is_best(tree))
		return (0);

	heightL = bianry_height(tree->left);
	heightR = binarytree_height(tree->right);

	diff = abs(heightL - heightR);

	if (diff == 0 && avl_checke(tree->left) && avl_checke(tree->right))
		return (1);
	return (0);
}

/**
 * binary_tree_is_avl - checks if a binary tree is a valid AVL Tree
 * @tree: pointer to the root node of the tree to check
 *
 * Return: 1 if tree is a valid AVL Tree, and 0 otherwise
 */
int binary_tree_is_avl(const binary_tree_t *tree)
{
	if (!tree)
		return (0);

	return (avl_checke(tree));
}
