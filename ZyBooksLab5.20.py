''' Type your code here. '''
user_int = []
result = []
while True:
  user_input = int(input())
  user_int.append(int(user_input))

  if len(user_int) > (int(user_int[0]) + 1):
    break

end_num = user_int[-1]

user_int.pop(0)
user_int.pop(-1)
output = str()

for vals in user_int:
  if vals <= end_num:
    output = output + str(vals) + ','
print(output, end='')
