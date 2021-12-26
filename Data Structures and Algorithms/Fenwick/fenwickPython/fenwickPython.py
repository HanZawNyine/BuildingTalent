class FenWickTree:
    def getsum(self,BITTree, i):
        s = 0
        i = i + 1
        while i > 0:
            s += BITTree[i]
            i -= i & (-i)
        return s

    def updatebit(self,BITTree, n, i, v):
        i += 1
        while i <= n:
            BITTree[i] += v
            i += i & (-i)

    def construct(self,arr, n):
        BITTree = [0] * (n + 1)
        for i in range(n):
            self.updatebit(BITTree, n, i, arr[i])
        return BITTree

if __name__ == '__main__':
    # Driver code to test above methods
    fenwick = FenWickTree()
    freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    BITTree = fenwick.construct(freq, len(freq))
    print("Sum of elements in arr[0..5] is " + str(fenwick.getsum(BITTree, 5)))
    freq[3] += 6
    fenwick.updatebit(BITTree, len(freq), 3, 6)
    print("Sum of elements in arr[0..5]" +
          " after update is " + str(fenwick.getsum(BITTree, 5)))