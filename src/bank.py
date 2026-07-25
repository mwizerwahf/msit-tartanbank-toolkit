class Account:
    all_deposits = []
    all_withdrawals = []
    def __init__(self, account_id, balance: float = 0.0):
        self.account_id = account_id
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = balance
        self.opeing_balance = balance
        self.transaction_count = 0

    def get_balance(self):
        return self.__balance
    
    def _adjust_balance(self, amount):
        if self.__balance + amount < 0:
            raise ValueError("Insufficient funds")
        self.__balance += amount
        self.transaction_count += 1

    def deposit(self, amount):
        if amount <= 0:
            return False
        self._adjust_balance(amount)
        Account.all_deposits.append(amount)
        return True

    def withdraw(self, amount):
        if amount <= 0:
            return False
        if amount > self.__balance:
            return False
        self._adjust_balance(-amount)
        Account.all_withdrawals.append(amount)
        return True


class Ledger:
    def __init__(self, accounts:dict,flagged:list):
        self.accounts = accounts
        self.flagged = flagged

    def apply(self, id, type, amount):
        account = self.get_or_create(id)
        if type.lower() == "deposit":
            account.deposit(amount)
            return True
        elif type.lower() == "withdraw":
            feedback = account.withdraw(amount)
            if not feedback:
                self.flagged.append((id,amount))
                return True
            return True

    def get_or_create(self, id):
        if id not in self.accounts:
            self.accounts[id] = Account(id)
        return self.accounts[id]

    def summary(self):
        total_deposits = sum(_ for _ in Account.all_deposits)
        average_deposit = total_deposits / len(Account.all_deposits) if Account.all_deposits else 0
        total_withdrawals = sum(_ for _ in Account.all_withdrawals)
        average_withdrawal = total_withdrawals / len(Account.all_withdrawals) if Account.all_withdrawals else 0
        return {
            "total_deposits":total_deposits, 
            "average_deposit":average_deposit, 
            "total_withdrawals":total_withdrawals,
            "average_withdrawal":average_withdrawal
            }
