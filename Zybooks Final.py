def divisible_by(list1, int1):
    # code goes here
    newList = []
    for i in list1:
        if (i%int1) == 0:
            newList.append(i)
    return newList


    
if __name__ == "__main__":
    # use this to test your function
    test_list = [2, 9, 4, 19, 20, -3, -15]
    print(divisible_by(test_list, 3))



#def paint_cost(color, gallons):
#    paint_dict = {
#        'red':5,
#        'yellow':7,
#        'blue':9
#        }
#    # populate the paint_dict with appropriate entries
#    print(paint_dict['red'])
#    if color == 'red':
#        return paint_dict['red'] * gallons

    # code goes here
#print(paint_cost('red',17))
def paint_cost(color, gallons):
    paint_dict = {
        'red':5,
        'yellow':7,
        'blue':9
        }
    # populate the paint_dict with appropriate entries
    if color == 'red':
        return gallons * paint_dict['red']
    elif color == 'yellow':
        return gallons * paint_dict['yellow']
    elif color == 'blue':
        return gallons * paint_dict['blue']
    else:
        return -1
    
        
    print(paint_color(red,2))