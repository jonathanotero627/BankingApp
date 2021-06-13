import datetime
import pytz


class Account:
    """Simple Bank App innit """

    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print("An account has been created slime!")

    def deposit(self,amount):
        self.balance += amount
        self.show_balance()
        self.transaction_list.append((Account._current_time(),amount))

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(),-amount))
            self.show_balance()
        else:
            print("Amount your trying to withdraw must be greater than 0 & less than your available funds")
            self.show_balance()

    def show_balance(self):
        print("Your current balance is: {}".format(self.balance))

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))

if __name__ == '__main__':
    jony = Account("Y",500)
    jony.show_balance()

    jony.deposit(40)
    jony.withdraw(234)
    jony.show_transaction()
