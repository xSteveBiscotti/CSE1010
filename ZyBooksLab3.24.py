koala = """
             |       :     . |
             | '  :      '   |
             |  .  |   '  |  |
   .--._ _...:.._ _.--. ,  ' |
  (  ,  `        `  ,  )   . |
   '-/              \-'  |   |
     |  o   /\   o  |       :|
     \     _\/_     / :  '   |
     /'._   ^^   _.;___      |
   /`    `""""""`      `\=   |
 /`                     /=  .|
;             '--,-----'=    |
|                 `\  |    . |
\                   \___ :   |
/'.                     `\=  |
\_/`--......_            /=  |
            |`-.        /= : |
            | : `-.__ /` .   |
            |    .   ` |    '|
            |  .  : `   . |  |"""


def exec_2(f):
    f()
    f()

def exec_4(f):
    # define this function using exec_2
    f()
    f()
    f()
    f()
# define a new function here that prints out the koala once
def print_koala():
    print(koala, end='')
# use your function and exec_4 to draw 4 koala bears!
exec_4(print_koala)