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
	listint_t *new_node, *current, *temp;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	current = *head;
	temp = *head;
	while (current)
	{
		if (current->n > number)
			break;
		temp = current;
		current = current->next;
	}
	new_node->next = current;
	if (temp == NULL)
		*head = new_node;
	else
		temp->next = new_node;
	return (NULL);
}
