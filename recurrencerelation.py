def rabbit_recursive(n, k):
    if n < 2: return n
    else:
        return rabbit_recursive(n-1, k) + rabbit_recursive(n-2, k) * k


def rabbit_recurrence(n,k):
    count = 0
    fib1, fib2 = 1, 0  # pop in first month
    while count < n:
        nth =    fib1+fib2*k
        fib1, fib2 = nth, fib1
        count += 1
    return fib2


tot = rabbit_recurrence(5, 3)
print(tot)

# tot = rabbit_recursive(5, 3)
# print(tot)

# with open('genefiles/rosalind_fib.txt') as file:
#     rabbit = file.read()
#     rabbit = rabbit.split()
#     month = int(rabbit[0])
#     pairs = int(rabbit[1])
#     tot = rabbit_recurrence(month, pairs)
#     print(tot)

