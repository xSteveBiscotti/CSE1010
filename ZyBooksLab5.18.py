''' Type your code here. '''
num_1 = int(input())

num_2 = int(input())

if num_1 > num_2:

        print("Second integer can't be less than the first.", end='')

for x in range(num_1, num_2+1, 5):

    print('{} '.format(x), end='')

print('')