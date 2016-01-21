import sys

__author__ = 'Andrew, Myles, Robert'

with open("MSS_Problems.txt") as inFile:
    testArray = ''.join(inFile.readline())
    testArray = testArray.replace("[", "").replace(",", "").replace("]", "").split()
    testArray = map(int, testArray)

if len(sys.argv) > 1:
    algorithmToRun = sys.argv[1]
else:
    print("Please specify algorithm you want to use as an argument.")
    print("eg. python maxSubArray.py <Algorithm Number>")
    print("Algorithm #1 - Enumeration")
    print("Algorithm #2 - Better Enumeration")
    print("Algorithm #3 - Divide and Conquer")
    print("Algorithm #4 - Linear-Time")
    sys.exit()

print ("ARRAY INPUT:")
print (testArray)
print ("\n")

def maxSubArrayEnum(numList):
    start, end, maxSum = 0, 0, 0

    for i in range(0, len(numList)):
        for j in range(i, len(numList)):
            tempSum = sum(numList[i:j])
            if maxSum < tempSum:
                maxSum = tempSum
                start, end = j, i
    return (start, end, maxSum)

def maxSubArrayEnum2(numList):
    start, end, maxSum, newStart, tempSum = 0, 0, 0, 0, 0

    for i, j in enumerate(numList): #this is just one loop, i is the index and j is the value
        tempSum += j
        if maxSum < tempSum:
            maxSum = tempSum
            start, end = newStart, i
        elif tempSum < 0: #if we have a subarray that dips below zero, it is a negative sequence so just dump it and start over
            tempSum = 0
            newStart = i

    return (start, end, maxSum)


def divideConquer(array, left, right):
    if (left == right): # if only one element
        return array[left]

    middle = (left+right)/2 #store the middle index, will be used to divide array into halves
    leftSub = divideConquer(array, left, middle) #leftSub will contain left half of array
    rightSub = divideConquer(array, middle+1, right) #rightSub will contain right half of array
    leftMax = 0
    rightMax = 0
    tempMax = 0
    for i in range(middle, -1, -1): #backwards loop starting at middle to 0, find max sub array of left sub
        tempMax += array[i]

        if(tempMax > leftMax):
            leftMax = tempMax

    tempMax = 0
    for i in range(middle+1, right): # loop for right sub, find max array of right sub
        tempMax += array[i]
        print tempMax
        if(tempMax > rightMax):
            rightMax = tempMax

    return max(max(leftMax, rightMax),leftMax+rightMax) #return max of three options


def maxSubArrayLT(numList):
    tempMax = maxSum = numList[0] #start with the first element of the array
    for x in numList[1:]:   #loop starting with the 2nc element in array
        tempMax = max(x, tempMax + x) #set next equal to max of current element, and next + current element
        maxSum = max(maxSum, tempMax) #compar maxSum to tempMax and set maxSum to the greater of the two
    return maxSum

def printResult(algorithm):    
        print algorithm(testArray)

def printResultDC(algorithm, start, end):
    print algorithm(testArray, start, end)

if (algorithmToRun == "Algorithm 1" or algorithmToRun == "1"):
    print("Using enumeration algorithm:")
    printResult(maxSubArrayEnum)
elif (algorithmToRun == "Algorithm 2" or algorithmToRun == "2"):
    print("Using better enumeration algorithm:")
    printResult(maxSubArrayEnum2)
elif (algorithmToRun == "Algorithm 3" or algorithmToRun == "3"):
    print("Using divide and conquer algorithm:")
    printResultDC(divideConquer, 0, len(testArray) - 1)
elif (algorithmToRun == "Algorithm 4" or algorithmToRun == "4"):
    print("Using Linear-Time algorithm:")
    printResult(maxSubArrayLT)
