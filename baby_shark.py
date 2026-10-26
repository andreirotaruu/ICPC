
def main():
    inp = "baby baby shark shark shark doo doo"
    words = inp.split()

    count = 1
    max_count = 0
    max_word = " "
    prev = words[0]
    for i in range(1, len(words)):

        if words[i] == prev:
            count += 1 
        else:
            count = 1

        if count > max_count:
            max_count = count
            max_word = words[i]

        prev = words[i]

    print(f"Most frequent word {max_word}")






if __name__ == "__main__":
    main()