# Define your function here
def seconds_to_jiffies(user_seconds):
    return user_seconds * 100
if __name__ == '__main__':
    # Type your code here.
    user_seconds = int(input())
    jiffies = user_seconds * 100
    print('{:.2f}'.format(jiffies))