from csv import DictReader
import time
from tqdm import tqdm


with open('table_share_original.csv', 'r') as csv_file:
    csv_reader = DictReader(csv_file, delimiter = '\t')
    # Passing the cav_reader object to list() to get a list of lists
    table_shares = list(csv_reader)

def brute_force(table, invested_price_max):
    start = time.time()
    #nbr of shares
    n=len(table)
    #list comprehension: all integers between 0 and 2**n-1
    tab_integers=[i for i in range (2**n)]
    #binary conversion of tab_integers and suppression of first and second characters with [2:]
    tab_bin=[bin(integer)[2:] for integer in tab_integers]
    # On veut des mots binaires de longueur 20 avec toutes nos shares prises ou pas (1 ou 0)
    # pr chaque mot binaire on rajoute des 0 devant pour avoir 20 caractères
    combinations = ["0"*(n-len(k)) + k for k in tab_bin]
    combinations_valid = []
    for combi in tqdm(combinations):
        invested_price_combi = 0
        benefice_combi = 0
        
        for i in range (n):
            if combi[i] == "1":
                invested_price_combi = invested_price_combi + float(table[i]['price'])
                benefice_share = float(table[i]['price'])*float(table[i]['profit'])/100
                benefice_combi = benefice_combi + benefice_share
        if invested_price_combi <= invested_price_max:
            combinations_valid.append((combi, benefice_combi))
    optimal_solution = combinations_valid[0][0]
    benefice_max = combinations_valid[0][1]
    for combi in combinations_valid:
        if combi[1] > benefice_max:
            benefice_max = combi[1]
            optimal_solution = combi[0]
    combi_shares_optimal = []
    invested_price_total = 0
    for i in range (len(optimal_solution)):
        if optimal_solution[i]=="1":
            combi_shares_optimal.append(table[i]['name'])
            invested_price_total = invested_price_total + float(table[i]['price'])
    print("\nOptimal combination : ",combi_shares_optimal)
    print("\nTotal Invested_price : ", invested_price_total)
    print("\nbenefice max : ", benefice_max)
    end = time.time()
    algo_time = end - start
    print("\nThe time used to find brute force solution is: ", algo_time, "\n")
    return combi_shares_optimal

brute_force(table_shares, 500)
