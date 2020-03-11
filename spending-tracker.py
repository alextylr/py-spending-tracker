
from csv import reader
opened = open('Checking1.csv')
read_file = reader(opened)
checking_data = list(read_file)

transactions = []
merchants = []
merchants_parsed = []


for data in checking_data:
    # get all the transaction amounts + the merchants
    transactions.append(data[1])
    merchants.append(data[-1])
for i in range(len(merchants) -1):
    merchants[i] = merchants[i].split(' ')
    if 'PURCHASE' in merchants[i]:   
      merchants[i] = merchants[i][4]

      print(merchants)
# for x in range(len(transactions)-1):
#     transactions[x] = float(transactions[x])
      
       
# total_spent = sum(transactions)

# print("You've spent", total_spent)

print(merchants)
