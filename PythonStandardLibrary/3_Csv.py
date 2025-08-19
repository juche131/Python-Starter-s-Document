import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    print(type(writer))  # <class '_csv.writer'>
    writer.writerow(["transaction_id", "product_id", "price.id"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1000, 2, 15])

# D:\000_PersonalDocuments\1_StudyMaterials\Programming\data.csv

with open("data.csv") as file:
    reader = csv.reader(file)
    print(list(reader))
    # [['transaction_id', 'product_id', 'price.id'], ['1000', '1', '5'], ['1000', '2', '15']]

    # iterator index already at the tail of the csv

with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
"""
['transaction_id', 'product_id', 'price.id']
['1000', '1', '5']
['1000', '2', '15']
"""
