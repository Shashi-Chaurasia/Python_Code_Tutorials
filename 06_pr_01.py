def max(num1 , num2 , num3 , num4):
    if(num1 > num2):
        if(num1>num3):
            if(num1>num4):
                print("gretaest number is :" + str(num1))
    elif(num2 > num3):
        if(num2>num4):
            if(num2>num1):
                print ("gretaest number is :" + str(num2))
    elif(num3 > num4):
        print("greatest number is " + str(num3))
    else:
        print("gretest number is :" + str(num4))

number = max(578,2765734,45,1)
print(number)

    

    