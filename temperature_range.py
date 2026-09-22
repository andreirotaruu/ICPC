num_inp = "5"
inp = "72, 68 ,75, 64, 70"
num_temps = int(num_inp)


max_num = 0
min_num = 999999
max_index = 0

for i in range(len(inp)):
    if not inp[i].isdigit():
        del(inp[i])

for i in range(0, len(inp), 2):
    end = i + 2
    num = int(inp[i:end])

    if num > max_num:
        max_num = num
        max_index = i
    elif num < min_num:
        min_num = num


print(f'Min num: {min_num}')
print(f'Max num: {max_num}')
print(f'Range: {max_num - min_num}')


