def factorielle(n):
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat


def zeros_naif(n):
    f = factorielle(n)
    total = 0
    while f % 10 == 0:
        f //= 10
        total += 1
    return total


for n in [5,6, 10, 15, 20, 24, 25, 30]:
    print(f"{n}! = {factorielle(n)}  →  {zeros_naif(n)} zéro(s)")
