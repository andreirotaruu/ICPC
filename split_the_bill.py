def main():
    inp = "5 3 17 3 15"

    inputs = inp.split()
    n = int(inp[0])
    meals = inp[1]

    remainders = 0
    for i in range(2, len(inputs)):
        remainder = int(inputs[i]) % n
        if remainder == 0:
            continue

        remainders += remainder

    if remainders % n != 0:
        print(0)
    else:
        print(1)


if __name__ == "__main__":
    main()