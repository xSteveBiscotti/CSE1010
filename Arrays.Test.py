myList = [
    [0,1,2,3,4],
    [5,6,7,8,9],
    [10,11,12,13,14],
    [15,16,17,18,19]

]

rowcount = 0 
colcount = 0 

for rows in myList:
   rowcount += 1
   for col in rows:
       colcount += 1
    
print('Rows: ' + str(rowcount))
print('Columns: ' + str(int(colcount/rowcount)))



#print(myList[2][3])