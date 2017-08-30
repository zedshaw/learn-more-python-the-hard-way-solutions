from dllist import DoubleLinkedList
from queue import Queue
from random import randint

def bubble_sort(numbers):
    """Sorts a list of numbers using bubble sort."""
    while True:
        # start off assuming it's sorted
        is_sorted = True
        # comparing 2 at a time, skipping ahead
        node = numbers.begin.next
        while node:
            # loop through comparing node to the next
            if node.prev.value > node.value:
                # if the next is greater, then we need to swap
                node.prev.value, node.value = node.value, node.prev.value
                # oops, looks like we have to scan again
                is_sorted = False
            node = node.next

        # this is reset at the top but if we never swapped then it's sorted
        if is_sorted: break


def count(node):
    count = 0

    while node:
        node = node.next
        count += 1

    return count


def merge_sort(numbers):
    numbers.begin = merge_node(numbers.begin)

    # horrible way to get the end
    node = numbers.begin
    while node.next:
        node = node.next
    numbers.end = node


def merge_node(start):
    """Sorts a list of numbers using merge sort."""
    if start.next == None:
        return start

    mid = count(start) // 2

    # scan to the middle
    scanner = start
    for i in range(0, mid-1):
        scanner = scanner.next

    # set mid node right after the scan point
    mid_node = scanner.next
    # break at the mid point
    scanner.next = None
    mid_node.prev = None
   
    merged_left = merge_node(start)
    merged_right = merge_node(mid_node)

    return merge(merged_left, merged_right)



def merge(left, right):
    """Performs the merge of two lists."""
    result = None

    if left == None: return right
    if right == None: return left

    if left.value > right.value:
        result = right
        result.next = merge(left, right.next)
    else:
        result = left
        result.next = merge(left.next, right)

    result.next.prev = result
    return result

def node_at(numbers, i):
    count = 0
    node = numbers.begin
    while count < i:
        count += 1
        node = node.next
        assert node, f"Attempted to get node past end {i}"
    return node


def quick_sort(numbers, lo, hi):
    """Sorts a list of numbers using quick sort.
    You must implement this one based on the p-code
    at https://en.wikipedia.org/wiki/Quicksort or
    any other reference.
    """
    if lo < hi:
        p = quick_sort_partition(numbers, lo, hi)
        quick_sort(numbers, lo, p - 1)
        quick_sort(numbers, p + 1, hi)

def quick_sort_partition(numbers, lo, hi):
    """Does the partition step of quicksort."""
    pivot = node_at(numbers, hi)
    i = lo - 1

    for j in range(lo, hi):
        numbers.dump()
        node_j = node_at(numbers, j)
        if node_j.value < pivot.value:
            i += 1
            node_i = node_at(numbers, i)
            node_i.value, node_j.value = node_j.value, node_i.value
        else:
            
    node_hi = node_at(numbers, hi)
    node_i = node_at(numbers, i + 1)
    if node_hi.value < node_i.value:
        node_i.value, node_hi.value = node_hi.value, node_i.value

    return i + 1

    
