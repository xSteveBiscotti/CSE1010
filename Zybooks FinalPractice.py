#Practice #2
def removeDuplicates(input_list):
    newList = []

    for i in input_list:
        if i not in newList:
            newList.append(i)
    
    return newList
    
if __name__ == '__main__':
    # you can use this to test your code
    print(removeDuplicates([5, 0, 0, 1, 2, -1, 1, 5]))

#Practice #3 
def removeDuplicates(input_list):
    newList = []

    for i in input_list:
        if i not in newList:
            newList.append(i)
    
    return newList
    
if __name__ == '__main__':
    # you can use this to test your code
    print(removeDuplicates([5, 0, 0, 1, 2, -1, 1, 5]))

#Practice #5
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
    
#Practice #7
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
    
#Practice #8
import pandas as pd

# returns the minimum value of column col for sex s
def get_min_by_sex(df,s,col):
    # complete this function

    newdf = df.query(f"sex=='{s}'")    
    return newdf[col].min()
    pass

# returns the mean of column col for rows with a birth_month > gt
def get_mean_by_birth_month(df,gt,col):
    # complete this function
    newdf = df.query(f"birth_month>{gt}")
    return newdf[col].mean()
    pass

if __name__ == '__main__':
    # the data frame stores animal information for a local shelter
    name = ['zoe','sadie','linus','sophie','heidi', 'tobey','jasper']
    sex = ['female','female','male','female','female','male','male']
    shy = [True, False, True, False, False, False , False]
    meow_volume = [10,10,8,4,12,6,10]
    # 0=unknown, 1=january, 2=februrary, ... and so on
    birth_month = [3,0,6,0,0,9,4]
    
    cats = pd.DataFrame({
        'name':name,
        'sex':sex,
        'shy':shy,
        'meow_volume':meow_volume,
        'birth_month':birth_month
    })
    print(get_min_by_sex(cats,'male','meow_volume'))
    print(get_mean_by_birth_month(cats,0,'meow_volume'))
    
#Practice #9
def min_max_stock(filename):
    # code goes here
    file = open(filename)
    stocks = file.readline().split(',')
    stocklist = []
    for i in stocks:
        stocklist.append(int(i))
    minval = stocklist[0]
    maxval = stocklist[0]
    
    for j in stocklist:
        if j >= maxval:
            maxval = j
        
        elif j <= minval:
            minval = j
            
    stockstuple = (minval, maxval, stocklist)
    return stockstuple
    
if __name__ == '__main__':
    # you can use this to test your code
    print(min_max_stock('stock_prices_1.csv'))