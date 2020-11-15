from src.tally import Tally
from src.suffix_array import SuffixArray


class FmIndex():
    ''' O(m) size FM Index, where checkpoints and suffix array samples are
        spaced O(1) elements apart.  Queries like count() and range() are
        O(n) where n is the length of the query.  Finding all k
        occurrences of a length-n query string takes O(n + k) time.

        Note: The spacings in the suffix array sample and checkpoints can
        be chosen differently to achieve different bounds. '''

    def __init__(self, t, checkpoint_interval=4):

        SA = SuffixArray(t)
        self.bwt = SA.bwt
        self.bwt_len = len(self.bwt)
        self.ssa = SA.ssa
        # Make rank checkpoints
        self.checkpoints = Tally(self.bwt, checkpoint_interval)
        # Calculate # occurrences of each character
        total_occurrences = dict()
        print(self.bwt)
        for c in self.bwt:
            if c not in total_occurrences.keys():
                total_occurrences[c] = 0
            total_occurrences[c] += 1
        # Calculate concise representation of first column
        self.first_column = {}
        total_cnt = 0
        for c, count in sorted(total_occurrences.items()):
            self.first_column[c] = total_cnt
            total_cnt += count

    def range(self, p):
        ''' Return range of BWM rows having p as a prefix '''
        l, r = 0, self.bwt_len - 1  # closed (inclusive) interval
        for i in range(len(p) - 1, -1, -1):  # from right to left
            l = self.checkpoints.rank(self.bwt, p[i], l - 1) + self.first_column[p[i]]
            r = self.checkpoints.rank(self.bwt, p[i], r) + self.first_column[p[i]] - 1
            if r < l:
                break
        return l, r + 1

    def resolve(self, row):
        ''' Given BWM row, return its offset w/r/t T '''
        nsteps = 0
        while row not in self.ssa:
            if row >= self.bwt_len:
                return 0
            c = self.bwt[row]
            row = self.checkpoints.rank(self.bwt, c, row - 1) + self.first_column[c]
            nsteps += 1
        return self.ssa[row] + nsteps

    def hasSubstring(self, p):
        ''' Return true if and only if p is substring of indexed text '''
        l, r = self.range(p)
        return r > l

    def hasSuffix(self, p):
        ''' Return true if and only if p is suffix of indexed text '''
        l, r = self.range(p)
        off = self.resolve(l)
        if off == 0:
            return False
        return r > l and off + len(p) == self.bwt_len - 1

    def occurrences(self, p):
        ''' Return offsets for all occurrences of p, in no particular order '''
        l, r = self.range(p)
        occ = [self.resolve(x) for x in range(l, r)]
        return sorted(occ)