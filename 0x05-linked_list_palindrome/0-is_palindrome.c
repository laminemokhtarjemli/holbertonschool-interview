#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * is_palindrome - Function that checks if a singly linked list is palindrome.
 * @head: Pointer to Linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int i = 0, j = 0, k[1000000], len = 0;

	if (head == NULL)
		return (0);
	for (len = 0; tmp != NULL; len++)
	{
		k[len] = tmp->n;
		tmp = tmp->next;
	}
	for (i = 0, j = len - 1; i < (len / 2); i++, j--)
	{
		if (k[i] != k[j])
			return (0);
	}
	return (1);
}