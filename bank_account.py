class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            return "Вы ничего не внесли"
        if amount > 0:
            self.balance += amount
            return f"Вы пополнили баланс на {amount}. Баланс: {self.balance}"
        
    def withdraw(self, amount):
        if amount <= 0:
            return "Error"
        if amount > self.balance:
            return "Недостаточно средств"
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Вы сняли {amount}. Баланс: {self.balance}"
    def get_info(self):
        return f"Номер аккаунта {self.account_number}. Баланс: {self.balance}"
    

if __name__ == "__main__":
    first_bank_account = BankAccount(4235532, 3500)
    second_bank_account = BankAccount(4412345, 1200)
    first_bank_account.deposit(750)
    first_bank_account.deposit(1200)
    first_bank_account.withdraw(8000) #должно вызвать ошибку
    first_bank_account.get_info()
    
    second_bank_account.deposit(-1250)
    second_bank_account.withdraw(-120)
    second_bank_account.get_info()
