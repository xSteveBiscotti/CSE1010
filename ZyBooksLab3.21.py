# Define your function here.
def swap_values(user_val1, user_val2):
    print(user_val2 , user_val1)
    return(user_val2 , user_val1)
if __name__ == '__main__': 
    # Type your code here. Your code must call the function.
    user_val1 = int(input())
    user_val2 = int(input())
    swap_values(user_val1, user_val2)