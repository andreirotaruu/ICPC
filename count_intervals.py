def main(): 
    inp = "3\n2 5\n4 8\n10 12"
    inp_arr = inp.split('\n')

    print(inp_arr)
    output_list = []
    num_intervals = inp_arr[0]
    for i in range(1, len(inp_arr)):
        current = inp_arr[i].split()
        new = [num for num in range(int(current[0]), int(current[1]))]
        for num in new:
            if num not in output_list:
                output_list.append(num)

    print(output_list)
    print(len(output_list))
if __name__ == "__main__":
    main()