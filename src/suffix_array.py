class SuffixArray():

    def __init__(self, t, ssa_interval=4):
        if t[-1] != '$':
            t += '$'  # add dollar if not there already
        # Get BWT string and offset of $ within it
        self.sa = self.suffixArray(t)
        self.bwt = self.bwtFromSa(t, self.sa)
        # Get downsampled suffix array, taking every 1 out of 'ssaIval'
        # elements w/r/t T
        self.ssa = self.downsampleSuffixArray(self.sa, ssa_interval)

    def suffixArray(self, s):
        ''' Given T return suffix array SA(T).  Uses "sorted"
        function for simplicity, which is probably very slow. '''
        satups = sorted([(s[i:], i) for i in range(len(s))])
        return list(map(lambda x: x[1], satups))  # extract, return just offsets

    def bwtFromSa(self, t, sa):
        ''' Given T, returns BWT(T) by way of the suffix array. '''
        bw = []
        for si in sa:
            if si == 0:
                bw.append('$')
            else:
                bw.append(t[si - 1])
        return ''.join(bw)  # return string-ized version of list bw

    def downsampleSuffixArray(self, sa, n=4):
        ''' Take only the suffix-array entries for every nth suffix.  Keep
            suffixes at offsets 0, n, 2n, etc with respect to the text.
            Return map from the rows to their suffix-array values. '''
        ssa = {}
        for i, suf in enumerate(sa):
            # We could use i % n instead of sa[i] % n, but we lose the
            # constant-time guarantee for resolutions
            if suf % n == 0:
                ssa[i] = suf
        return ssa