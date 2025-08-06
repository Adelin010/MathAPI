class BankAccount():
    def __init__(self):
        self.__balance = 0.0

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, balance: float):
        if balance < 0:
            raise Exception("No Balance under 0...")
        self.__balance = balance

    
    def deposite(self, value: float) -> int:
        if value < 0:
            raise Exception("At deposite the value deposited must be above 0")
        self.balance += value
        return 0

    def withdraw(self, value: float) -> int:
        if value < 0:
            raise Exception("At deposite the value deposited must be above 0")
        
        if value > self.balance:
            raise Exception("Withdrawing value must be below or equal to the balance")

        self.balance -= value