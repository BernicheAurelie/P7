from csv import DictReader
import time

with open('table_share_original.csv', 'r') as csv_file:
    """ get csv_reader object using DictReader() and
    pass it to list() to get a list of lists"""
    csv_reader = DictReader(csv_file, delimiter = '\t')
    table_shares = list(csv_reader)

with open('dataset1_P7.csv', 'r') as csv_file:
    """ get csv_reader object using DictReader() and
    pass it to list() to get a list of lists"""
    csv_reader = DictReader(csv_file, delimiter = '\t')
    dataset1 = list(csv_reader)

with open('dataset2.csv', 'r') as csv_file:
    """ get csv_reader object using DictReader() and
    pass it to list() to get a list of lists"""
    csv_reader = DictReader(csv_file, delimiter = ',')
    dataset2 = list(csv_reader)


def remove_data(data):
    """clean data removing all negatives or null values"""
    cleaned_data = []
    for share in data:
        if not (share['price']=="0" or share['price']=="0.0" or "-" in share['price']) :
            cleaned_data.append(share)
    return cleaned_data

dataset1 = remove_data (dataset1)
dataset2 = remove_data(dataset2)



def benefice_share(share):
    """calculate shares profits from price and given percentage profit """
    benefice_share = float(share['price'])*float(share['profit'])/100
    return benefice_share

def share_price(share):
    """return share's price from share"""
    return share["price"]

def total_price(table):
    """return the sum of shares price in table"""
    price_t = 0
    for share in table:
        price_t = price_t + float(share['price'])
    return price_t

def total_benefice(table):
    """calculate shares' profits in table and return the sum"""
    benefice_t = 0
    for share in table:
        benefice_share = float(share['price'])*float(share['profit'])/100
        benefice_t = benefice_t + benefice_share
    return benefice_t

def optimized(table, price_max):
    """sort table in profits' order,
    browse table share by share 
    and append a shares list with share 
    while cumulated price is under maximal price """
    start = time.perf_counter()
    sort_table = sorted(table, key=benefice_share, reverse=True)
    share_prices = 0
    optimized_solution = []
    i = 0
    while i < len(sort_table) and share_prices <= price_max:
        share = sort_table[i]
        price = float(share_price(share))
        if share_prices + price <= price_max:
            optimized_solution.append(share)
            share_prices = share_prices + price
        i += 1
    print("Optimized solution: ")
    for share in optimized_solution:
        name = share["name"]
        price = share["price"]
        print(f"name: {name}, price: {price}€")
    
    print("price: ", total_price(optimized_solution))
    print("profits: ", total_benefice(optimized_solution))
    end = time.perf_counter()
    print("The time used to find optimized solution is given below")
    print(end - start)

# print("\nOptimized choice for table shares: ")
# optimized(table_shares, 500)
# print("\nOptimized choice for dataset1: ")
# optimized(dataset1, 500)
print("\nOptimized choice for dataset2: ")
optimized(dataset2, 500)
