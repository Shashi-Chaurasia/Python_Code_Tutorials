import random 

print(" Computer guess number in between 1 to 100 : ")
randm = random.randint(1,100)
print(f"computer guessed number is : {randm}")

user = None
guess = 0

while(user != randm):
    user = int(input("Enter your number :?? - "))
    guess += 1
    

    if 1 < user <=100:
        if user > randm:
            print("Plz guess the number lesser !")
            print(f"computer guessed number is : {randm}")
            print(f" You gessed number is :{user}")

        elif user < randm:
            print("Plz guess the number greater !")
            print(f"computer guessed number is : {randm}")
            print(f" You gessed number is :{user}")


        else:
            print("You guess correct !")

            print(f"computer guessed number is : {randm}")
            print(f" You gessed number is :{user}")


    else:
        print("Plz enter your number in between 1 to 100")

    





# import random

# randomNumber = random.randint(1,100)

# user = None
# guess = 1

# while(user != randomNumber):
#     user = int(input("Enter Your number :"))
#     guess += 1





