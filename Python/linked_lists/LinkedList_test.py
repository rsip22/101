# -*- coding: utf-8 -*-

"""
module:: Tests for LinkedList
moduleauthor:: Renata Scheibler
"""
import pytest
from LinkedList import Element, LinkedList

@pytest.fixture()
def element():
    return Element(1)

def test_create_element(element):
    assert element.value == 1

@pytest.fixture()
def linked_list_object():
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)
    ll.append(e4)
    return ll

def test_create_LinkedList(linked_list_object):
    assert linked_list_object.head.value == 1

def test_get_position_LinkedList(linked_list_object):
    assert linked_list_object.getposition.next.next.value == 3

if __name__ == '__main__':
    unittest.main()
