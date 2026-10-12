def main():
    target = 10
    nums = [2,5,9,8,7,3]
    comps = {}

    for num in nums:
        compl = target - num

        if compl in comps:
            break

        comps[num] = compl

    print(f"Answer: {target - compl} {compl}")

if __name__ == "__main__":
    main()