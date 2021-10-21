highway_number = int(input())

''' Type your code here. '''
if highway_number == 0:
    print( str(highway_number) + ' is not a valid interstate highway number.')
if highway_number in range(1, 99+1):
     if highway_number % 2 == 0:
         print('I-'+ str(highway_number) + " is primary, going east/west.")
     else:
          print('I-'+ str(highway_number) + " is primary, going north/south.")
else:
  served = highway_number % 100 
  if highway_number >= 1000:
    print( str(highway_number) + ' is not a valid interstate highway number.')
  if highway_number in range(99, 999+1):
     if highway_number % 2 == 0:
         print('I-'+ str(highway_number)+ ' is auxiliary, serving I-'+'%.f,' %served + ' going east/west.')
     else:
          print('I-' + str(highway_number) + ' is auxiliary, serving I-'+'%.f,' %served + ' going north/south.')
    