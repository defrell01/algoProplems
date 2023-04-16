# need to return the triplets of integers which sum is eq to the target one
# O(n^2) time O(n) space 
def threeNumSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets



sampleArray = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

print(threeNumSum(sampleArray, targetSum))


## just as two num sum we sort an array to walk through
## we've got two loops first one iterates through the very beginning
# and 'till the end of it and other one is two pointers - left and right
# firstly we calculate the current sum and if it fits we put it into the triplets array and inc
# left pointer and the second
# if sum is smaller than target we inc left index and oppositely we decrement right one