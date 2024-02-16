print("Welcome to the world of python 😀")

# num1 = int(input())
# num2 = int(input())

# print(float(num1 + num2))

# string = str(input("Enter your company name -> "))
# print(string)

# string2 = input("Enter your 2nd company name -> ")
# print(string2)

'''To take multiple values or inputs in one line by two methods. 
 Using split() method
 Using List comprehension''' 


# split() method
# x,y = input().split(',')
# print("X =", x)
# print("Y =", y)
'''
x,y,z = input().split('-')
print("X = ", x, type(x))
print("Y = ", y, type(y))
print("Z = ", z, type(z))'''

a,b,c = input().split(',')
print("{} {} ka {} ".format(a,b,c))