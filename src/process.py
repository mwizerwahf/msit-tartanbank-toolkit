from bank import Account, Ledger
import sys, os, csv

if len(sys.argv) < 2:
    raise ValueError("Please provide a transaction file path as a command line argument.")
elif not os.path.isfile(sys.argv[1]) or not os.path.exists(sys.argv[1]):
    raise ValueError("The provided transaction file path does not exist or is not a file.")
transactions = sys.argv[1] 
report = sys.argv[2]

ledger = Ledger({}, [])

with open(transactions, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    # print("Processing transactions from file:", transactions)
    
    for line in csv_reader:
        id, type, amount = line
        amount= float(amount)
        ledger.apply(id,type,amount)
        # print(f"Processed transaction: Account ID: {id}, Type: {type}, Amount: {amount}")

with open(report, 'w') as file:
    file.write(f"FINAL REPORT\n{'='*15}\n")
    for id, account in ledger.accounts.items():
        declined_withdrawals = [t[1] for t in ledger.flagged if t[0] == id]
        file.write(f"Acccount: {id}, Balance:{account.get_balance()}, Transanctions count: {account.transaction_count}, Flagged: {declined_withdrawals}\n")
    total_transaction = sum(account.transaction_count for account in ledger.accounts.values())
    file.write(f"Total processed transactions: {total_transaction}\n\n")
    file.write(f"Flagged transactions: {ledger.flagged}\n\n")
    summary = ledger.summary()
    file.write(f"Total deposits: {summary['total_deposits']}\nAverage deposit: {summary['average_deposit']}\n")