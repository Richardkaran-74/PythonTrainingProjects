
def sort(nums):
    for i in range(3):
        minpos=i
        for j in range(i,4):
            if nums[j] < nums[minpos]:
                minpos = j

        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp

nums=[74,20,47,27]
sort(nums)

print(nums)