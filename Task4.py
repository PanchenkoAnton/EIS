from operator import itemgetter
import pymongo

# Connection to the database.

conn = pymongo.MongoClient('localhost', 27017)
db = conn.four
coll_acrual = db.acrual
coll_payment = db.payment

# Getting and sorting data.

acruals, payments, result, sad_payments = [], [], [], []
acruals_len, payments_len = 0, 0

for elem in coll_acrual.find():
    acruals_len += 1
    acruals.append([int(elem['date']), int(elem['month']), -1])
for elem in coll_payment.find():
    payments_len += 1
    payments.append([int(elem['date']), int(elem['month']), -1])
acruals = sorted(acruals, key=itemgetter(1, 0))
payments = sorted(payments, key=itemgetter(1, 0))

# Finding acruals for each payment. If it's impossible - you'll also get the list of the payments without an acrual.

id = 0
for payment in payments:
    added = False
    it = -1
    while it + 1 < acruals_len: # First try: same month
        it += 1
        if acruals[it][2] == -1 and acruals[it][1] == payment[1]:
            acruals[it][2], payments[id][2] = 1, 1
            result.append([payments[id], acruals[it]])
            added = True
            break
    if added == True: # Checking if the acrual was already found. If yes - skip that iteration
        id += 1
        continue
    it = -1
    while it + 1 < acruals_len: # Second try: all previous dates
        it += 1
        if acruals[it][2] == -1 and ((acruals[it][1] < payments[id][1]) or (acruals[it][1] == payments[id][1] and acruals[it][0] < payments[id][0])) :
            acruals[it][2], payments[id][2] = 1, 1
            result.append([payments[id], acruals[it]])
            break
    id += 1
for payment in payments: # Getting the list of the payments without an acrual
    if payment[2] == -1:
        sad_payments.append(payment)

# Printing results

print("\nHint! One row - one pair: payment is on the left and it's acrual is on the right.\n")
for elem in result:
    print(elem)
print("\nHere you may check all payments with no acrual:\n")
for elem in sad_payments:
    print(elem)
