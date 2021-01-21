import csv
try:
    with open('genefiles/rosalind_dna.txt') as dna_files:
        genes = dna_files.read()
        genes = genes.upper()
        print(len(genes))

        ade = genes.count('A')
        thy = genes.count('T')
        cyt = genes.count('C')
        gua = genes.count('G')

    #writing into a file
    with open('outputs/dna_count.txt', 'a+') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        rows = map(str, [ade, gua, cyt, thy])
        csv_writer.writerows([rows])

except FileNotFoundError as err:
    print(err, ':File doesn\'t exist')