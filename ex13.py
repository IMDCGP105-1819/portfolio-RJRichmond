def remove_dups(L1, L2):
    for e in range(5):
        if e in L2:
            L1.remove(e)


L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]

remove_dups(L1, L2)
# Didnt work as expected since for e in l1 would take the first number in list being 1 and run the loop one time.
