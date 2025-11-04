class BankAccount:
    def __init__(self, account_number, initial_balance):
        if not account_number or not isinstance(account_number, str):
            raise ValueError("Номер счета должен быть непустой строкой")
        
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        try:
            val = int(amount)
        except ValueError:
            print("Это не int")
            
        if amount > 0:
            self.balance += amount
            return f"Вы пополнили баланс на {amount}. Баланс: {self.balance}"
        
    def withdraw(self, amount):
        try:
            val = int(amount)
        except ValueError:
            print("Это не int")
        if amount <= 0:
            raise ValueError("Вы не можете снять отрицательную сумму")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")       
        self.balance -= amount
    def get_info(self):
        return f"Номер аккаунта {self.account_number}. Баланс: {self.balance}"
    

if __name__ == "__main__":
    try:
        account1 = BankAccount("", -1200)
    except ValueError as e:
        print(f"Ошибка {e}")
    try:
        account2 = BankAccount(3245, 200)
        account2.withdraw(7500)
        account2.deposit(-620)
        account2.get_info()
    except ValueError as e:
        print(f"Ошибка {e}")
    try:
        account3 = BankAccount(67434, 7200)
        account3.withdraw(7200)
        account3.withdraw(0)
        account3.deposit(-20)
        account3.get_info()
    except ValueError as e:
        print(f"Ошибка {e}")
    try:
        account4 = BankAccount("Jhon", 9200)
        account4.withdraw(-600)
        account4.get_info("abs")
        account4.deposit("640")
    except ValueError as e:
        print(f"Ошибка {e}")
    try:
        account5 = BankAccount(545364, "absdbd")
    except ValueError as e:
        print(f"Ошибка {e}")