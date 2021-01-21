# To solve the prbability of getting a dominant allele, we can approach it in two ways
# 1. getting the probabilities of getting a dominant trait
# 2. getting the probabilities of getting a recessive trait and subtract from 1

# k == dominant in both alleles
# m == dominant in one allele and recessive in the other
# n == autosomal recessive

# In Mendelian law there's a 3/4 probability of getting a dominant gene and a 1/4 for recessive
# In this since we are selecting at random 2 species from k,m and n, without replacement, so all possible combinations
# KK, KM, MK, KN, NK, MN, NM, MM, NN
# Shorter way is to get all possible combinations of getting a recessive gene, which is
# a heterozygous x heterozygous, homozygous x homozygous, homozygous x heterozygous
# p(hetero x hetero) = 1/4, p(homo x homo) = 1, p(homo x hetero) = 2/4 = 1/2, p(hetero x homo) = 2/4 = 1/2

# ie [MM, MN, NM, NN]
# so 1 - p([MM + MN + NM + NN]) == p(Dominance)
# MM = m

def mendelLaw(filepath):
    with open(filepath, mode='r') as file:
        line = file.read()
        line = line.strip().split()
        k = int(line[0])
        m = int(line[1])
        n = int(line[2])

    popu = k + m + n
    C = popu * (popu - 1)
    mm = m * (m - 1) * 1/4 
    mn = m * n * 1/2
    nm = n * m * 1/2
    nn = n * (n-1) * 1

    pp = (mm + mn + nm + nn)
    p_recess = pp / C
    p_dom = round(1 - p_recess, 6)

    return p_dom

if __name__ == '__main__':
    res = mendelLaw('genefiles/rosalind_iprb.txt')
    print(res)
    

