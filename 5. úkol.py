teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
""" for prumer in teploty:
    x = sum(prumer)/len(prumer)
    print(x) """
prumerna_teplota = [sum(teploty)/len(teploty) for teploty in teploty]
print(prumerna_teplota)

"""for rano in teploty:
    rano = rano[0]
    print(rano)"""
ranni_teploty = [teploty[0] for teploty in teploty]
print(ranni_teploty)

"""for noc in teploty:
    noc = noc[3]
    print(noc)"""
nocni_teploty = [teploty[3] for teploty in teploty]
print(nocni_teploty)

"""for poledne_a_noc in teploty:
    poledne_a_noc = [poledne_a_noc[1], poledne_a_noc[3]]
    print(poledne_a_noc)"""
poledne_a_noc = [[teploty[1], teploty[3]] for teploty in teploty]
print(poledne_a_noc)