def BiSearch(UBound, LBound, key, myList):
    if UBound >= LBound:
        mid = (UBound+LBound)//2
        if myList[mid]==key:
            return mid
        elif myList[mid]<key:
            LBound = mid + 1
            return BiSearch(UBound, LBound, key, myList)
        elif myList[mid]>key:
            UBound = mid - 1
            return BiSearch(UBound, LBound, key, myList)
    else:
        return -1

myList = []
n = int(input("Enter number of elements in the List:\n"))
for j in range(0,n):
    element = int(input("Input elements in Ascending order:\n"))
    myList.append(element)
print("Your list is "+str(myList))

key = int(input("Enter the value of the element you'd like to search for\n"))

result = BiSearch(len(myList)-1, 0, key, myList)

if result != -1:
    print("The Element"+str(key)+"is found at the "+str(result+1)+"th position")
else:
    print("The value "+str(key)+" has not been found in the array")
