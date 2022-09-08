#include "search.h"

/**
 * linear_skip - searches for a value in a sorted skip list of integers
 * @list: pointer to head of skip list
 * @value: value to be searched for in skip list
 *
 * Return: pointer on success or NULL
 */

skiplist_t *linear_skip(skiplist_t *list, int value)
{
	skiplist_t *express_lane, *previous;

	if (!list)
		return (NULL);

	express_lane = list->express;
	previous = list;

	for (; express_lane; express_lane = express_lane->express)
	{
		printf("Value checked at index [%lu] = [%d]\n",
				express_lane->index, express_lane->n);
		if (!express_lane->express || express_lane->n >= value)
		{
			if (!express_lane->express && express_lane->n < value)
			{
				previous = express_lane;
				for (; express_lane->next; express_lane = express_lane->next)
					;
			}
			printf("Value found between indexes [%lu] and [%lu]\n",
					previous->index, express_lane->index);
			for (; previous; previous = previous->next)
			{
				printf("Value checked at index [%lu] = [%d]\n",
						previous->index, previous->n);
				if (previous->n > value)
					return (NULL);
				if (previous->n == value)
					return (previous);
			}
			break;
		}
		previous = express_lane;
	}
	return (NULL);
}
