#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *tmp, *new_node;

	ptr = *head;
	tmp = ptr->next;

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
		return (*head);
	}

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
