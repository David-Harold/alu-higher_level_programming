#!/usr/bin/python3
"""Module that replaces an element of a list at a specific position."""
 
 
def replace_in_list(my_list, idx, element):
    """Replace the element at idx with element, or leave list unchanged
    if idx is negative or out of range. Returns the list."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
 
