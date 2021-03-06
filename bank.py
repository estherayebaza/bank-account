from datetime import datetime,time
now=datetime.now()
class Account:
    def __init__(self,accountNumber,phoneNumber,name,loan_limit):
        self.accountNumber=accountNumber
        self.phoneNumber=phoneNumber
        self.name=name
        self.loan=0
        self.balance=0
        self.loan_limit=loan_limit
        self.transactions=[]
        self.withDraws=[]
        self.loans=[]
        self.repay_loan=[]
    def deposit(self,amount):
        try:
              10+amount
        except TypeError:
            return f"The amount must be in figures "
        if amount<=0:
 
            return f"The amount must be greater than zero"
        else:
            self.balance+=amount
            transaction={
                "amount":amount,
                "balance":self.balance,
                "time":now.strftime("%D"),
                "narration":"Deposit"
                }
            self.transactions.append(transaction)
            return f"Dear {self.name} you have deposited {amount} your balance is {self.balance}"
    def get_statement(self):
        for transaction in self.transactions:
            narration=transaction["narration"]
            amount=transaction["amount"]
            balance=transaction["balance"]
            time=transaction["time"]
            print (f"{time}.. {narration}..{amount}..Balance{balance}")

    def show(self,balance):
            return self.balance

    def withDraw(self,amount):
        try:
              10+amount
        except TypeError:
                 return f"The amount must be in figures "
        if amount<0:
            return "You can't withdraw negative amount "
        elif amount>self.balance:
            return "You can have insufficient balance"
        else:
             self.balance-=amount
             withDraw_transaction={
                "amount":amount,
                "balance":self.balance,
                "time":now.strftime("%D"),
                "narration":"WithDraw"
                }
             self.withDraws.append(withDraw_transaction)
             return f"You have successfully withdrawn {amount} your balance is {self.balance}"
    def borrow(self,amount):
        try:
              10+amount
        except TypeError:
                 return f"The amount must be in figures" 
        if amount>=self.loan_limit:
            return f"You cant borrow"
        elif self.loan>0:
            return f"You already have an existing loan"
        else:
            self.loan+=1
            self.balance+=amount
            loan_transaction={
                "amount":amount,
                "balance":self.balance,
                "time":now.strftime("%D"),
                "narration":"Loan"
                }
            self.loans.append(loan_transaction)
            return "You have successfully borrowed"
    def repayLoan(self,amount):
        if amount<=0:
            return "Please deposit a positive amount"
        elif amount<self.loan:
            self.loan-=amount
            return f"You have paid {amount} on your loan"
        else:
            diff=amount-self.loan
            self.balance+=diff
            self.loan=0
            return f"You have fully paid your loan and your balance is {self.balance}"
    def transfer(self,amount,account):
        try:
              10+amount
        except TypeError:
                 return f"The amount must be in figures"
        fee=amount*0.005
        if amount+fee>self.balance:
            return f"your balance is {self.balance} and you need {amount+fee} to complete the transaction"
        else:
            self.balance=amount+fee
            account.deposit(amount)
            return f"you have sent {amount} to {account.name} and your balance is {self.balance}"

class MobilemoneyAccount(Account):
    def __init__(self,accountNumber,phoneNumber,name,loan_limit,serviceProvider):
        Account.__init__(accountNumber,phoneNumber,name,loan_limit)
        self.serviceProvider=serviceProvider
        self.limit=20000000
    def buy_airtime(self,amount):
        try:
              10+amount
        except TypeError:
                 return f"The amount must be in figures"
        if amount<0:
            return f"Enter a positive amount"
        elif amount>self.balance:
            return f"You have insufficient balance"
        else:
            self.balance-=amount
 












