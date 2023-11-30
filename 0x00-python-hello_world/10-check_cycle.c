#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 *check_cycle -Checks if a circle exists in a singly linked list
 *@list: The list to be checked
 *
 *Return: 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast; 

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}	
	return (0);
}
