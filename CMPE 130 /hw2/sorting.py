# 1. selection sort
# 2. insertion sort
# 3. shell sort
# 4. heap sort
# 5. merge sort
# 6. quick sort

import time
import random
import matplotlib.pyplot as plt
import timing as timing


class Sorting(object):
    """Sorting class
       Assignment by Alam Figueroa
    """

    def __init__(self):
        self.id = []

    def sort_init(self, N):
        """initialize the data structure

        """

        try:
            self.id = random.sample(range(1, N ** 3), N)
        except ValueError:
            print('Sample size exceeded population size.')

        # self.id = [random.randint(0, N - 1) for i in range(N)]

    def get_id(self):
        """initialize the data structure

        """

        return self.id

    def swapvar(self, a, b):
        temp = self.id[a]
        self.id[a] = self.id[b]
        self.id[b] = temp

    def selection_sort(self):
        """Selection sort algorithm is an
        in-place comparison sort. It has O(n^2) time complexity, making it
        inefficient on large lists, and generally performs worse than the
        similar insertion sort

        """
        for i_idx, i_item in enumerate(self.id):
            mini = i_idx
            for j_idx in range(i_idx + 1, len(self.id)):
                if self.id[j_idx] < self.id[mini]:
                    mini = j_idx
            # swap
            temp = self.id[i_idx]
            self.id[i_idx] = self.id[mini]
            self.id[mini] = temp
        return 1

    def insertion_sort(self):
        """Insertion sort is a simple sorting algorithm that builds the final
        sorted array (or list) one item at a time. More efficient in practice
        than most other simple quadratic (i.e., O(n^2)) algorithms such as
        selection sort or bubble sort specifically an

        """
        for idx in range(len(self.id)):
            j = self.id[idx]
            while j > 0 and self.id[idx] < self.id[idx - 1]:
                temp = self.id[idx - 1]
                self.id[idx - 1] = self.id[idx]
                self.id[idx] = temp
                j = j - 1
        return 1

    def shell_sort(self):
        """Shell sort also known as  or Shell's method, is an in-place comparison sort.
        It can be seen as either a generalization of sorting by exchange (bubble sort)
        or sorting by insertion (insertion sort).

        """
        h = 1
        while h < len(self.id) / 3:
            h = 3 * h + 1

        while h >= 1:
            i = h
            while i < len(self.id):
                j = i
                while j >= h and self.id[j] < self.id[j - h]:
                    b = j - h
                    # self.swapvar(self, j, b)
                    self.id[j], self.id[b] = self.id[b], self.id[j]
                    j += 1
                i += 1
        return 1

    # To heapify subtree rooted at index i.
    # n is size of heap
    def heapify(self, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and self.id[i] < self.id[l]:
            largest = l

            # See if right child of root exists and is
        # greater than root
        if r < n and self.id[largest] < self.id[r]:
            largest = r

            # Change root, if needed
        if largest != i:
            self.id[i], self.id[largest] = self.id[largest], self.id[i]  # swap

            # Heapify the root.
            self.heapify(self, n, largest)
        return 0

    def heap_sort(self):
        """Heapsort is an improved selection sort: it divides its input into a sorted
        and an unsorted region, and it iteratively shrinks the unsorted region by
        extracting the largest element and moving that to the sorted region.

        """
        n = len(self.id)

        # Build a maxheap.
        for i in range(n, -1, -1):
            self.heapify(self, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            self.id[i], self.id[0] = self.id[0], self.id[i]  # swap
            self.heapify(self, i, 0)
        return 1

    def compare(self, indx1, indx2):

        return 1

    def heapUp(self, indx):
        while indx > 1 and self.compare(self.id, indx / 2, indx):
            half = indx / 2
            # self.swapvar(self, indx, b)
            self.id[indx], self.id[indx / 2] = self.id[indx / 2], self.id[indx]
            indx /= 2
        return 1

    def merge(self, temp, lo, mid, hi):
        k = lo
        while k <= hi:
            temp[k] = self.id[k]
            k += 1

        i = lo, j = mid + 1
        k = lo
        while k <= hi:
            if i > mid:
                self.id[k] = temp[j + 1]
            elif j > hi:
                self.id[k] = temp[i + 1]
            elif temp[j] < temp[i]:
                self.id[k] = temp[j + 1]
            else:
                self.id[k] = temp[i + 1]
        return 1

    def mergeSort(self, temp, lo, hi):
        if hi <= lo: return

        mid = lo + (hi - lo)
        self.mergeSort(self, temp, lo, mid)
        self.mergeSort(self, temp, mid + 1, hi)
        self.merge(self, temp, lo, mid, hi)
        return 1

    def merge_sort(self):
        """Merge sort is a divide and conquer algorithm that was invented
        by John von Neumann in 1945. Most implementations produce a stable
        sort, which means that the implementation preserves the input order
        of equal elements in the sorted output.
        """
        temp = []
        self.mergeSort(self, temp, 0, (len(self.id)) - 1)
        return 1

    def shuffle(self):
        for i in range(len(self.id)):
            r = random.randint(0, i + 1)
            # self.swapvar(self, i, r)
            self.id[i], self.id[r] = self.id[r], self.id[i]
        return 1

    def partition(self, lo, hi):
        i = lo, j = hi + 1
        while 1:
            while self.id[i + 1] < self.id[lo]:
                if i == hi: break
            while self.id[lo] < self.id[j - 1]:
                if j == lo: break

            if i >= j: break
            # self.swapvar(self, i, b)
            self.id[i], self.id[j] = self.id[j], self.id[i]
        # self.swap(self, lo, b)
        self.id[lo], self.id[j] = self.id[j], self.id[lo]
        return j

    def qsort(self, lo, hi):
        if hi <= lo: return 0
        j = self.partition(self, lo, hi)
        self.qsort(self, lo, j - 1)
        self.qsort(self, j + 1, hi)
        return 1

    def quick_sort(self):
        """Quicksort (sometimes called partition-exchange sort) is an efficient
        sorting algorithm. Developed by Tony Hoare in 1959. It is still a commonly
        used algorithm for sorting. When implemented well, it can be about two or
        three times faster than its main competitors, merge sort and heapsort.

        """
        self.shuffle(self)
        self.Qsort(self, 0, len(self.id) - 1)
        return 1

    # this plots things in log scale (pls google it), you need to add matplotlib
    # to your virtualenv first!

    # plot also python's sorted() function to see how well you do.


    plt.plot(10 ^ 1, timing)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('log')
    plt.ylabel('some numbers')
    plt.show()
