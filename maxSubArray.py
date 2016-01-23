import sys
import timeit
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

def maxSubArrayEnum(numList):
    start, end, maxSum = 0, 0, 0

    for i in range(0, len(numList)):
        for j in range(i, len(numList)):
            tempSum = sum(numList[i:j+1])
            if maxSum < tempSum:
                maxSum = tempSum
                start, end = i, j

    maxSumArray = numList[start:end+1]
    print "Max SubArray:",
    print maxSumArray, "\n"
    print "Max Sum:",
    print maxSum
    print "Runtime:",
    return maxSum

def maxSubArrayEnum2(numList):
    maxSum, tempSum = 0, 0

    for i in range(0, len(numList)): #this is just one loop, i is the index and j is the value
        tempSum = 0
        for j in range(i, len(numList)):
            tempSum += numList[j]
            if (tempSum > maxSum):
                maxSum = tempSum
                start, end = i, j

    maxSumArray = numList[start:end+1]
    print "Max SubArray:",
    print maxSumArray, "\n"
    print "Max Sum:",
    print maxSum
    print "Runtime:",
    return maxSum

def divideConquer(array, left, right):
    start = time.time()
    if (left == right): # if only one element
        return array[left]

    middle = (left+right)/2 # store the middle index, will be used to divide array into halves
    leftSub = divideConquer(array, left, middle) # leftSub will contain left half of array
    rightSub = divideConquer(array, middle+1, right) # rightSub will contain right half of array
    leftMax = 0
    rightMax = 0
    tempMax = 0
    # combined funtions maxPrefix and maxSuffix from pseudocode here
    for i in range(middle, -1, -1): # backwards loop starting at middle to 0, find max sub array of left sub
        tempMax += array[i]

        if(tempMax > leftMax):
            leftMax = tempMax

    tempMax = 0
    for i in range(middle+1, right+1): # loop for right sub, find max array of right sub
        tempMax += array[i]
        if(tempMax > rightMax):
            rightMax = tempMax

    print "Max SubArray:",
    print maxSumArray, "\n"
    print "Max Sum:",
    print maxSum
    print "Runtime:",

    return max(max(leftMax, rightMax),leftMax+rightMax) #return max of three options

def maxSubArrayLT(numList):
    bestSum = -sys.maxint - 1
    bestStart = bestEnd = -1
    localStart = localSum = 0
    for i in range(0, len(numList)):
        localSum += numList[i]
        if localSum > bestSum:
            bestSum = localSum
            bestStart = localStart
            bestEnd = i
        if localSum <= 0:
            localSum = 0
            localStart = i + 1

    maxSumArray = numList[bestStart:bestEnd+1]
    print "Max SubArray:"
    print maxSumArray, "\n"
    print "Max Sum:",
    print bestSum
    print "Runtime:",

    return bestSum

def printResult(algorithm):
        print algorithm(testArray)
def printResultDC(algorithm, start, end):
    print algorithm(testArray, start, end)

if (algorithmToRun == "Algorithm 1" or algorithmToRun == "1"):
    print("Using enumeration algorithm:")
    # printResult(maxSubArrayEnum)
    t1 = timeit.Timer( "maxSubArrayEnum(testArray)", "from __main__ import maxSubArrayEnum, testArray")
    print t1.timeit(number=1)
elif (algorithmToRun == "Algorithm 2" or algorithmToRun == "2"):
    print("Using better enumeration algorithm:")
    # printResult(maxSubArrayEnum2)
    t1 = timeit.Timer( "maxSubArrayEnum2(testArray)", "from __main__ import maxSubArrayEnum2, testArray")
    print t1.timeit(number=1)
elif (algorithmToRun == "Algorithm 3" or algorithmToRun == "3"):
    print("Using divide and conquer algorithm:")
    # printResultDC(divideConquer, 0, len(testArray) - 1)
    t1 = timeit.Timer( "divideConquer(testArray)", "from __main__ import divideConquer, testArray")
    print t1.timeit(number=1)
elif (algorithmToRun == "Algorithm 4" or algorithmToRun == "4"):
    print("Using Linear-Time algorithm:")
    # printResult(maxSubArrayLT)
    t1 = timeit.Timer( "maxSubArrayLT(testArray)", "from __main__ import maxSubArrayLT, testArray")
    print t1.timeit(number=1)
    
print ("\nArray Input:"),
print testArray
print ("\n")
