# class Train:
#     def __init__(self , name , seat ,fare ) -> None:
#         self.name = name
#         self.seat = seat
#         self.fare = fare

#     def nameOfTrain(self):
#         print(f" Indian Railway : {self.name}")

#     def Trainfare(self):
#         print("*********************")
#         print(f"fare of {self.name} train is : {self.fare} ")
#         print("*********************")

#     def booking(self):
#         if(self.seat > 0):
#             print("*************************")
#             print(f"seat is avilable you can book you seat {self.seat}")
#             print("******************")
#             self.seat -= 1

#         else:
#             ("Sorry ! seat are not avilable !")


# intercity = Train("SamparkKaranti" , 2 , 456)

# intercity.nameOfTrain()
# intercity.Trainfare()
# intercity.booking()

'''
1 2 3 4 5 6 7 8 9 10
'''

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self, seatNo):
        pass

intercity = Train("Intercity Express: 14015", 90, 2)
intercity.getStatus() 
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()



    
        