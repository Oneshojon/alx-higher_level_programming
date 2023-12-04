#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *is_palindrome - checks if a singly linked list is pallindrome
 *@head: Pointer to the linked list
 *
 *Return: 1 if pallindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i = 0, j, k, *arr;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	while(temp != NULL)
	{
		i++;
		temp = temp->next;
	}
	arr = malloc(sizeof(int) * i);
	if (arr == NULL)
		return (0);
	temp = *head;
	for (j = 0; j < i; j++)
	{
		arr[j] = temp->n;
		temp = temp->next;
	}

	j = 0;
	for (j = 0, k = i - 1; j <= k; j++, k--)
	{
		if (arr[j] != arr[k])
		{
		/*	printf("%d = %d\n", (temp + j)->n, (temp + k)->n);*/
			free(arr);
			return (0);
		}
		/*printf("%d = %d\n", (temp + j)->n, (temp + k)->n);*/
	}
	free(arr);
	return (1);
}
