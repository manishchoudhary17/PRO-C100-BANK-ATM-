class Atm(object):
        def __init__(self,cardNumber,pinNumber,balance):
                self.cardNumber = cardNumber
                self.pinNumber = pinNumber
                self.balance = balance

        def BalanceEnquiry():
                print(self.balance)

        def CashWithdrawl():
                cashAmount = input("Enter the withdrawl amount: ")
                self.balance = self.balance-cashAmount
                print("Now your balance is: ",self.balance)   

ATM1 = Atm(1234,6453,10000)
ATM2 = Atm(6758,8768,50000)
CashWithdrawl()                           
