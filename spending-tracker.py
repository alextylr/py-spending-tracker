
from csv import reader

opened = open('Checking1.csv')
read_file = reader(opened)
checking_data = list(read_file)

transactions = []
merchants = []

count = 0
for data in checking_data:
    # get all the transaction amounts + the merchants
    transactions.append(data[1])
    merchants.append(data[-1])
for i in range(len(merchants) -1):
    merchants[i] = merchants[i].split(' ')
    if 'PURCHASE' in merchants[i]:   
        merchants[i] = merchants[i][4]
    if merchants[i] == 'STARBUCKS' or 'CHIPOTLE':
        count += 1
        print(count)
       


# convert all transaction amounts from strings to floats
list_of_transactions = [float(item) for item in transactions]


# print(merchants)
total_spent = sum(list_of_transactions)
print("This month Allie spent a total of $", str(total_spent), "this month!")
