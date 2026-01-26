# Count frequency of elements in a list
def frequency_count(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq


nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result = frequency_count(nums)
print(result)
