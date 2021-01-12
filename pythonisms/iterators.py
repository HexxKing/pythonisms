# Use iterators/generators on a custom collection to…
  # add ability to be used in a for in loop
  # add ability to be used in a list comprehension
  # add ability to convert to a list or other collection type

from data_structures.linked_list import LinkedList

class IterableLinkedList(LinkedList):
  def __init__(self, collection=None):
    self.head = None
    if collection:
      for item in reversed(collection): 
        self.insert(item)

  # iter needs to return a generator
  def __iter__(self):
    def value_generator():
    #traverse thru the LL
      current = self.head
      while current:
        yield current.value
        current = current.next
    return value_generator()
