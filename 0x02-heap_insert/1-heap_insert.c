#include "binary_trees.h"

/**
 * heap_insert - Function that inserts a value into a Max Binary Heap.
 * @root: Double pointer to the root node of the Heap.
 * @value: Value store in the node to be inserted.
 * Return: Return a pointer to the inserted node, or NULL on failure
 */

heap_t *heap_insert(heap_t **root, int value)
{
	heap_t *new = NULL;
	heap_t *lowest = NULL;

	new = binary_tree_node(NULL, value);
	if (!new)
	{
		return (NULL);
	}

	if (!(*root))
	{
		*root = new;
		return (new);
	}

	lowest = insert_new_node(*root);
	if (!lowest->left)
	{
		lowest->left = new;
	}
	else
	{
		lowest->right = new;
	}

	new->parent = lowest;
	return (heap_swap(new));
}

/**
 * heap_size - Finds the node size.
 * @node: Pointer to the root node of the Heap.
 * Return: An struct with the node size.
 */

space_t heap_size(heap_t *node)
{
	space_t tmp, left, right;

	tmp.n = 0;
	tmp.p = node;
	if (!node->left || !node->right)
	{
		return (tmp);
	}

	left = heap_size(node->left);
	right = heap_size(node->right);
	if (left.n <= right.n)
	{
		left.n += 1;
		return (left);
	}
	else
	{
		right.n += 1;
		return (right);
	}
}

/**
 * insert_new_node - Inserts a new node.
 * @root: Pointer to the root node of the Heap.
 * Return: Pointer to new node.
 */
heap_t *insert_new_node(heap_t *root)
{
	space_t tmp;

	tmp = heap_size(root);
	return (tmp.p);
}

/**
 * heap_swap - Swap  position of Nodes.
 * @node: Pointer to be change the position.
 * Return: Pointer to the new position at the node.
 */
heap_t *heap_swap(heap_t *node)
{
	int tmp;
	heap_t *new_node = node;

	while (new_node->parent)
	{
		if (new_node->n > new_node->parent->n)
		{
			tmp = new_node->n;
			new_node->n = new_node->parent->n;
			new_node->parent->n = tmp;

			new_node = new_node->parent;
			continue;
		}
		return (new_node);
	}
	return (new_node);
}
