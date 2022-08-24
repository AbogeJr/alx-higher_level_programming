#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *tmp, *new_node;

	ptr = *head;

	new_node = malloc(sizeof(listint_t));

	if(!new_node)
	{
		printf("Allocation Error!\n");
		return (NULL);
	}

	new_node->next = NULL;
	new_node->n = number;

	if(!(*head))
	{
		*head = new_node;
		return (new_node);
	}

	if((*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	tmp = ptr->next;
	while(tmp)
	{
		if(tmp->n >= number)
			break;
		ptr = tmp;
		tmp = tmp->next;
	}

	new_node->next = tmp;
	ptr->next = new_node;

	return (new_node);
}
