def pointMutations(filepath='genefiles/rosalind_hamm.txt'):
    with open(filepath, mode='r') as file:
        seq = file.readlines()
        seq1 = seq[0].strip()
        seq2 = seq[1].strip()

    hamming_distance = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            hamming_distance += 1
    return hamming_distance


res = pointMutations()
print(res)           