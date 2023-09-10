class BankAccount:
    def _init_(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Deposit: +${amount}')
            return f'Deposited ${amount}. New balance: ${self.balance}'
        else:
            return 'Invalid amount for deposit.'

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Withdraw: -${amount}')
            return f'Withdrawn ${amount}. New balance: ${self.balance}'
        else:
            return 'Invalid amount for withdrawal or insufficient funds.'

    def transfer(self, recipient_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append(f'Transfer: -${amount} to {recipient_account.account_number}')
            recipient_account.transaction_history.append(f'Transfer: +${amount} from {self.account_number}')
            return f'Transferred ${amount} to {recipient_account.account_number}. New balance: ${self.balance}'
        else:
            return 'Invalid amount for transfer or insufficient funds.'

    def display_balance(self):
        return f'Account Balance: ${self.balance}'

    def display_transaction_history(self):
        return '\n'.join(self.transaction_history)

    def reset_account(self):
        self.balance = 0
        self.transaction_history.clear()
        return 'Account has been reset.'

    def exit_atm(self):
        return 'Thank you for using the ATM. Have a great day!'

def main():
    account1 = BankAccount('12345', 'John Doe')
    account2 = BankAccount('67890', 'Jane Smith')

    while True:
        print('\n===== ATM Menu =====')
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Transfer')
        print('4. Display Balance')
        print('5. Transaction History')
        print('6. Reset Account')
        print('7. Exit')

        choice = input('Enter your choice (1-7): ')

        if choice == '1':
            amount = float(input('Enter the deposit amount: $'))
            print(account1.deposit(amount))

        elif choice == '2':
            amount = float(input('Enter the withdrawal amount: $'))
            print(account1.withdraw(amount))

        elif choice == '3':
            recipient = account2 if account1.account_number != '12345' else account1
            amount = float(input('Enter the transfer amount: $'))
            print(account1.transfer(recipient, amount))

        elif choice == '4':
            print(account1.display_balance())

        elif choice == '5':
            print(account1.display_transaction_history())

        elif choice == '6':
            print(account1.reset_account())

        elif choice == '7':
            print(account1.exit_atm())
            break

        else:
            print('Invalid choice. Please select a valid option (1-7).')

if _name_ == "__main__":
    main()
