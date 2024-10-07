def findSecondLargestNumber(nums):
    if len(nums) > 1:
        nums.sort()
        return nums[-2]
    else:
        return None

number_list = list(map(int, input("Enter a list of numbers: ").split(",")))
secondLargestNumber = findSecondLargestNumber(number_list)
print(secondLargestNumber)