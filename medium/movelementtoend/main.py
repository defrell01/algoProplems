# i need to move elements in the array to its end without maintaining other elements order
# O(n) time o(1) space
def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1

    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        
        i += 1
    return array

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

print(moveElementToEnd(array, toMove))

#i've got to pointers to end of array and the begining
# and if the last one is good i move j pointer to the beginning
# if first pointer element is eq to toMove i swap it with the j pointer element
# end after that we increment the first pointer