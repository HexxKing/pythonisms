from pythonisms.iterators import IterableLinkedList
from pythonisms.dunder_methods import __eq__, __str__
import pytest

def test_str():
  foods = IterableLinkedList(["apple","banana","cucumber"])
  assert str(foods) == "[ apple ] -> [ banana ] -> [ cucumber ] -> None"