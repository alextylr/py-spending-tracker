
from csv import reader
opened = open('Checking1.csv')
read_file = reader(opened)
checking_data = list(read_file)

transactions = []
merchants = []


for data in checking_data:
    # get all the transaction amounts + the merchants
    transactions.append(data[1])
    merchants.append(data[-1])

# convert all transaction amounts from strings to floats
list_of_transactions = [float(item) for item in transactions]



total_spent = sum(list_of_transactions)
print("This month Allie spent a total of $", str(total_spent), "this month! Maybe she should stop eating so much Chipotle :)")