def arrange(x,y,z):
    lst = [x,y,z]
    #print(lst)
    arr = lst.sort() #use a sort function to arrange three numbers from small to large
    print(arr)
    return 

arrange(3,1,9)


 class Calculator(): 
     def __init__(self,a,b): 
         self.a=a 
         self.b=b 
     
     def add(self): 
         return self.a+self.b 
     
     def mul(self): 
         return self.a*self.b 
     
     def div(self): 
         return self.a/self.b 
     
     def sub(self): 
         return self.a-self.b 
     
     def main(): 
         user_input='' 
         while user_input!='quit': 
             user_input=input("Enter ") 
             if user_input[0] in ['+','-','*','/']: 
                 symbol=user_input[0] 
                 num1=last_result 
                 num2=int(user_input[1]) 
                 
            else: 
                num1=int(user_input[0]) 
                symbol=user_input[1] 
                num2=int(user_input[2]) 
                cal=Calculator(num1,num2) 
                
                if symbol=='+': 
                    last_result=cal.add() 
                    
                elif symbol=='-': 
                    last_result=cal.sub() 
                    
                elif symbol=='*': 
                    last_result=cal.mul() 
                    
                elif symbol=='/': 
                    last_result=cal.div() 
                    
                print(last_result) 
                
                main()