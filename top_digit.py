def top_digit():
    inp = input()
    range_vals = inp.split()
    low = int(range_vals[0])
    n = int(range_vals[1])

    prime = [True] * (n + 1)

    p = 2
    while p*p <= n:
        if prime[p]:

            #mark all multiples of p as non-primes
            for i in range(p*p, n + 1, p):
                prime[i] = False

        p += 1

    #collect all prime numbers
    res = []
    for p in range(max(low, 2), n + 1):
        if prime[p]:
            res.append(p)

    counts = {}
    res_str = ""
    for num in res:
        res_str+=str(num)

    for c in res_str:
        counts[c] = counts.get(c, 0) + 1

    max_count = -1
    answer = 0
    for digit in range(10):
        count = counts.get(str(digit), 0)

        if count > max_count:
            max_count = count
            answer = digit

    print(answer)

if __name__ == "__main__":
    top_digit()