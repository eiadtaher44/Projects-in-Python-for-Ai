class Couloutors:
    
    def Division(self,num1,num2):
        if num2==0:
            raise ZeroDivisionError("can not div by zero ..")
        return num1/num2

    @staticmethod
    def power(base: int,exp:int):
        if exp <0:
            raise ValueError("Negative number..!")
        return base**exp
    
    def get_item(self, vale,index):
        if len(vale)==0:
            raise IndexError("the list is empty")
        if index<0 or index>=len(vale):
            raise IndexError("index is out of limeted..!")
        return vale[index]
    
    def get_avreag(self,number):
        if len(number)==0:
            raise ValueError("can not calcolutr of avrag is empty list..!")
        return sum(number)/len(number)
    

if __name__=="__main__":
    cal=Couloutors()
    
    print("Divgson :")
    try:
        print(cal.Division(16, 2))
        print(cal.Division(10, 0))
    except Exception as e:
        print("Error..",e)
    
    print("power :")
    
    try:
        print(cal.power(2, 3))
        print(cal.power(2,-2))
        
    except Exception as e:
        print("Error..",e)

    print("get elment ..")
    
    try:
        my_list=[10,30,40]
        print(cal.get_item(my_list, 2))
        print(cal.get_item(my_list, 5))
    except Exception as e:
        print("index  Error..",e)

    print(" Avg :")
    try:
        my_list2=[10,20,30,50,99]
        print(cal.get_avreag(my_list2))
        print(cal.get_avreag([]))
    except Exception as e:
        print("avg error :",e)
            
            
            