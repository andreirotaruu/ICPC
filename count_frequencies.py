def main():

    nums = [2,5,2,3,5,2,4,5]
    nums.sort()
    current = 0
    highest_frequency = 0
    curr_freq = 0
    highest_frequency_value = 0 
    for num in nums:
        if num == current:
            curr_freq += 1
        else:
            current = num
            curr_freq = 1

        if curr_freq > highest_frequency:
            highest_frequency = curr_freq
            highest_frequency_value = current

    print(f'Max Freq: {highest_frequency_value}')
    











if __name__ == "__main__":
    main()