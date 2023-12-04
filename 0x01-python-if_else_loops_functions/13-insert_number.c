#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 *insert_node - Inserts a node in an ordered list
 *@head: Pointer to the linked list
 *@number: Value of the node to be added
 *
 *Return: Pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;

	current = *head;
	if (current == NULL || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}
	while (current && current->n < number)
	{
		current = current->next;
	}
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
