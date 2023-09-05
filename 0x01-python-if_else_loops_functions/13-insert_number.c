#include "lists.h"
/**
 * insert_node - insert a node at a point
 *
 * @head: the head of the node
 * @number, the number
 * Return: the head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newd = (listint_t *)(malloc(sizeof(listint_t))), *temp;

	if (newd == NULL)
		return (NULL);
	newd->n = number;
	newd->next = NULL;
	temp = *head;
	if ((*head) == NULL || temp->n > number)
	{
		
		newd->next = (*head);
		(*head) = newd;
		return (*head);

	}
	for (; temp->next != NULL; temp = temp->next)
		{
			if (temp->next->n > number)
				break;
		}
	newd->next = temp->next;
	temp->next = newd;
	return ((temp));
}
