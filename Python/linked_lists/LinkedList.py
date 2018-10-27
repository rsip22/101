"""
Adicione três funções à lista vinculada.

"get_position" retorna o elemento em uma determinada posição.

A função "insert" adicionará um elemento a um lugar específico na lista.

"delete" excluirá o primeiro elemento com aquele valor específico.
"""

class Element(object):
    """ Unity in a linked list """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    """ Linked List. Head sets the first element in the list. """

    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """
        Append new_element to the end of the list. Repeats the reference
        'next' in each Element until it reaches the end of the list (setting
        the new_element).
        """
        current = self.head

        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def getposition(self, position):
        """
        Returns the element in the given position.
        Returns None if the position is not in the list.
        """
        return None

    def insert(self, element, position):
        """
        Inserts an element into a given position in the Linked List.
        """
        pass

    def delete(self, value):
        """
        Excludes the first element with the given value.
        """
        pass
