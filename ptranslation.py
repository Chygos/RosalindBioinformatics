protein_map = {
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",

    "UGU":"C", "UGC":"C", "GAU":"D", "GAC":"D",
    
    "GAA":"E", "GAG":"E", "UUU":"F", "UUC":"F",
    
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",
    
    "CAU":"H", "CAC":"H", "AUA":"I", "AUU":"I", 
    
    "AUC":"I", "AAA":"K", "AAG":"K", "UUA":"L", 
    
    "UUG":"L", "CUU":"L", "CUC":"L", "CUA":"L", 
    
    "CUG":"L", "AUG":"M", "AAU":"N", "AAC":"N", 
    
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    
    "CAA":"Q", "CAG":"Q", "CGU":"R", "CGC":"R", 
    
    "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R",
    
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", 
    
    "AGU":"S", "AGC":"S", "ACU":"T", "ACC":"T", 
    
    "ACA":"T", "ACG":"T", "GUU":"V", "GUC":"V", 
    
    "GUA":"V", "GUG":"V", "UGG":"W", "UAU":"Y", 
    
    "UAC":"Y", "UAA":"_", "UAG":"_", "UGA":"_"
}


def translation(filepath):
    with open('genefiles/rosalind_prot.txt', 'r') as file:
        rna_seq = file.read()
        rna_seq = rna_seq.strip()
    
    proteins = ''
    for i in range(0, len(rna_seq)-3, 3):
        codon = rna_seq[i:i+3]
        amino_acid = protein_map[codon]
        proteins += amino_acid
    return proteins


if __name__ == '__main__':
    res = translation('genefiles/rosalind_prot.txt')
    print(res)


