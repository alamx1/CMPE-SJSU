

# 1. quick-find
# 2. quick-union
# 3. weighted QU
# 4. QU + path compression
# 5. weighted QU + path compression

import random
import time
import matplotlib.pyplot as plt


class UF(object):
    """Union Find class

    """

    def __init__(self):
        self.id = []
        self.sz = []


    def qf_init(self, N):
        """initialize the data structure

        """
        for x in range(N):
            self.id.append(x)
            self.sz.append(1)

    def qf_union(self, p, q):
        """Union operation for Quick-Find Algorithm.

        connect p and q. You need to
        change all entries with id[p] to id[q]
        (linear number of array accesses)

        """
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid
        #return 1


    def qf_connected(self, p, q):
        """Find operation for Quick-Find Algorithm.
        simply test whether p and q are connected

        """

        return self.id[p] == self.id[q]
        #return True

    def root(self, i):
        while i != id[i]:
            i = id[i]
        return i

    def qu_union(self, p, q):
        """Union operation for Quick-Union Algorithm.
         connect p and q.

         """
        i = self.root(self, p)
        j = self.root(self, q)
        self.id[i] = j
        #return 1

    def qu_connected(self, p, q):
        """Find operation for Quick-Union Algorithm.
         test whether p and q are connected

         """

        #return True
        return self.root(self, p) == self.root(self, q)


    def wqu_union(self, p, q):
        """Union operation for Weighted Quick-Union Algorithm.
         connect p and q.

         """
        i = self.root(self, p)
        j = self.root(self, q)
        if sz[i] < sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.sz[j] = i
            self.sz[i] += self.sz[j]
        #return 1


    def wqu_connected(self, p, q):
        """Find operation for Weighted Quick-Union Algorithm.
         test whether p and q are connected

         """
        return self.root(self, p) == self.root(self, q)
        #return True

    def pqu_root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def pqu_union(self, p, q):
        """Union operation for path compressed Quick-Union Algorithm.
         connect p and q.

         """
        i = self.pqu_root(self, p)
        j = self.pqu_root(self, q)
        self.id[i] = j
        #return 1


    def pqu_connected(self, p, q):
        """Find operation for path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """
        return self.pqu_root(self, p) == self.pqu_root(self, q)
        #return True

    def wpqu_union(self, p, q):
        """Union operation for Weighted path compressed Quick-Union Algorithm.
         connect p and q.

         """
        i = self.pqu_root(self, p)
        j = self.pqu_root(self, q)
        if sz[i] < sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.sz[j] = i
            self.sz[i] += self.sz[j]
        #return 1


    def wpqu_connected(self, p, q):
        """Find operation for Weighted path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """
        return self.pqu_root(self, p) == self.pqu_root(self, q)
        #return True

if __name__ == "__main__":

    # iteration
    set_szs = [10]
    timing = []

    # gives the timing for union operation only, you might want to do this for all functions you wrote.
    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            inodes.qf_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    # this plots things in log scale (pls google it), you need to add matplotlib to your virtualenv first!


    plt.plot(set_szs, timing)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('log')
    plt.ylabel('some numbers')
    plt.show()