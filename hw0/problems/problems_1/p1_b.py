def add_element(lst, element):
    """
    Appends the given element to the end of the list.
    """
    lst.append(element)

def insert_element_at(lst, element, index):
    """
    Inserts the element at the specified index.
    """
    lst.insert(index, element)

def remove_element(lst, element):
    """
    Removes the first occurrence of the element from the list.
    """
    if element in lst:
        lst.remove(element)

def pop_element_at(lst, index):
    """
    Pops and returns the element at the specified index.
    """
    if len(lst) > index:
        return lst.pop(index)
