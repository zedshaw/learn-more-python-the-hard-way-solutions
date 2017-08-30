import sorting
from dllist import DoubleLinkedList
from random import randint

max_numbers = 30

def random_list(count):
    numbers = DoubleLinkedList()
    for i in range(count, 0, -1):
        numbers.shift(randint(0, 10000))
    return numbers


def is_sorted(numbers):
    node = numbers.begin
    while node and node.next:
        if node.value > node.next.value: 
            return False
        else:
            node = node.next

    return True


def test_bubble_sort():
    numbers = random_list(max_numbers)

    sorting.bubble_sort(numbers)

    assert is_sorted(numbers)


def test_merge_sort():
    numbers = random_list(max_numbers * 31) 

    sorting.merge_sort(numbers)

    assert is_sorted(numbers)

def test_quick_sort():
    numbers = random_list(max_numbers)

    sorting.quick_sort(numbers, 0, numbers.count() - 1)

    assert is_sorted(numbers)
