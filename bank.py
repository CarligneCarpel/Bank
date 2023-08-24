class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance):
        if initial_balance < 500.0:
            raise ValueError("Balans inisyal la dwe pi plis pase 500.0 Goud.")
        
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Depo {amount} Goud. Nouvo balans: {self.balance} Goud."
        else:
            return "Kantite depo a envalid."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Retire {amount} Goud. Nouvo balans: {self.balance} Goud."
        else:
            return "Fòk nivo lajan oubyen kantite ou retire a envalid."

    def get_balance(self):
        return f"Balans nan kont pou {self.account_holder}: {self.balance} Goud."

    def __str__(self):
        return f"Nimewo Kont: {self.account_number}\nMèt Kont la: {self.account_holder}\nBalans: {self.balance:.2f} HTG"

try:
    kont1 = BankAccount("123456", "Francois Jodany", 100000)
    kont2 = BankAccount("789012", "Paillant Mitche", 75500000)
    kont3 = BankAccount("123456","Carligne Carpel",155000000)
    print("Kont 1:")
    print(kont1)
    print(kont1.deposit(500))
    print(kont1.withdraw(200))
    
    
    print("\nKont 2:")
    print(kont2)
    print(kont2.deposit(1500))
    print(kont2.withdraw(3000))
    
    print("Kont 3:")
    print(kont3)
    print(kont3.deposit(9000000))
    print(kont3.withdraw(500000))
except ValueError as e:
    print(e)
