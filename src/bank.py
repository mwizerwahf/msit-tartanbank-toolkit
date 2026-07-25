class Account:
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
        return True

    def withdraw(self, amount):
        if amount <= 0:
            return False
        if amount > self.__balance:
            return False
        self._adjust_balance(-amount)
        return True


class Ledger:
    def __init__(self, accounts:dict,flagged:list):
        self.accounts = accounts
        self.flagged = flagged

    def apply(self, id, type, amount):
        if id not in self.accounts:
            self.accounts[id] = Account(id)
        if type.lower() == "deposit":
            self.accounts[id].deposit(amount)
            return True
        elif type.lower() == "withdraw":
            feedback = self.accounts[id].withdraw(amount)
            if not feedback:
                self.flagged.append((id,amount))
                return True
            return True

    def get_or_create(id):
        pass

    def summary():
        pass
