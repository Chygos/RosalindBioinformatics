import re
import csv

def motifs(seq, pat):
    pat_list = []
    pattern = re.compile(pat)
    all_occurrences = re.finditer(pattern, seq)
    for match in all_occurrences:
        pat_list.append(match.span()[0]+1)
    return map(str, pat_list)


def findMotifs(seq, pat):
    starts = []
    for i in range(0, len(seq)):
        if seq[i:i+len(pat)] == pat:
            starts.append(str(i+1))
    return starts

if __name__ == '__main__':
    with open('genefiles/rosalind_subs.txt') as file:
        fi = [i.strip() for i in file.readlines()]
        seq = fi[0]
        pat = fi[1]

    res = findMotifs(seq, pat)
    res1 = motifs(seq, '(?='+pat+')')
    with open('outputs/rosalind_motif.txt', 'a+') as file:
        csv_writer = csv.writer(file, delimiter= ' ')
        csv_writer.writerow(res)
        csv_writer.writerow(res1)
    

# pat = '(?=ATAT)' (?=pat) gets overlapping matches
# seq = 'GATATATGCATATACTT'

# res = motifs(seq, pat)
# print(res)

# res = findMotifs(seq, 'ATAT')
# print(res)