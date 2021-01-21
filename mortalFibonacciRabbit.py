def mortalFibRabbits(n,m):
    count = 1 # rabbit at 1st month
    ages = [0] * m
    ages[-1] = 1 #alive rabbit with m months to live
    while count < n:
        # newborns
        new = sum(ages[:-1])
        # shift ages left ie rabbit getting older
        ages[:-1] =  ages[1:]
        # asssign newborns
        ages[-1] = new       
        count += 1
    return sum(ages)


"""
This algorithm tracks the number of rabbits at each month,
"""
def fib(n, m):
    pop = [1,0] # num mature, num small
    for i in range(1,n):
        pop.insert(0,  sum(pop[1:m]))
        if len(pop) > m:
            pop.pop()
    return sum(pop[:m])

print(fib(94, 16))

# res = mortalFibRabbits(12,4)
# print(res)

with open('genefiles/rosalind_fibd.txt') as file:
    mortal_rabbit = file.read()
    mortal_rabbit= mortal_rabbit.split()
    month = int(mortal_rabbit[0])
    death_month = int(mortal_rabbit[1])
    res = mortalFibRabbits(month, death_month)
    print(res)
