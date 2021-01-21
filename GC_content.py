def gc_content(gene_seq):
    """Returns the proportion of Guanine-Cytosine content in the gene sequence
    """
    from collections import Counter
    freq = Counter(gene_seq)

    gc_content = (freq['G'] + freq['C']) / sum(freq.values())
    return round(gc_content * 100, 6)


def textPreprocess(filepath='genefiles/rosalind_gc.txt'):
    """Preprocesses the sequences in FASTA files
    """
    import re
    pat = re.compile('>(\w+_\d{4})')

    seq_data = []
    seq_id = []

    with open(filepath, 'r') as file:
        for line in file:
            seq_data.append(line.strip()) # getting seqs
            
            # getting seq ids
            if line.startswith('>'):
                seq_id.append(line[1:].strip())
        # replacing pattern with spaces and spliting into lists
        subs = re.sub(pat,  ' ', ''.join(seq_data))
        subs = subs.split()
    return subs, seq_id


def max_GC_content(filepath='genefiles/rosalind_gc.txt'):
    """Gets seq_id with highest GC content
    """
    gc_contents = []
    gc_content_dict = {}
    seqs, seq_ids = textPreprocess(filepath)

    # getting gc contents
    for i in range(len(seqs)):
        gc = gc_content(seqs[i])
        gc_contents.append(gc)
        
        # putting  in dict
        gc_content_dict[gc] = seq_ids[i]
    
    # getting max gc
    max_gc = max(gc_contents)
    return seqs
    # return gc_content_dict.get(max_gc, None), max_gc


if __name__ == '__main__':
    res = max_GC_content()
    print(res)
    
