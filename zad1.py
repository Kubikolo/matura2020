def primes_to_n(n):
    candidates = list(range(2, n + 1))
    primes = []

    while len(candidates) != 0:
        prime = candidates[0]
        to_go = [prime * x for x in range(1, n // prime + 1)]
        for i in to_go:
            if i in candidates:
                candidates.remove(i)
        primes.append(prime)

    return primes


def goldbach(n):
    primes = primes_to_n(n)
    for i in primes:
        if n - i in primes:
            return i, n - i
    raise ValueError


file_path = r"./Dane_PR2/pary.txt"
with open(file_path, "r") as f:
    raw_data = f.readlines()

numbers = [int(x.split(" ")[0]) for x in raw_data]
numbers = [x for x in numbers if x % 2 == 0 and x > 4]

for number in numbers:
    prime1, prime2 = goldbach(number)
    print(number, prime1, prime2)

