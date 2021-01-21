try:
    with open('genefiles/rosalind_rna1.txt', 'r') as dna_files:
        bases = dna_files.read()
        rnas = bases.replace('T', 'U')

    #writing into a file
    with open('outputs/rna.txt', mode='w+', encoding='utf-8') as output:
        output.write(rnas)
        output.write('\nGene Length: '+ str(len(rnas)))

except FileNotFoundError as err:
    print(err, ': File doesn\'t exist')