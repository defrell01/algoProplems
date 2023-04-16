# need to find the smallest difference between elements in two arrays
# O(nlog(n) + nlog(m)) time O(1) space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    firstIdx = 0
    secondIdx = 0

    smallest = float("inf")
    current = float("inf")

    smallestPair = []

    while firstIdx < len(arrayOne) and secondIdx < len(arrayTwo):
        
        firstNum = arrayOne[firstIdx]
        secondNum = arrayTwo[secondIdx]

        if firstNum < secondNum:
            current = secondNum - firstNum
            firstIdx += 1
        
        elif secondNum < firstNum:
            current = firstNum - secondNum
            secondIdx += 1
        
        else:
            return [firstNum, secondNum]
        
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    
    return smallestPair


arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

print(smallestDifference(arrayOne, arrayTwo))

# i use two pointers to walk through arrays both sorted
# if number from the first one if less than number from the second one 
# then i increment first pointer to make it greater and of course save the current diff
# if second element is less than i increment second index
# if two numbers are eq - that is it
# and the end of the loop we compare current diff and the smallest one
# and depends on that we assign the new one or not