#!/usr/bin/python

# Programming question week 2, http://www.algo-class.org/ June 2012.

# Given a file containing all of the integers between 1 and 10,000
# (inclusive, with no repeats) in unsorted order, compute the total
# number of comparisons used to sort the given input file by
# QuickSort.

# Do this using three different pivot-choosing strategies: always
# using the first element of the given array, always using the final
# element, and using the 'median-of-three' rule, i.e. the median
# element of the first, middle and final elements of the array.

import sys
import math

def Partition(A, l, r):
  """Partition a section of an array for the QuickSort algorithm.
     The element at A[l] is used as the pivot.
     Args:
       A: an array of integers;
       l: the leftmost index of the section to partition;
       r: the rightmost index of the section to partition (inclusive).
  """
  p = A[l]
  i = l + 1
  for j in range(l + 1, r + 1):
    if A[j] < p:
      A[i], A[j] = A[j], A[i]
      i = i + 1
  A[l], A[i - 1] = A[i - 1], A[l]
  return i - 1

def ChoosePivotLeft(A, l, r):
  return l

def ChoosePivotRight(A, l, r):
  return r

def ChoosePivotMedian(A, l, r):
  length = (r - l + 1)
  if length % 2 == 0:
    m = l + (length / 2) - 1
  else:
    m = l + length / 2 

  a = [A[l], A[m], A[r]]
  a.sort()

  if a[1] == A[l]:
    return l
  if a[1] == A[m]:
    return m
  if a[1] == A[r]:
    return r

def QuickSort(A, l, r):
  if r - l <= 0:
    return 0

  pindex = ChoosePivotLeft(A, l, r)
  A[l], A[pindex] = A[pindex], A[l]
  pindex = Partition(A, l, r)
  l_comparisons = QuickSort(A, l, pindex - 1)
  r_comparisons = QuickSort(A, pindex + 1, r)

  return (pindex - l) + (r - pindex) + l_comparisons + r_comparisons

f = open(sys.argv[1])
array = [int(l) for l in f.readlines()]
comparisons = QuickSort(array, 0, len(array) - 1)

print comparisons