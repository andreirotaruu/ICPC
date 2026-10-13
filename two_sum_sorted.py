def main():
    target = 10
    nums = [2,5,9,8,7,3]
    left = 0
    right = len(nums) - 1
    nums.sort()
    while left <= right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            break


    print(f"Answer: {nums[left]} {nums[right]}")





if __name__ == "__main__":
    main()