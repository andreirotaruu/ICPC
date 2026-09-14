input = "1 2 3 4"

nums = input.split()
input_len = len(nums)
sum_nums = 0
for num in nums:
    sum_nums += int(num)
real_nums = [i + 1 for i in range(int(nums[-1]))]
sum_real = sum(real_nums)

print(f'The missing number is {abs(sum_nums - sum_real)}')
