class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = int(account_id)
        self.account_type = account_type
        self.pin = int(pin)
        self.balance = float(balance)

    def deposit(self, amount):
        #amount = float(input('Enter the quantity of your deposit'))
        self.balance += amount
        print(f'Your new balance is: ${self.balance}.')

    def withdraw(self, amount):
        #amount = float(input('Enter the quantity you want to withdraw: '))
        self.balance -= amount
        print(f'Your withdrawn amount is: ${amount}.')

    def display_balance(self):
        print(f'Your balance amount is: ${self.balance}')

newAccount = BankAccount('Matheus', 'Muniz', 123456, 'Checking Account', 147852, 10000.57)

newAccount.deposit(1000)
newAccount.withdraw(100)
newAccount.display_balance()