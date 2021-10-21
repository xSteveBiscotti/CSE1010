#def check_reverse(string):
    # your code goes here
#    txt = string
#    txt2 = string[::-1]
#    
#    if txt == txt2:
#        print('True')
#    else:
#        print('False')
#
#check_reverse('abc')

#def fib(num):
#    lst = [0,1]
#    for i in range(num):
#        fibarr = lst[-2:]
        #consider a line of code here so that the lst become a fib sequence
#        lst.append(fibarr[0] + fibarr[1])
#    return lst

#fib(6)

#def swapIntegers(A, index1, index2):
#    try:
#        num1 = A[index1]
#        num2 = A[index2]
#        newList = A
        #print(A)
        #A.insert(index1,num1)
        #print(A)
        #A.insert(index2,num2)
        #print(A)
        #del A[index1]
        #del A[index2 + 1]
        #print(A)
#        del newList[index2]
        #print(A)
#        newList.insert(index2, num1)
        #print(A)
#        del newList[index1]
        #print(A)
#        newList.insert(index1,num2)
#        A = newList
#        return A
#    except IndexError:
#        A = None
#        index1 = None
#        index2 = None
#        return -1 
    
#if __name__ == '__main__':
    # you can use this to test your code
#    print(swapIntegers([1, 2, 3, 4], 2, 6))
    #swapIntegers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4, 7)

#def removeDuplicates(input_list):
#    newList = []
    # your code here
    # remember to return appropriate value
    #count = 0
    #for i in input_list:
    #    if i in input_list:
    #        del input_list[count]
    #        count += 1
    #count +=1
#    for i in input_list:
#        if i not in newList:
#            newList.append(i)

#    return newList
    
#if __name__ == '__main__':
    # you can use this to test your code
#    print(removeDuplicates([5, 0, 0, 1, 2, -1, 1, 5]))


            
        
    
    
def count_pairs(socks):
    # your code goes here
    #total number of socks
    totalsocks = len(socks)
    #sock sizes sorted
    socks.sort()
    #number of pairs
    pairs = 0
    i = 0
    j = (totalsocks - 1)
    while i<j:
        if socks[i] == socks[i+1]:
            pairs += 1
            i += 2
        else:
            i += 1
            
    return pairs
    
    
    
    
if __name__ == "__main__":
    # first, we split the input line on whitespace
    # this problem can use a list of strings or integers
    nums = input().split() 
    total = count_pairs(nums) 
    print(total)
