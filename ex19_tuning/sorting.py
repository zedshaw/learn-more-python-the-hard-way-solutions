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
    """performance: cache the length in the node?"""
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
  
    # performance: can we use a for loop?
    merged_left = merge_node(start)
    merged_right = merge_node(mid_node)

    # performance: can we reduce the calls to this?
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
    """performance slowest part of quick_sort, but because it's called a lot"""
    count = 0
    node = numbers.begin
    while node and count < i:
        node = node.next
        count += 1
    return node

def quick_sort(numbers, lo, hi):
    numlist = numbers.to_list()
    quick_sort_doit(numlist, lo, hi)

def quick_sort_doit(numbers, lo, hi):
    """Sorts a list of numbers using quick sort.
    You must implement this one based on the p-code
    at https://en.wikipedia.org/wiki/Quicksort or
    any other reference.
    """
    # performance: just turn it into a python list first
    if lo < hi:
        # performance: can we replace with for-loop?
        p = quick_sort_partition(numbers, lo, hi)
        quick_sort_doit(numbers, lo, p - 1)
        quick_sort_doit(numbers, p + 1, hi)

def quick_sort_partition(numbers, lo, hi):
    """ performance, node_at called too many times"""
    pivot = numbers[hi]
    i = lo - 1
    node_i = None

    for j in range(lo, hi):
        node_j = numbers[j]
        if node_j.value < pivot.value:
            i += 1
            if i != j:
                node_i = numbers[i]
                node_i.value, node_j.value = node_j.value, node_i.value

    # performance: can we eliminate these?
    node_i = numbers[i+1]

    if pivot.value < node_i.value:
        pivot.value, node_i.value = node_i.value, pivot.value

    return i + 1
