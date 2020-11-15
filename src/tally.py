class Tally(object):
    ''' Manages rank checkpoints and handles rank queries, which are
        O(1) time, with the checkpoints taking O(m) space, where m is
        length of text. '''

    def __init__(self, bw, checkpoint_interval=4):
        ''' Scan BWT, creating periodic checkpoints as we go '''
        self.checkpoints = {}  # checkpoints
        self.checkpoint_interval = checkpoint_interval  # spacing between checkpoints
        tally = {}  # tally so far
        # Create an entry in tally dictionary and checkpoint map for
        # each distinct character in text
        for c in bw:
            if c not in tally:
                tally[c] = 0
                self.checkpoints[c] = []
        # Now build the checkpoints
        for i, c in enumerate(bw):
            tally[c] += 1  # up to *and including*
            if i % checkpoint_interval == 0:
                for c in tally.keys():
                    self.checkpoints[c].append(tally[c])

    def rank(self, bw, c, row):
        ''' Return # c's there are in bw up to and including row '''
        if row < 0 or c not in self.checkpoints:
            return 0
        i, nocc = row, 0
        # Always walk to left (up) when calculating rank
        while (i % self.checkpoint_interval) != 0:
            if bw[i] == c:
                nocc += 1
            i -= 1
        return self.checkpoints[c][i // self.checkpoint_interval] + nocc