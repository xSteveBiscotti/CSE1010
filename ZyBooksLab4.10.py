''' Type your code here. '''
red = int(input())
green = int(input())
blue = int(input())

if red < green:
    if red < blue:
        print((red - red), (green - red), (blue-red))
elif green < red:
    if green < blue:
        print((red - green), (green - green), (blue - green))
else:
        print((red - blue), (green - blue), (blue - blue))
