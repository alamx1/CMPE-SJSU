import time
import random


class Array_Search:
    def __init__(self, array):
        self.array = array

    def init_array_search(self, val_array):
        self.array = Array_Search(val_array)

    def squential_search(self, key):

        idx = 0
        for num in self.array:
            if num == key:
                return idx
            idx = idx+1
        return False

    def bsearch(self, val):
        l = 0
        r = len(self.array)-1
        mid = (l+r)/2
        while l <= r:
            if val == self.array[mid]:
                return mid
            elif val > self.array[mid]:
                l = mid + 1
                mid = (l+r) / 2
            else:
                r = mid - 1
                mid = (l+r) / 2
        return -1


class BST_Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def init_bst(self, val):
        self.root = BST_Node(val)

    def insert(self, val):
        if self.root is None:
            self.init_bst(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):
        if current is None:
            current.val = val
        else:
            if current.val < val.val:
                if current.right is None:
                    current.right = val
                else:
                    self.insert(current.right, val)
            else:
                if current.left is None:
                    current.left = val
                else:
                    self.insert(current.left, val)
        return False

    def bsearch(self, val):
        temp = self.root
        while temp:
            if val == temp.val:
                return True
            elif val > temp.right.val:
                temp = temp.right
            else:
                temp = temp.left
        return False

    def searchNode(self, current, val):
        if val == current.val:
            return True
        elif val > current.val:
            self.searchNode(self, current.right, val)
        elif val < current.val:
            self.searchNode(self, current.left, val)
        return False

    def minValueNode (current):
        while current.left is not None:
            current = current.left
        return current

    def delete(self, val):
        if self.root is None:
            return True

        current = self.root

        while current:
            if val < current.val:
                current = current.left

            elif val > current.val:
                current = current.right

            else:


                # Node with only one child or no child
                if current.left is None:
                    temp = current.right
                    current = None
                    return True

                elif current.right is None:
                    temp = current.left
                    current = None
                    return True

                # Node with two children: Get the inorder successor
                # (smallest in the right subtree)
                temp = self.minValueNode(current.right)

                # Copy the inorder successor's content to this node
                current.val = temp.val

                # Delete the inorder successor
                current.right = self.deleteNode(current.right, temp.val)

        return False



class RBBST_Node:
    def __init__(self, val, color):
        self.val = val
        self.left = None
        self.right = None
        self.color = color


RED = True
BLACK = False


class RBBST:
    def __init__(self):
        self.root = None

    def init_rbbst(self, val, color):
        self.root = RBBST_Node(val, color)

    def is_red(self, current):
        return current.color
        return False

    def rotate_left(self, current):
        x = current.right
        current.right = x.left
        x.left = current
        x.color = current.color
        current.color = RED
        return x

    def rotate_right(self, current):
        x = current.left
        current.left = x.right
        x.right = current
        x.color = current.color
        current.color = RED
        return x

    def flip_colors(self, current):
        if current.color == RED:
            current.color = BLACK
        else:
            current.color = RED
        return

    def insert(self, val):
        if (self.root is None):
            self.init_rbbst(val, RED)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):




        return False

    def bsearch(self, val):
        temp = self.root
        while temp is not None:
            if temp.val is val:
                return True
            elif temp.val < val:
                temp = temp.right
            elif temp.val > val:
                temp = temp.left
        return False

    def searchNode(self, current, val):
        while current:
            if current.val < val:
                self.searchNode(self,current.right,val)
            elif current.val > val:
                self.searchNode(self,current.left,val)
            else:
                return True
        return False


if __name__ == "__main__":

    # iteration
    set_szs = [10]
    timing = []