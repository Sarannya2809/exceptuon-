try:
    num1, num2= eval(input("enter two numbers, seperated by a comma: "))
    result = num1/num2
    print("result is", result)
except ZeroDivisionError :
     print("division by zero is error : : ")

except SyntaxError:
     print("comma is missing. Enter numbers seperated by coma like this 1,2")
except:
     print("wrong input")
finally:
     print("this will execute no matter what")

