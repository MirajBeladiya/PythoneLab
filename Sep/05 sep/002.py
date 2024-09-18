class My_bank:

    def __init__(self,account_no, balance):
        self.balance = balance
        self.__account_no = account_no

    def deposite(self,amount):
        self.balance = self.balance + amount
    def check_balnce(self):
        print(self.balance)


icici = My_bank(123456,100)
icici.deposite(100)
icici.check_balnce()