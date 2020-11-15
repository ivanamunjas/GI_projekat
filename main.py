from src.fm_index import FmIndex

if __name__ == '__main__':

    s = 'abaaba'
    fm = FmIndex(s)
    substrings = ['abaa', 'baaaa', 'baab', 'abaaba']
    for substr in substrings:
        print("{} is a substring of {}? {}".format(substr, s, fm.hasSubstring(substr)))
    suffixes = ['aba', 'bbba', 'baaba']
    for suff in suffixes:
        print("{} is a suffix of {}? {}".format(suff, s, fm.hasSuffix(suff)))
    occurences = ['ab', 'baab', 'ba', 'bba', 'abaaba']
    for occ in occurences:
        print("{} occurs in {} at these indicies: {}".format(occ, s, fm.occurrences(occ)))

    s = 'TTGTGTGCATGTTGTTTCATCATTTAGAGATACATTGCGCTGCATCATGGTCA'
    fm = FmIndex(s)
    substrings = ['GCATGTTGTTTCA', 'GTTGTTACTCCATTTAGAGATACA', 'AGAGATACAT', 'ACATTGCGCTGCTATGGT'] #true false true false
    for substr in substrings:
        print("{} is a substring of {}? {}".format(substr, s, fm.hasSubstring(substr)))
    suffixes = ['TGGTCA', 'ATACATTGCGC', 'TTGCGCTGCATCATGGTCA'] # true false true
    for suff in suffixes:
        print("{} is a suffix of {}? {}".format(suff, s, fm.hasSuffix(suff)))
    occurences = ['GTGCATGTTGTTTCA', 'CAT', 'TG', 'CCCC', 'GTTTCATCATTTAGAGATACATTGCGC']
    for occ in occurences:
        print("{} occurs in {} at these indicies: {}".format(occ, s, fm.occurrences(occ)))


