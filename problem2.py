def p2():
    inlist = input().split()
    inlist2 = input().split()
    inlist_all = inlist + inlist2
    inlist_all.sort(reverse=True)
    print(" ".join(inlist_all))
