def reverse_complement(file_path):
    """
    Returns the complementary DNA of a gene sequence
    """
    try:
        with open(file_path, 'r') as dna_files:
            dnas = dna_files.read()
            dna_map = {'A':'T', 'G':'C', 'C':'G', 'T':'A'}
            rcDNA = ''.join([dna_map[base] for base in dnas.strip('\n')])
    
        #writing into a file
        with open('outputs/rcdna.txt', mode='w+', encoding='utf-8') as output:
            output.write(rcDNA[::-1])
    except FileNotFoundError as err:
        print(err, ': File doesn\'t exist')



file_path = 'genefiles/rosalind_revc.txt'
rcdna = reverse_complement(file_path)