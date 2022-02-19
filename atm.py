from pip import main


class atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin
    def check_balance(self):
        print("your balance is 50000")
    def withdrawel(self,amount):
        new_amount=50000-amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))
def main():
    card_number=input("insert your card number")
    pin_number=input("enter your pin number")
    new_user=atm(card_number,pin_number)
    print("choose your activities")
    print("1.balance enquiry 2.withdrawel ")
    activity=int(input("enter activity number"))
    if (activity==1):
        new_user.check_balance()
    elif(activity==2):
        amount=int(input("enter the amount"))
        new_user.withsrawel(amount)
    else:
        print("please enter a valid number")
if __name__ == "__main__": main()
           