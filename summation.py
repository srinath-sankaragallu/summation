def summation(list_1 = None , type_var = None):
    if list_1:
        result = type_var()
        print(result.r)
        if not hasattr(type_var , '__add__'):
            raise TypeError('unsupported operand type for + : ' + str(type_var))

        for element in list_1:
            if isinstance(element,type_var):
                    result =result + element  
                    #result += element                    
        return result
    else:
        return None

    

#------------------------------------------#
#------ example as shown below ------------#
# class c:
#     r = None
#     def __init__(self,r = 0):
#         self.r = r
    
#     def __add__(self,other):
#         return c(self.r + other.r)

# c1 = c(5)
# c2 = c(10)


# print(5 + 10)
# k = summation([1,2,[1,2],[3,4], 'hi','hello' , {1,2} , {3,4} , c1,c2] , c )
# print(k.r)
# del k

