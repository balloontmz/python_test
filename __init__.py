class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        a = []
        str = ''
        for y in range(len(s)):
            q = y // (2 * numRows - 2) * (numRows - 1)
            if y % (2 * numRows - 2) in list(x for x in range(numRows)):
                a[y % (2 * numRows - 2) + 1][q + 1] = s[y]
            else:
                z = y % (2 * numRows - 2) - numRows + 1
                a[numRows - z][q + z + 1] = s[y]

        if len(s) % (2*numRows-2) in list(x for x in range(numRows)):
            l = len(s) // (2 * numRows - 2) * (numRows - 1)  + 1
        else:
            zi = len(s) % (2 * numRows - 2) - numRows + 1
            l = len(s) // (2 * numRows - 2) * (numRows - 1) + zi + 1
        for m in range(1, numRows + 1):
            for n in range(1, l + 1):
                str = str.join(a[m][n])
        return str

