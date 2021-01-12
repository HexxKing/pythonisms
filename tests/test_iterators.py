from pythonisms.iterators import IterableLinkedList 
import pytest

#ability to be used in a for in loop
def test_for_in():
    foods = IterableLinkedList(("apple","banana","cucumber"))
    foods_list = []
    for food in foods:
        foods_list.append(food)
    assert foods_list == ["apple","banana","cucumber"]


#ability to be used in a list comprehension
def test_list_comprehension():
  foods = IterableLinkedList(("apple","banana","cucumber"))
  cap_foods = [food.upper() for food in foods]
  assert cap_foods == ["APPLE","BANANA","CUCUMBER"]

# ability to convert to a list
def test_list_cast():
  food_list = ["apple","banana","cucumber"]
  foods = IterableLinkedList(food_list)
  assert list(foods) == food_list