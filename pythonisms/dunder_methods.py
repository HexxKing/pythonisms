# Use dunder methods make your code more readable and elegant. For example…
# add ability for custom data structure to be considered truthy/falsy

from pythonisms.iterators import IterableLinkedList

# add ability for two custom data structure to be considered equal
def __eq__(self, other):
  # consider https://docs.python.org/3/library/functools.html#functools.total_ordering for Data collections
  return list(self) == list(other)

def __str__(self):
  out = ""
  for value in self:
      out += f"[ {value} ] -> "
  return out + "None"