import csv


# file = open("data.csv", "w")    # we cannot use path class here. so we open a csv file in write mode
# file.close()  #close kore dite hobe  , othoba nicher moto kore korle close korar dorkar hobena.

with open("data.csv", "w") as file:
    writer = csv.writer(file)                # csv writer create er jonno use kora hoy. r eikhane argument hisebe ekta file
                                    # object use korte hoy. jar karone eikhane path use kora hoyna.
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1040, 3, 10])

# the way to read a csv file ========= ========= ========== ========
with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))      # list akare amra file tar value guloke read kortechi. eita commentout na korle nicher
                               # ta execute hobena. karon eita list a convert howar somoy eikhane close hoyea jacche.
    csv_list = list(reader)
    for row in csv_list:
        print(row)