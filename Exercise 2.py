#----------- FAULTY CALCULATER ---------------##

print("enter the first numbers ")
num1=int(input())

print("enter the second numbers ")
num2=int(input())

print("Enter the operator you want to use","[+,-,*,/]")
num3=input()

print("Then the result are")
num4 = int(num1) and int(num2)


if num1==45 and num2==3 and num3=="*":
    print("555")

elif num1==56 and num2==9 and num3=="+":
    print("77")

elif num1==56 and num2==6 and num3=="/":
    print("4")

elif num3=="+":
    add=num1+num2
    print(add)

elif num3=="-":
    sub=num1-num2
    print(sub)

elif num3=="*":
    mul=num1*num2
    print(mul)

elif num3=="/":
    div=num1/num2
    print(div)

else:
    print("!!!!!! error!!!!")

