#include "binary_trees.h"

/**
 * new_node - creates a new node
 *
 * @parent: parents node
 * @n: data of the new node
 * Return: new node
 */

avl_t *new_node(avl_t *parent, int n)
{
	avl_t *new_node;

	new_node = malloc(sizeof(avl_t));
	if (!new_node)
		return (NULL);
	new_node->n = n;
	new_node->parent = parent;
	new_node->left = NULL;
	new_node->right = NULL;

	return (new_node);
}

/**
 * array_to_bts - builds the array into a avl tree
 *
 * @array: array of integers
 * @start: start point
 * @end: end point of the array
 * @parent: parent's node
 * Return: root node
 */

avl_t *array_to_bts(int *array, int start, int end, avl_t *parent)
{
	avl_t *root;
	int middle;

	if (start > end)
		return (NULL);

	middle = (start + end) / 2;
	root = new_node(parent, array[middle]);

	if (!root)
		return (NULL);

	root->left = array_to_bts(array, start, middle - 1, root);

	root->right = array_to_bts(array, middle + 1, end, root);

	return (root);
}

/**
 * sorted_array_to_avl - builds an AVL tree from a sorted array
 *
 * @array: array
 * @size: size of the array
 * Return: root node
 */

avl_t *sorted_array_to_avl(int *array, size_t size)
{
	if (!array)
		return (NULL);

	return (array_to_bts(array, 0, size - 1, NULL));
}