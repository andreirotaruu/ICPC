def main():

    inp = [1, 2, 2, 3, 2, 2, 4, 5]
    freqs = {}
    max_val = 0
    for i in range(len(inp)):
        if i + 4 > len(inp):
            break
        for j in range(i, i + 4):
            freqs[inp[j]] = freqs.get(inp[j], 0) + 1
            if max(freqs.values()) > max_val:
                max_val = max(freqs.values())
        freqs = {}


    print(f"Max frequency: {max_val}")






if __name__ == "__main__":
    main()