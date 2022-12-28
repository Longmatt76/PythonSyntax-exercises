def in_range(nums, lowest, highest):
    for num in nums:
        if num >= lowest and num <= highest:
            print(num)
